"""yui.urls"""
from django.conf.urls import  url
from . import views
urlpatterns = [
    #url(r'', views.post_list),
    #ファーストマッチングで上記がヒットすることがあるのでコメントアウト。
    # url(r'^$', views.post_list),
    url(r'^$', views.post_list, name='index'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'post/new/', views.post_new, name='post_new'),
    url(r'post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #    url(r'post/(?P<pk>[0-9]+)/$', views.post_detail),
    #    url(r'hachu/$', views.hachu_kanri),
]
