import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


from .models import Product, ProductComment
from .forms import CommentForm, ProductSearchForm


def prepare_data(objects):
    """
    :return:
    """
    cols = 3
    products = []  # this will be 2d array.
    data = []
    for item in objects:
        if len(data) == cols:
            products.append(data)
            data = [item]
        else:
            data.append(item)
    products.append(data)
    return products


class HomePageListView(ListView):
    model = Product
    template_name = "home.html"
    paginate_by = 10

    def get_queryset(self):
        name = self.request.GET.get('item', None)
        if name:
            return self.model.objects.filter(name__icontains=name.lower())
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = self.get_queryset()
        context['products'] = prepare_data(objects)
        context['form'] = ProductSearchForm()
        return context

class ProductDetailsView(DetailView):
    model = Product
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_product_comments()
        context['form'] = CommentForm()
        context['search_form'] = ProductSearchForm()
        return context

    def get_product_comments(self):
        """
        This method will pull all comments for a given product and login user
        :return:
        """
        return ProductComment.objects.filter(product=self.object, approved_status=True).order_by('-created')


class CommentCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = None
    model = ProductComment
    fields = ['comment']

    def get_success_url(self):
        object_id = self.kwargs[self.pk_url_kwarg]
        return reverse_lazy('product-detail', kwargs={'pk': object_id})

    def form_valid(self, form):
        object_id = self.kwargs[self.pk_url_kwarg]
        try:
            form.instance.created_by = self.request.user
            form.instance.product = Product.objects.get(id=object_id)
            form.save()
        except Exception as ex:
                print(ex)
        return HttpResponseRedirect(self.get_success_url())


class ContactUsView(TemplateView):
    template_name = "contactUs.html"


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Product.objects.filter(name__contains=q).values_list('name', flat=True)
        data = json.dumps(list(search_qs))
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
