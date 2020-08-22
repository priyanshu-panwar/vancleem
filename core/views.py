from django.shortcuts import render, get_object_or_404
from .models import Experience_Clients, Work, Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	return render(request, 'core/index.html')


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
	return render(request, 'core/work.html', context)


def post_home(request):
	posts = Post.objects.all()
	#posts = [::-1]
	
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
	}
	return render(request, 'core/repository.html', context)


def post_detail(request, pk):
	object = get_object_or_404(Post, pk=pk)
	context = {
		'post' : object,
	}
	return render(request, 'core/repository-details.html', context)


