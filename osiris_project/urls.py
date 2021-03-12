"""osiris_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view	# If I type "from pages.views import home_view"
						 			 			# it is clear I am refering to a specific view, 
						 			 			# and that it belongs to pages (not products)
from products.views import product_detail_view, product_create_view
urlpatterns = [
    path('', home_view, name='home'), # the empty string can be fulled with "contact/" for example
    path('about/', about_view),
    path('contact/', contact_view),
    path('create/', product_create_view),
    path('product/', product_detail_view),
    path('admin/', admin.site.urls)
]

#path('create/', product_create_view),
#path('home/', home_view),