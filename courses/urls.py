from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step'),# above course_detail b/c this url is more specific, dont want it to be satisfied with just 'pk' in course_detail
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]

