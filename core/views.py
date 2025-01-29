from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request,'core/index.html')


def contact(request):

    return render(request,'core/contact.html')

def aboutpage(request):

    return render(request,'core/about.html')