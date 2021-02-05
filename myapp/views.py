from django.shortcuts import render

from myapp.models import * 

# Create your views here.

def index(request):
    our_blogs = BlogPost.objects.all()[::-1]
    info = CompanyInfo.objects.latest('id')
    about = AboutUs.objects.all()
    data = {}
    data['infos'] = info 
    data['posts'] = our_blogs
    data['about'] = about 
    return render(request, 'index1.html', data)


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
    return render(request, 'aboutus.html', data)


def services(request):
    service = None
    categories = ServiceCategory.objects.all()
    info = CompanyInfo.objects.latest('id')
    category_id = request.GET.get('category')
    print(category_id, "ID")
    if category_id:
        service = Service.get_all_service_by_categoryid(category_id)
    else:
        service = Service.objects.all()
    data = {}
    data['infos'] = info
    data['services'] = service
    data['category'] = categories

    return render(request, 'services.html', data)


def servicedesciption(request, id):
    categories = ServiceCategory.objects.all()
    desc = Service.objects.get(id=id)
    print(desc)
    data  = {}
    data['category'] = categories
    data['desc'] = desc
    return render(request, 'services desc.html', data)


def career(request):
    career = None
    categories = CareerCategory.objects.all()
    categories_count = CareerCategory.objects.all().count()
    info = CompanyInfo.objects.latest('id')

    category_id = request.GET.get('category')
    print(category_id)
    if category_id:
        career = Career.get_all_careers_by_categoryid(category_id)
    else:
        career = Career.objects.all()[::-1]
    # categoryID = request.GET.get('category')
    # print(categoryID)
    
    # if categoryID:
    #     categories = Career.get_all_category_by_id(categoryID)
    # else:
    #     categories = Career.objects.all()
    
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


def portfolio(request):
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['infos'] = info
    return render(request, 'portfolio.html', data)


def ourplan(request):
    plan = OurPlan.objects.all()
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['plan'] = plan 
    data['infos'] = info
    return render(request, 'plan.html', data)


def chooseplan(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        development_type = request.POST.get('developmenttype')
        plan_type = request.POST.get('plantype')
        
        plan = PlanForm(firstname=firstname, lastname=lastname, 
        email=email, phone=phone, 
        development_type=development_type, plan_type=plan_type)
        
        print(plan)

        plan.save()   
    plan = OurPlan.objects.all()
    info = CompanyInfo.objects.latest('id')
    data = {}
    data['info'] = info 
    data['plan'] = plan 
    return render(request, 'planform.html', data)