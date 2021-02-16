from django.contrib import admin

# Register your models here.

from .models import Product

# This is a relative import because admin and models 
# are both in the same directory

admin.site.register(Product)