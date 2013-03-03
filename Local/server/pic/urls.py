from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^picture/$', views.PictureList.as_view()),
    url(r'^picture/(?P<pk>[0-9]+)/$', views.PictureDetail.as_view()),
)
