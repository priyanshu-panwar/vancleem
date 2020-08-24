from django.shortcuts import render, get_object_or_404
from .models import Experience_Clients, Work, Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

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


def is_valid_queryparam(param):
	return param != '' and param is not None


def post_home(request):
	posts = Post.objects.all()
	posts = posts[::-1]
	recent_posts = posts[:4]

	tag_search = request.GET.get('tag_search')
	common_tags = Post.tags.most_common()[:4]

	if is_valid_queryparam(tag_search):
		posts = posts.filter(tags__slug = tag_search)

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

	if is_valid_queryparam(tag_search):
		posts = posts.filter(tags__slug = tag_search)

	object = get_object_or_404(Post, pk=pk)
	
	categories = Category.objects.all()
	categories = categories[::-1]
	categories = categories[:4]

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
	
	context = {
		'posts' : posts,
	}

	return render(request, 'core/repository.html', context)