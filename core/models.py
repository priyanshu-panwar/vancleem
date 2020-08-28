from django.db import models
from PIL import Image
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Experience_Clients(models.Model):
	name = models.CharField(max_length=20, default='')
	logo = models.ImageField(upload_to='logo/')
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Experience_Clients"
		ordering = ['-date', ]

	def __str__(self):
		return self.name


class Work(models.Model):
	title = models.CharField(max_length=100, default='')
	video = models.URLField(null=True, blank=True)
	description = models.TextField()
	client = models.CharField(max_length=100, default='')
	project_link = models.URLField(null=True, blank=True)
	date = models.DateField(null=True, blank=True)
	featured = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Works"
		ordering = ['-date', ]

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.title


class Post(models.Model):
	title = models.CharField(max_length=100, default='')
	image = models.ImageField(upload_to='posts/', null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	content = models.TextField()
	tags = TaggableManager()
	meta_description = models.TextField(default='', null=True, blank=True)
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})

	class Meta:
		verbose_name_plural = "Posts"
		ordering = ['-date_posted', ]


class Code(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, default='')
	description = models.TextField()
	code = models.TextField()

	class Meta:
		verbose_name_plural = "Codes"

	def __str__(self):
		return self.title


class Comment(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Comments"
		ordering = ['-date',]

	def __str__(self):
		return self.email


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	company = models.CharField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=13, null=True, blank=True)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Contacts"
		ordering = ['-date']

	def __str__(self):
		return self.email

