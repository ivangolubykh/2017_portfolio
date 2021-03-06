"""portfolio_django_2017 URL Configuration

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
# from django.conf.urls import url
# from django.contrib import admin
from django.conf.urls import url, include
# для редиректа с главной страницы в папку:
from django.views.generic.base import RedirectView
# для раздачи медиа ТОЛЬКО на ТЕСТОВОМ сервере
from django.conf import settings
from django.conf.urls.static import static

__author__ = 'Иван Голубых'

starturl = r'^portfolio/2017_portfolio/'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # редирект с главной страницы в папку:
    url(r'^$', RedirectView.
        as_view(url='portfolio/2017_portfolio/')),
]
urlpatterns += [
    url(starturl, include('app_main.urls')),
]


# для раздачи медиа ТОЛЬКО на ТЕСТОВОМ сервере:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(starturl, include('app_admin_debug.urls')),
    ]
