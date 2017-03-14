from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'findbatsmans', views.findBatsman, name='findBatsman'),
    url(r'findbowlers', views.findBowlers, name='findBowlers'),
    url(r'^$', views.index, name='index'),

]
