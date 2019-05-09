from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from .forms import CreateForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class PostListView(ListView):
	model=Post
	template_name='blog/index.html'
	context_object_name='posts'
	extra_context={
		'title':'Home'
	}
	ordering=['-date_posted']
	paginate_by=2

class UserPostListView(ListView):
	model=Post
	template_name='blog/user_posts.html'
	context_object_name='posts'
	paginate_by=2

	def get_queryset(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model=Post
	template_name='blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	form_class=CreateForm
	extra_context={
		'title':'Create'
	}
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	# fields=['title','content']
	form_class=CreateForm
	extra_context={
		'title':'update'
	}
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url='/'
	extra_context={
		'title':'Delete'
	}
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False



def about(request):
	context={
		'title':'About'
	}
	return render(request,'blog/about.html',context)
 