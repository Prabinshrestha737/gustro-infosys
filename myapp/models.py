from django.db import models
import datetime

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    Description = models.TextField()
    image = models.ImageField(upload_to=None, blank=True)
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
    


