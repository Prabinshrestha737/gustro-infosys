
from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="home"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.aboutus, name="aboutus"),
    path('services', views.services, name="services"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('career', views.career, name="career"),
    path('contact', views.contactus, name="contact")
]