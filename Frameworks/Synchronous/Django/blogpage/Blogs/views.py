from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def homepage(request):
    template = loader.get_template("index.html")
    current_user = request.user
    context = {
        "user": current_user
    }

    return HttpResponse(template.render(context, request))
