from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.home,name= 'index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('services/<pk>', views.services_details, name='services_details'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.projects, name='projects'),
     path('projects/<int:id>/<pk>', views.project_details, name='projects_details'),
    path('contact', views.contact, name='contact'),
    path('blog', include('blog.urls'), name='blog'),


]