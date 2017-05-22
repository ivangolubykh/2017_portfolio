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
from django.conf.urls import url, include
from .views import MainListView, weather_json, ExamplesWorkListView,\
    ExamplesWorkPythonListView, ExamplesWorkJsListView,\
    ExamplesWorkHtmlCssListView, EducationListView, WorksListView


urlpatterns = [
    url(r'^$', MainListView.as_view(), name='main'),
    url(r'^weather.json/$', weather_json, name='weather_json'),
    url(r'^examples_work/$', ExamplesWorkListView.as_view(),
        name='examples_work'),
    url(r'^education/$', EducationListView.as_view(),
        name='education'),
    url(r'^works/$', WorksListView.as_view(),
        name='works'),
]
urlpatterns += [
    url(r'^examples_work/', include([
        url(r'^python_django/$', ExamplesWorkPythonListView.as_view(),
            name='examples_work_python_django'),
        url(r'^js/$', ExamplesWorkJsListView.as_view(),
            name='examples_work_js'),
        url(r'^html_css/$', ExamplesWorkHtmlCssListView.as_view(),
            name='examples_work_html_css'),
        ])),
]
