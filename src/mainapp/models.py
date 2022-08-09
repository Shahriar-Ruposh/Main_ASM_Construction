from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField



User = get_user_model()

# Create your models here.
class MainLogo(models.Model):

    logo = models.CharField(max_length=50)
    main_logo = models.ImageField()
    service_logo= models.ImageField()

    def __str__(self):
        return self.logo


class Qualities(models.Model):
    quality_title = models.CharField(max_length=255)
    quality_logo = models.ImageField()
    quality_content = models.CharField(max_length=255)

class Services(models.Model):

    service_title = models.CharField(max_length=1000)
    service_content = models.TextField()
    service_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.service_title

    def get_absolute_url(self):
        return reverse('services', kwargs={
            'id':self.id
        })

class ServicesGallery(models.Model):
    serv = models.ForeignKey(Services, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="services/images/")

    def __str__(self):
        return self.proj.project_title

class Category(models.Model):

    category_title = models.CharField(max_length=255)

    def __str__(self):
        return self.category_title

class Project(models.Model):

    project_title = models.CharField(max_length=1000)
    project_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_content = models.TextField()
    project_clint = models.CharField(max_length=300)
    project_location = models.CharField(max_length=255)
    project_budget = models.CharField(max_length=255)
    project_surfce_area = models.CharField(max_length=255)
    project_image = models.ImageField()
    project_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title

class ProjectGallery(models.Model):
    proj = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.proj.project_title


class Profile(models.Model):

    pro_name = models.CharField(max_length=255, default="H")
    pro_pic = models.ImageField()
    full_name = models.CharField(max_length=500)
    deg = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.pro_name


class About(models.Model):

    about_title = models.CharField(max_length=500)
    about_content = models.TextField()

class Brands(models.Model):
    brand_name = models.CharField(max_length=255)
    brand_image = models.ImageField()

    def __str__(self):
        return self.brand_name






















"""
1.Main Logo:
  1. Logo Image
  2. Description
  
2.Services:
  1.title
  2.service Content
  3.image
  4.mini logo
  
3.Project:
  1.title
  2.project Catagory
  3.project content
  4.Image galary
  5.clint
  6.location
  7.budget
  8.surfce area

4.Blog:
  1.title
  2.blog content
  3.Create time
  4.comment count
  5.view count
  6.author
  7.Thubnail
  8.category
  9.previous_post
  10.next-post
  
5.About Team:
  1.profile Pic
  2.Full name
  3.degnation
"""