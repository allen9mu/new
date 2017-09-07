from django.conf.urls import include,url

from . import views

urlpatterns =[
    url(r'^list', views.list_computer, name='list_computer'),
    url(r'^add', views.add_computer, name='add_computer'),
    url(r'^index', views.index, name='index'),

]