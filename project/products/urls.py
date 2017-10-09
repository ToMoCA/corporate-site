from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(\w+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
