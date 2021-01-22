from django.contrib import admin

from myapp.models import BlogPost, ContactUs, CareerCategory, Career, ServiceCategory, Service 

# Register your models here.

admin.site.register(BlogPost)

admin.site.register(ContactUs)

admin.site.register(CareerCategory)
admin.site.register(Career)

admin.site.register(ServiceCategory)
admin.site.register(Service)


