from django.shortcuts import render, get_object_or_404,redirect,reverse
from .models import Post, PostView, Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Count, Q
from .forms import CommentForm
from mainapp.models import MainLogo
def get_category_count():
    qs = Post.objects.values('categories__name').annotate(Count('categories'))
    return qs


def index(request):
    mainlogo = MainLogo.objects.all()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    catagory_count = get_category_count()
    article_list= Post.objects.all()
    article_list = article_list.order_by('-timestamp')
    paginator = Paginator(article_list,3)
    page_req = 'page'
    page = request.GET.get(page_req)
    try:
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    contex ={
        'queryset': paginated_queryset,
        'page_req': page_req,
        'most_recent': most_recent,
        'catagory_count' : catagory_count,
        'mainlogo': mainlogo,
    }

    return render(request, 'blog-one-column.html', contex)


def post(request,id):

    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id=id)
    catagory_count = get_category_count()
    if request.user.is_authenticated:

        PostView.objects.get_or_create(user=request.user,post=post)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post", kwargs={
                'id': post.pk
            }))

    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': catagory_count,
        'form': form
    }
    return render(request, 'blog-details.html', context)


def search(request):
    qs = Post.objects.all()
    query = request.GET.get('q')
    if query:
        qs = qs.filter(
            Q(title__icontains=query)|
            Q(overview__icontains=query)
        ).distinct()

    contex = {
        'qs':qs
    }

    return render(request,'search.html',contex)