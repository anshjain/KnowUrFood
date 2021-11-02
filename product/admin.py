from django.contrib import admin
from .models import Product, ProductCompany, Category, ScientificCode, Ingredient, ProductComment


admin.site.register([Product, ProductCompany, Category, ScientificCode, Ingredient, ProductComment])