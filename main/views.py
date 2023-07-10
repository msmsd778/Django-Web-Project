from django.shortcuts import render
from django.http import JsonResponse

from urllib.parse import unquote
from . import models


def index_view(request):
    cats = models.Category.objects.all()
    companies = models.Company.objects.all()[:6]
    items = models.Item.objects.filter(is_offer=True)

    context = {
        'cats': cats,
        'companies': companies,
        'items': items
    }

    return render(request, 'main/index.html', context)


def category_view(request, slug):
    cats = models.Category.objects.all()
    items = models.Item.objects.all()
    slug = unquote(slug)

    if slug != "همه":
        cat = cats.filter(slug=slug)
        if not cat:
            return render(request, 'main/404.html')
        cat = cat[0]
        items = items.filter(cat = cat)
    else:
        cat = "همه"

    
    context = {
        'cats': cats,
        'cat': cat,
        'items': items
    }

    return render(request, 'main/category.html', context)


def product_view(request, slug1, slug2):
    cats = models.Category.objects.all()
    slug1 = unquote(slug1)

    cat = cats.filter(slug=slug1)
    if not cat:
        return render(request, 'main/404.html')
    cat = cat[0]


    slug2 = unquote(slug2)

    product = models.Item.objects.filter(slug=slug2, cat=cat)
    if not product:
        return render(request, 'main/404.html')
    product = product[0]
    product.views += 1
    product.save()

    context = {
        'cats': cats,
        'item': product,
    }

    return render(request, 'main/product.html', context)


def services_view(request):
    cats = models.Category.objects.all()

    context = {
        'cats': cats,
    }
    return render(request, 'main/services.html', context)

def gallery_view(request):
    cats = models.Category.objects.all()
    gallery = models.GalleryImage.objects.all()

    context = {
        'cats': cats,
        'gallery': gallery,
    }
    return render(request, 'main/gallery.html', context)


def contract_view(request):
    cats = models.Category.objects.all()
    company = models.Company.objects.all()

    context = {
        'cats': cats,
        'companies': company,
    }
    return render(request, 'main/contract.html', context)


def about_view(request):
    cats = models.Category.objects.all()

    context = {
        'cats': cats,
    }
    return render(request, 'main/about.html', context)


def contact_view(request):
    cats = models.Category.objects.all()

    context = {
        'cats': cats,
    }

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name)
        print(phone)
        print(message)
        if name and phone and message:
            m = models.UserMessage(name=name, phone=phone, subject=subject, message=message)
            m.save()
            context['message'] = "پیام شما با موفقیت ثبت شد."
        else:
            context['message'] = "اطلاعات وارد شده کامل نمی‌باشد."
        
        return render(request, 'main/success.html', context)


    return render(request, 'main/contact.html', context)

