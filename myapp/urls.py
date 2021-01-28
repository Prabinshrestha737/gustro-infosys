
from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="home"),
    path('blog/', views.blog, name="blog"),
    path('blogview/<int:id>', views.blog_view, name="blogview"),
    path('about/', views.aboutus, name="aboutus"),
    path('services', views.services, name="services"),
    path('servicedesciption/', views.servicedesciption, name="servicedesciption"),
    path('career', views.career, name="career"),
    path('careerview/<int:id>', views.career_view, name="careerview"),
    path('contact/', views.contactus, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('ourplan/', views.ourplan, name="ourplan"),
    path('chooseplan/', views.chooseplan, name="chooseplan")
    
]