from django.shortcuts import render, get_object_or_404
from . models import MainLogo, Services, Project, ProjectGallery, About,Category,Qualities,ServicesGallery,Profile,Brands
from blog.models import Post
# Create your views here.



def brands(request):
    mainlogo = MainLogo.objects.all()
    contex= {
        'mainlogo': mainlogo,
    }
    return render(request,'main_logo',contex)

def home(request):
    mainlogo = MainLogo.objects.all()
    qualities = Qualities.objects.all()
    services = Services.objects.order_by('-id')[:3]
    project = Project.objects.order_by('-project_timestamp')[:5]
    latest_blog = Post.objects.order_by('-timestamp')[0:3]
    profile= Profile.objects.all()
    blog = Post.objects.order_by('-timestamp')[0:3]
    brand = Brands.objects.all()

    contex = {
        'mainlogo' : mainlogo,
        'qualities': qualities,
        'services': services,
        'project': project,
        'latest_blog': latest_blog,
        'profile': profile,
        'blogs': blog,
        'brand': brand
    }
    return render(request,'home.html', contex)


def about (request):
    mainlogo = MainLogo.objects.all()
    about = About.objects.all()
    qualities = Qualities.objects.all()
    profile = Profile.objects.all()
    brand = Brands.objects.all()
    contex = {
        'mainlogo': mainlogo,
        'about': about,
        'qualities': qualities,
        'profile' : profile,
        'brand': brand
    }
    return render(request,'about.html',contex)


def services(request):
    mainlogo = MainLogo.objects.all()
    qualities = Qualities.objects.all()
    brand = Brands.objects.all()
    services = Services.objects.order_by('id')
    contex = {
        'mainlogo': mainlogo,
        'qualities': qualities,
        'services': services,
        'brand': brand

    }

    return render(request, 'service.html', contex)

def services_details(request,pk):
    mainlogo = MainLogo.objects.all()
    qs = Services.objects.order_by('service_title')
    obj = Services.objects.filter(pk=pk)
    brand = Brands.objects.all()

    contex = {
        'mainlogo': mainlogo,
        'services': qs,
        'single_services' : obj,
        'brand': brand
    }

    return render(request,'single-service.html',contex)


def projects(request,id=None):
    categories = None
    projects = None
    mainlogo = MainLogo.objects.all()
    category = Category.objects.all()

    if id != None:
        categories = get_object_or_404(Category, id=id)
        projects = Project.objects.filter(project_category=categories)

    else:
        projects = Project.objects.all().order_by('project_title')

    contex = {
        'mainlogo': mainlogo,
        'projects': projects,
        'category' : category

    }
    return render(request,'projects-three.html', contex)

def project_details(request,id,pk):
    single_project = Project.objects.get(id=id, pk = pk )

    contex = {
        'single_projects' : single_project
    }
    return render(request,'single-project.html', contex)



def contact(request):
    pass