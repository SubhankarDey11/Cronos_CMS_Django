from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.utils import timezone
from .models import Post, Category, Comment
from pages.models import SiteSettings

def get_site_settings():
    """Get site settings or return None"""
    try:
        return SiteSettings.objects.first()
    except:
        return None

class PostListView(ListView):
    """Blog post list view"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return Post.objects.filter(status='published', published_at__lte=timezone.now())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        context['site_settings'] = get_site_settings()
        return context

class PostDetailView(DetailView):
    """Blog post detail view"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(status='published', published_at__lte=timezone.now())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(is_approved=True)
        context['categories'] = Category.objects.filter(is_active=True)
        context['site_settings'] = get_site_settings()
        return context

class CategoryPostListView(ListView):
    """Posts filtered by category"""
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'], is_active=True)
        return Post.objects.filter(
            category=self.category,
            status='published',
            published_at__lte=timezone.now()
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.filter(is_active=True)
        context['site_settings'] = get_site_settings()
        return context

def add_comment(request, post_id):
    """Add comment to a post"""
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id, status='published')
        comment = Comment.objects.create(
            post=post,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            content=request.POST.get('content')
        )
        messages.success(request, 'Your comment has been submitted and is awaiting approval.')
        return redirect('blog:post_detail', slug=post.slug)
