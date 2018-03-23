from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^speech/', views.speech, name='speech'),
    url(r'^hello/$', views.HelloWorldView.as_view(), name='hello'),
    url(r'^$', views.SpeechHomeView.as_view(), name='home'),

    url(r'^list/', views.PatientListView.as_view(), name='patient_list'),
    url(r'^list(?P<pk>\d+)/', views.PatientDetailView.as_view(), name='patient_detail'),

    url(r'^udemy/', views.udemy, name='udemy'),


]