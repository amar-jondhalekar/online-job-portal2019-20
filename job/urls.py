"""unicareer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index,name='home'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register,name='register'),
    path('login/forgot-password', views.frpass, name='frpass'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('post_job/', views.post_job,name='post_job'),
    path('login/register', views.register, name='register'),
    path('login/login', views.login, name='login'),
    path('browse_job', views.browse_job, name='browse_job'),
    path('add-resume', views.add_resume, name='add_resume'),
    path('job-details', views.job_details, name='job-details'),
    path('job-details/<int:id>', views.job_details, name='job-details_id'),
    path('search', views.search_job, name='search_job'),
    path('faq', views.faq,name='faq'),
    path('blog', views.blog, name='blog'),
    path('job-details/home', views.jobindex, name='jobhome'),
    path('about/home', views.reindex,name='redirecthome'),
    path('contact/home', views.reindex,name='redirecthome'),
    path('post_job/home', views.reindex,name='redirecthome'),
]
