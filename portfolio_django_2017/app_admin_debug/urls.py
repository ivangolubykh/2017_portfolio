"""django_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from .views import AdminListView, H1Create, H2Create, H3Create, H4Create, \
    TextCreate


urlpatterns = [
    url(r'^admin/$', AdminListView.as_view(), name='admin'),
    url(r'admin/add_h1/$', H1Create.as_view(), name='admin-add_h1'),
    url(r'admin/add_h2/$', H2Create.as_view(), name='admin-add_h2'),
    url(r'admin/add_h3/$', H3Create.as_view(), name='admin-add_h3'),
    url(r'admin/add_h4/$', H4Create.as_view(), name='admin-add_h4'),
    url(r'admin/add_text/$', TextCreate.as_view(), name='admin-add_text'),
]
