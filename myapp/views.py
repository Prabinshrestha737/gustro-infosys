from django.shortcuts import render

from myapp.models import * 

# Create your views here.

def index(request):
    return render(request, 'index.html')


def blog(request):
    blog_post = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': blog_post})


def aboutus(request):
    return render(request, 'about us.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    pass

def career(request):
    career = Career.objects.all()
    categories = CareerCategory.objects.all()
    categories_count = CareerCategory.objects.all().count()

    data = {}
    data['careers'] = career
    data['categories'] = categories
    data['count'] = categories_count


    return render(request, 'carrer.html', data)

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('textarea')

        contact = ContactUs(name = name, email= email, subject= subject, text= text)
        contact.save()


    return render(request, 'contact us.html')
