from django.contrib import admin
from .models import Experience_Clients, Service, Work, Post, Category, Comment, Contact, Code

admin.site.register(Experience_Clients)
admin.site.register(Category)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title', 'subtitle']

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
	list_display = ['title', 'client', 'date', 'featured']
	list_filter = ['date', ]
	search_fields = ('title', 'client', 'featured')

class CodeInline(admin.TabularInline):
	model = Code
	extra = 3

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'date_posted']
	list_filter = ['date_posted', ]
	search_fields = ('title', 'author')
	inlines = [CodeInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'date']
	list_filter = ['date', ]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'date', 'company']
	list_filter = ['date', ]
	search_fields = ('email', 'company', 'name')

