from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import Lead

# Create your views here.
def home_page(request):

    number = random.randint(1, 10)

    context = {
        "number": number,
    }

    return render(request, "leads/home_page.html", context)


def leads_list(request):

    leads_list = Lead.objects.all()

    context = {"leads_list": leads_list}

    return render(request, "leads/leads_list.html", context)
