from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home_page(request):

    number = random.randint(1,10)
    context = {
        'number': number
    }

    return render(request, "leads/home_page.html", context)
