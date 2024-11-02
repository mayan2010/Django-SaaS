import pathlib
from django.http import HttpResponse
from django.shortcuts import render
 
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home(request, *args, **kwargs):

    my_title = "Django"
    my_context=  {
        "title": my_title
    }
    html_ = ""
    html_template  = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)

def old_home(request, *args, **kwargs):

    my_title = ""
    my_context=  {
        "title": my_title
    }
    html_ = """
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>{title} anything??</h1>
</body>
</html>
    """.format(**my_context)

    return HttpResponse(html_)
