from django.http import HttpResponse


def home(request, *args, **kwargs):
    
    return HttpResponse("<p>Hello world</p>")