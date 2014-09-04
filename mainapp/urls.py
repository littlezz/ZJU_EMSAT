

from django.conf.urls import patterns, include, url
from mainapp import views

urlpatterns = patterns('',
    url(r'^$', views.welcome, name='welcome'),
    url(r'^create_nickname$', views.create_nickname,name='create_nickname'),
    url(r'^home$', views.home, name='home'),
    url(r'^logout$',views.out,name='logout'),
    url(r'^test_ajax$',views.test_ajax,name='test_ajax'),



)