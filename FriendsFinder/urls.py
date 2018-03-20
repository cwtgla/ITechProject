from FriendsFinder import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
	
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category, name='show_category'),

	url(r'^thread/(?P<thread_title_slug>[\w\-]+)/$',
		views.show_thread, name='show_thread'),

	url(r'^add_thread/$', views.add_thread, name='add_thread'),
	url(r'^thread/(?P<thread_title_slug>[\w\-]+)/add_post/$', views.add_post, name='add_post'),

	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^quiz/', views.quiz, name='quiz'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^results/', views.results, name='results'),
	url(r'^forum/', views.forum, name='forum'),
]

