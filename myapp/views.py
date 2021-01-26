from django.shortcuts import render

from myapp.models import * 

# Create your views here.

def index(request):
    our_blogs = BlogPost.objects.all()[::-1]
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['infos'] = info 
    data['posts'] = our_blogs
    return render(request, 'index.html', data)


def blog(request):
    blog_post = BlogPost.objects.all()[::-1]
    latest_blog = BlogPost.objects.latest('id')
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['infos'] = info
    data['posts'] = blog_post
    data['latestpost'] = latest_blog
    
    return render(request, 'blog.html', data)


def blog_view(request, id):
    blog = BlogPost.objects.get(id=id)
    latest_blogs = BlogPost.objects.all()[::-1]
    info = CompanyInfo.objects.all()
    data = {}
    data['infos'] = info
    data['blog'] = blog
    data['posts'] = latest_blogs
    
    return render(request, 'blog view.html', data)


def aboutus(request):
    about = AboutUs.objects.all()
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['infos'] = info
    data['about'] = about
    return render(request, 'about us.html', data)


def services(request):
    service = Service.objects.all()
    categories = ServiceCategory.objects.all()
    info = CompanyInfo.objects.latest('id')  
    data = {}
    data['infos'] = info
    data['services'] = service
    data['category'] = categories

    return render(request, 'services.html', data)


def career(request):
    career = Career.objects.all()[::-1]
    categories = CareerCategory.objects.all()
    categories_count = CareerCategory.objects.all().count()
    info = CompanyInfo.objects.latest('id')
    
    data = {}

    data['infos'] = info
    data['careers'] = career
    data['categories'] = categories
    data['count'] = categories_count

    return render(request, 'carrer.html', data)


def career_view(request, id):
    career = Career.objects.get(id = id)
    categories = CareerCategory.objects.all()
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['infos'] = info
    data['careers'] = career
    data['categories'] = categories

    return render(request, 'carrer view.html', data)


def contactus(request):
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['infos'] = info
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('textarea')
        contact = ContactUs(name = name, email= email, subject= subject, text= text)
        contact.save()

    return render(request, 'contact us.html', data)
