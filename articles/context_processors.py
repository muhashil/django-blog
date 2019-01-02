from .models import Category

def menu_link(request):
    categories = Category.objects.all()
    return dict(categories=categories)