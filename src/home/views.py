import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (100 * page_qs.count()) / qs.count()
    except:
        percent = 0

    my_title = "My Page"
    my_context = {
        "title": my_title,
        "page_count": page_qs.count(),
        "total_count": qs.count(),
        "percent": (100 * page_qs.count()) / qs.count()
    }
    print("  path :  ", request.path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
