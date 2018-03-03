from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^speech/', views.speech, name='speech'),
    url(r'^udemy/', views.udemy, name='udemy'),


]