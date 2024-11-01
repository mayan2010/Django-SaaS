import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent


def home(request, *args, **kwargs):

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
