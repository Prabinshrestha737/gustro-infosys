from django.db import models
import datetime

from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    image = models.ImageField(upload_to='uploads/images/', blank=True)
    date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.email


class CareerCategory(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category


class Career(models.Model):
    category = models.ForeignKey(CareerCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    deadline = models.DateField()
    education = models.CharField(max_length=450)
    experience = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class CompanyInfo(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50, default="Sallaghari")
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    google = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class AboutUs(models.Model):
    description = models.TextField()