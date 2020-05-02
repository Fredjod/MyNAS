'''
Created on 24 déc. 2016

@author: home
'''
from django.conf.urls import url
from nodeAdmin import views

app_name = 'nodeAdmin'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createNode/$', views.createNodeRequest, name='createNodeRequest'),
]