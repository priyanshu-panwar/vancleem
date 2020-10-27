from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('experience/', views.experience, name='experience'),
	path('solutions/', views.solutions, name='solutions'),
	path('work/', views.work, name='work'),
	path('posts/', views.post_home, name='post-home'),
	path('post/<int:pk>/', views.post_detail, name='post-detail'),
	path('category/<int:pk>/', views.post_category, name='post-category'),
	path('contact/', views.contact, name='contact'),
	path('project/', views.project, name='project'),
]