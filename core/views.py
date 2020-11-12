from django.shortcuts import render, get_object_or_404
from .models import Experience_Clients, Work, Post, Category, Comment, Contact, Service
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from vancleem.settings import EMAIL_HOST_USER, ADMIN_MAIL_1, ADMIN_MAIL_2


def service_details(request, pk):
	object = get_object_or_404(Service, pk=pk)
	services = Service.objects.all()
	context = {
		'service' : object,
		'services' : services,
	}
	return render(request, 'core/service_detail.html', context)

def service(request):
	services = Service.objects.all()
	context = {
		'services' : services,
	}
	return render(request, 'core/services.html', context)


def project(request):
	pass

def home(request):
	works = Work.objects.all()
	works = works[::-1]
	works = works[:3]
	context = {
		'works' : works,
	}
	return render(request, 'core/index.html', context)


def experience(request):
	logos = Experience_Clients.objects.all()
	context = {
		'logos' : logos,
	}
	return render(request, 'core/experience.html', context)


def solutions(request):
	return render(request, 'core/solutions.html')


def work(request):
	works = Work.objects.all()
	works = works[::-1]

	page = request.GET.get('page', 1)
	paginator = Paginator(works, 6)

	try:
		works = paginator.page(page)
	except PageNotAnInteger:
		works = paginator.page(1)
	except EmptyPage:
		works = paginator.page(paginator.num_pages)

	context = {
		'works' : works,
	}
	return render(request, 'core/projects.html', context)

def work_detail(request, pk):
	object = get_object_or_404(Work, pk=pk)
	context = {
		'work' : object,
	}
	return render(request, 'core/project_detail.html', context)


def is_valid_queryparam(param):
	return param != '' and param is not None


def post_home(request):
	posts = Post.objects.all()
	posts = posts[::-1]
	recent_posts = posts[:4]
	tag_search = request.GET.get('tag_search')
	common_tags = Post.tags.most_common()[:4]

	if is_valid_queryparam(tag_search):
		posts = Post.objects.filter(tags__slug = tag_search)

	categories = Category.objects.all()
	categories = categories[::-1]
	categories = categories[:4]

	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 6)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {
		'posts' : posts,
    	'cnt' : len(posts),
		'recent_posts' : recent_posts,
		'common_tags' : common_tags,
		'categories' : categories,
	}
	return render(request, 'core/repository.html', context)


def post_detail(request, pk):
	posts = Post.objects.all()
	posts = posts[::-1]
	recent_posts = posts[:4]

	tag_search = request.GET.get('tag_search')
	common_tags = Post.tags.most_common()[:4]
	print(tag_search)

	if is_valid_queryparam(tag_search):
		posts = Post.objects.filter(tags__slug = tag_search)

	object = get_object_or_404(Post, pk=pk)
	
	categories = Category.objects.all()
	categories = categories[::-1]
	categories = categories[:4]

	name = request.GET.get('Name')
	email = request.GET.get('Email')
	mess = request.GET.get('message')
	print("NAME = ", name)
	print("EMAIL = ", email)
	print("MESSAGE = ", mess)

	if is_valid_queryparam(name) and is_valid_queryparam(email) and is_valid_queryparam(mess):
		c = Comment(name=name, email=email, message=mess)
		c.save()
		#email
		send_mail(
			'Thank you for contacting - vanCleem.com',
			'Test Message',
			EMAIL_HOST_USER,
			[email, ],
			fail_silently=True,
		)
		send_mail(
			'Thank you for contacting - vanCleem.com',
			'Test Message',
			EMAIL_HOST_USER,
			[ADMIN_MAIL_1, ],
			fail_silently=True,
		)
		send_mail(
			'Thank you for contacting - vanCleem.com',
			'Test Message',
			EMAIL_HOST_USER,
			[ADMIN_MAIL_2, ],
			fail_silently=True,
		)
		return render(request, 'core/thankyou.html')

	context = {
		'post' : object,
		'recent_posts' : recent_posts,
		'common_tags' : common_tags,
		'categories' : categories,
	}
	return render(request, 'core/repository-details.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'core/repository.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


def post_category(request, pk):
	posts = Post.objects.filter(category__id=pk)
	posts = posts[::-1]

	fun = Post.objects.all()
	fun = fun[::-1]
	recent_posts = fun[:4]

	tag_search = request.GET.get('tag_search')
	common_tags = Post.tags.most_common()[:4]

	if is_valid_queryparam(tag_search):
		posts = posts.filter(tags__slug = tag_search)

	categories = Category.objects.all()
	categories = categories[::-1]
	categories = categories[:4]

	context = {
		'posts' : posts,
		'recent_posts' : recent_posts,
		'common_tags' : common_tags,
		'categories' : categories,
	}

	return render(request, 'core/repository.html', context)


def contact(request):
	name = request.GET.get('contact-name')
	email = request.GET.get('contact-email')
	company = request.GET.get('contact-company')
	phone = request.GET.get('contact-phone')
	message = request.GET.get('contact-message')

	if is_valid_queryparam(name) and is_valid_queryparam(email) and is_valid_queryparam(message):
		c = Contact(name=name, email=email, company=company, phone=phone, message=message)
		#email
		send_mail(
			'Thank you for contacting - vanCleem.com',
			'Test Message',
			EMAIL_HOST_USER,
			[email, ],
			fail_silently=True,
		)
		send_mail(
			'Thank you for contacting - vanCleem.com',
			'Test Message',
			EMAIL_HOST_USER,
			[ADMIN_MAIL_1, ],
			fail_silently=True,
		)
		send_mail(
			'Thank you for contacting - vanCleem.com',
			'Test Message',
			EMAIL_HOST_USER,
			[ADMIN_MAIL_2, ],
			fail_silently=True,
		)
		c.save()
		return render(request, 'core/thankyou.html')

	return render(request, 'core/contact.html')