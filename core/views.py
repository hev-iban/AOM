from django.shortcuts import render

from item.models import Category,Item

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def privacy(request):
    return render(request,'core/privacy.html')

def term_use(request):
    return render(request, 'core/term_use.html')

def about(requesst):
    return render(requesst, 'core/about.html')
