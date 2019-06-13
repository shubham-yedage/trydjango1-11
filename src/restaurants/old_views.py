from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#  Functioned bases view
def home(request):
    html_ = """<!DOCTYPE html>
    <html lang=en>
    
    <head>
    </head>
    <body>
    <h1>Hello world!<h1>
    <p>Django App</p>
    </body>
    </html>
    """
    # return render(request, "home.html", {})
    # return HttpResponse("hello world")
    return HttpResponse(html_)


def index(request):
    import random
    rand_val = random.randint(0, 100000)
    nums = [rand_val, random.randint(0, 100000), random.randint(0, 100000)]
    ctx = {"context_var": "With you always!", "bool_val": True, "num": rand_val, "nums": nums}
    return render(request, "index.html", context=ctx)


def about(request):
    ctx = {}
    return render(request, "about.html", context=ctx)


def contact(request):
    ctx = {}
    return render(request, "contact.html", context=ctx)
