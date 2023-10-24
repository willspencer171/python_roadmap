from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def homepage(request):
    current_user = request.user
    context = {
        "user": current_user
    }

    return render(request, "index.html", context)
