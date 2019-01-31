"""FWB_Portal URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from portal import views


admin.site.site_title = 'FWB Portal Site Admin'

admin.site.site_header = 'FWB Portal Administration'

admin.site.index_title = 'FWB Portal Administration'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^admin/', admin.site.urls),
]
