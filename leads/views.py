from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import Lead

# Create your views here.
def home_page(request):

    number = random.randint(1,10)
    leads_list = Lead.objects.all()

    context = {
        'number': number,
        'leads_list': leads_list
    }

    return render(request, "leads/home_page.html", context)
