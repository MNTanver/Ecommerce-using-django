from .models import Category

#we use this context processor for category link and we have to write it in settings
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)