from django.contrib import admin
from .models import Author, Category, Product

admin.site.register([Author, Category, Product])
# Register your models here.
