# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    Category model is used to maintain product category such as
    1. Veg
    2. Non-Veg
    3. Vegan
    """
    name = models.CharField(max_length=50, verbose_name=_("name"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ScientificCode(models.Model):
    """
    Scientific codes that are used in the product Ingredient
    """
    code = models.CharField(max_length=50, verbose_name=_("Code"))
    details = models.TextField(max_length=500, verbose_name=_("Details"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))

    class Meta:
        verbose_name = _("Scientific Code")
        verbose_name_plural = _("Scientific Codes")
        ordering = ['-id']

    def __unicode__(self):
        return self.code

    def __str__(self):
        return self.code


class Ingredient(models.Model):
    """
    Ingredient model is used to maintain the list of ingredients used in any product.
    """
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    description = models.CharField(max_length=500, verbose_name=_("Description"), blank=True, null=True)
    code = models.ForeignKey(ScientificCode, verbose_name=_('Code'), blank=True, null=True,
                             related_name='ingredient_code', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ProductCompany(models.Model):
    """
    Class for product company details
    """
    name = models.CharField(max_length=50, verbose_name=_("Company Name"))
    website = models.CharField(max_length=50, verbose_name=_("Website"), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


def get_upload_path(instance, filename):
    """ creates unique-Path & filename for upload """
    return os.path.join('static/images', instance.company.name, instance.name, filename)


class Product(models.Model):
    """
    This model is design to maintain the Product details.
    """
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    company = models.ForeignKey(ProductCompany, verbose_name=_('Company Name'), related_name='product_company',
                                on_delete=models.CASCADE)
    description = models.CharField(max_length=500, verbose_name=_("Description"), blank=True, null=True)
    front_image = models.ImageField(verbose_name=_('Front Image'), upload_to=get_upload_path)
    back_image = models.ImageField(verbose_name=_('Back Image'), upload_to=get_upload_path)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='product_category',
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    """
    Collect comments from logged in user and  show based on the approval to all users.
    """
    comment = models.TextField(max_length=1000, verbose_name=_("Comment"))
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='product_comment', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, verbose_name=_('Created By'), related_name='user_comment', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    approved_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Product Comment")
        verbose_name_plural = _("Product Comments")
        ordering = ['-id']

    def __unicode__(self):
        return 'Comment by {} on {}'.format(self.created_by, self.product)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.created_by, self.product)
