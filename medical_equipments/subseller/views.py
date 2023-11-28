from django.shortcuts import render
from subseller.models import *


def subseller_home(request):
    return render(request, 'subseller/subseller_home.html')
