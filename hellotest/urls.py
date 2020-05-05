from django.conf.urls import url

from hellotest.views import HelloView
from . import views

app_name = 'hello'
urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^doadd/$', HelloView.as_view(), name='doadd'),
    url(r'^$', HelloView.as_view(), name='index'),
]