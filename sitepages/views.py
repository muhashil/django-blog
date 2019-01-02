from django.shortcuts import render

def about(request):
    return render(request, 'sitepages/about.html', {})

def contact(request):
    return render(request, 'sitepages/contact.html', {})