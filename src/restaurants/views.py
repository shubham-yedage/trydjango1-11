import random
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation

# Create your views
# Function based views
# def home(request):
#     html_var = "f string"
#     html_ = f"""
#     <!DOCTYPE html>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>Hello World!<h1>
#     <p>The {html_var} is coming through</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_ )
# return render(request, "home.html", {})
# return HttpResponse("Hello World!")

"""
 Function based views
"""


def home(request):
    no = random.randint(0, 100000)
    some_list = [no, random.randint(0, 100000), random.randint(0, 100000)]
    context = {"html_var": "Context Variable", "bool_item": False, "no": no, "some_list": some_list}
    return render(request, "home.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context=context)


def about(request):
    context = {}
    return render(request, "about.html", context=context)

def restaurant_list_View(request):
    template = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request=request, template_name=template, context=context)


"""
Class based simple view.
"""


class ContactView(View):
    def get(self, request, **args):
        context = {
        }
        return render(request, "contact.html", context)

    # def post(self, request, **args):
    #     context = {
    #     }
    #     return render(request, "contact.html", context)
    #
    # def put(self, request, **args):
    #     context = {
    #     }
    #     return render(request, "contact.html", context)


"""
Template based Template View
"""


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        no = random.randint(0, 100000)
        some_list = [no, random.randint(0, 100000), random.randint(0, 100000)]
        context = {"html_var": "Context Variable", "bool_item": False, "no": no, "some_list": some_list}
        return context

class AboutTemplateView(TemplateView):
    template_name = "about.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"

"""
List view
"""
class RestaurantListView(ListView):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            return RestaurantLocation.objects.filter(
                Q(category__iexact = slug) | Q(category__icontains = slug)
            )
        return RestaurantLocation.objects.all()
