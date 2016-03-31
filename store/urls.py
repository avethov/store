"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from datetime import datetime
from django.conf.urls import patterns, url
from apps.example.forms import BootstrapAuthenticationForm

from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home$', 'apps.example.views.home', name='home'),
    url(r'^contact$', 'apps.example.views.contact', name='contact'),
    url(r'^about', 'apps.example.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'apps.example/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.catalogue.views.index', name='index'),
    url(r'^list1/', include('apps.catalogue.urls')),
    url(r'^list2/', 'apps.catalogue.views.Product2View', name='Product2View'),
    url(r'^akcii/', 'apps.catalogue.views.AkciiView', name='AkciiView'),
)
