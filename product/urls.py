
from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePageListView.as_view(), name="home"),
    path('details/<int:pk>/', views.ProductDetailsView.as_view(), name='product-detail'),
    path('contact-us/', views.ContactUsView.as_view(), name="contact-us"),
    path('details/<int:pk>/comment', views.CommentCreateView.as_view(), name='product-comment'),
    path('ajax/search/', views.autocompleteModel),
]