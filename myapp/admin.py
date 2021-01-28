from django.contrib import admin

from myapp.models import * 

# Register your models here.

admin.site.register(BlogPost)

admin.site.register(ContactUs)

admin.site.register(CareerCategory)
admin.site.register(Career)

admin.site.register(ServiceCategory)
admin.site.register(Service)

admin.site.register(CompanyInfo)
admin.site.register(AboutUs)

admin.site.register(OurPlan)

admin.site.register(PlanForm)


