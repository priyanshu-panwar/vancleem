from django.contrib import admin
from .models import Experience_Clients, Work, Post, Category, Comment

admin.site.register(Experience_Clients)
admin.site.register(Category)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
	list_display = ['title', 'client', 'date', 'featured']
	list_filter = ['date', ]
	search_fields = ('title', 'client', 'featured')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'date_posted']
	list_filter = ['date_posted', ]
	search_fields = ('title', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'date']
	list_filter = ['date', ]

