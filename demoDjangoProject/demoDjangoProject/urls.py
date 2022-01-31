"""demoDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from demoapp.views import index
from demoapp.views import create_contact
from demoapp.views import contact_list
from demoapp.views import create_customer
from demoapp.views import list_customers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demoapp', index, name='index'),
    path('demoapp/contact/create', create_contact, name='create-contact'),
    path('demoapp/contact/contactlist', contact_list, name='contact-list'),
    path('demoapp/customer/create', create_customer, name='create-customer'),
    path('demoapp/customer/list', list_customers, name='list-customer'),
]
