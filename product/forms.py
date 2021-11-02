# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import ProductComment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments', 'rows': '3',
                                                           'autocomplete': 'off', 'class': 'w3-input w3-border'}))

    class Meta:
        model = ProductComment
        fields = ('comment',)


class ProductSearchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product Name', 'id': 'txtSearch',
                                                         'autocomplete': 'off', 'class': "w3-input w3-right w3-half",
                                                         'style': "margin-top:18px;"}))
