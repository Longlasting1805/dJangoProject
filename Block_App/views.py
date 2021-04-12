from django.shortcuts import render

# create your views here.
from django.template.context_processors import request
# from django.views.generic import listView


def block(requests):
    return render(requests, "index.html")
