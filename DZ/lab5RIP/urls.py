"""lab5RIP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from Shop_El.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    url(r'^$', list_view),
    url(r'^admin', admin.site.urls),
    url(r'^list', list_view, name='list_p'),
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^logout', logout, name="logout"),
    url(r'^create/$', ProdCreate.as_view(), name='create'),
    url(r'^product/(?P<id>\d+)', ProdView.as_view(), name='product_url'),
    url(r'^error/$', ErrorView.as_view(), name='error_page'),
    url(r'^order/(?P<id>\d+)/(?P<user_id>\d+)', order, name='order'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
