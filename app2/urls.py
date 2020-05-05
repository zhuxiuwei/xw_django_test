# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'polls2'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index2'),
    # 注意以下两行，用的是pk，不是question_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail2'),
    url(r'^(?P<pk>[0-9]+)/results2/$', views.ResultsView.as_view(), name='results2'),
    url(r'^(?P<question_id>[0-9]+)/vote2/$', views.vote, name='vote2'),
]