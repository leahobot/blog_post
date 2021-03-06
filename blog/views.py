from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    object_list = Post.objects.filter(status="published")
    paginator = Paginator(object_list, 2)

    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    data = {
        'page': page,
        "posts": posts,

    }

    return render(request, 'blog/post/list.html', data)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=slug)

    data = {

        "post": post,

    }

    return render(request, 'blog/post/detail.html', data)
