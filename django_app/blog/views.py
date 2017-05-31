from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    )
    context = {
        'title' : 'PostList from post_list view',
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, pk):
    context = {
        'post' : Post.objects.get(pk=pk)
    }
    return render(request, 'blog/post_detail.html', context)