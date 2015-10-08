from django.conf.urls import patterns, url
from webapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pkmnrevo/$', views.pkmnrevo, name='pkmnrevo'),
    url(r'^arkanoid/$', views.arkanoid, name='arkanoid'),
    url(r'scrabble/$', views.scrabble, name='scrabble'),
    url(r'tichu/$', views.tichu, name='tichu'),
    url(r'pokyellow/$', views.pokyellow, name='pokyellow')
    )
