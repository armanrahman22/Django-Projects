from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^phikaps2015areawesome/$', views.Display, name='display'),
    url(r'^delete/$',views.delete_location, name="delete location"),
    url(r'^vote/$', views.vote, name='vote'),
    )