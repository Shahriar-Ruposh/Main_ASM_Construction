from django.urls import path,include
from . import views

urlpatterns =[

    path('', views.index, name = 'index'),
    path('/post/<id>/', views.post, name='post'),
    path('/search/', views.search, name='search')
]