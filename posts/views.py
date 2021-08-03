from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Author
from marketing.models import Signup
from django.db.models import Count, Q

from django.views.generic import DetailView, ListView, TemplateView
import datetime








def list_by_category(request, pk):
    category_list = Category.objects.all()
    
    
    categories = get_object_or_404(Category, id=pk)
    posts = Post.objects.filter(categories=categories)
    template = 'category.html'

    category_count = get_category_count()

   

    context = {
        'category_list': category_list,
        'posts': posts,
        'categories': categories,
        
        'category_count': category_count
        

    }

    return render(request, template, context)


def search(request):
    category_list = Category.objects.all()
    queryset = Post.objects.all()
    query = request.GET.get('q')
    lats = query
    category_count = get_category_count()
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(categories__title__icontains=query)
        ).distinct()
    context = {
        'lats': lats,
        'search_set': queryset,
        'category_count': category_count,
        'category_list': category_list,
        
    }
    return render(request, 'search_results.html', context)


def get_category_count():
    category_count = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))

    
    return category_count




def index(request):
    category_list = Category.objects.all()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp') [0:6]
    category_count = get_category_count()
    


    if request.method == "post":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    context = {
        'object_list': featured,
        'latest' : latest,
        'category_count': category_count,
        'category_list': category_list,
        
    }
    return render(request, 'index.html', context )




    

def author(request, pk):
    category_list = Category.objects.all()
    author = get_object_or_404(Author, id=pk)
    posts = Post.objects.filter(author=author)
    context = {
        'posts': posts,
        'author': author,
        'category_list': category_list,
    }
    return render(request, 'author.html', context)


def blog(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_req_var = 'page'
    page = request.GET.get(page_req_var)
    category_count = get_category_count()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_req_var,
        'category_count': category_count,
        'category_list': category_list,
    }
    return render(request, 'blog.html', context)


def post(request, pk):
    category_list = Category.objects.all()
    category_count = get_category_count()
    
    post = get_object_or_404(Post, id=pk)

    post.views = post.views + 1
    post.save()

    

   

   
    context = {
        'post': post,
        
        'category_count': category_count,
        'category_list': category_list,
        
    }
    return render(request, 'post.html', context)








    
