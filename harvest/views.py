from django.shortcuts import render

from .models import CoffeeOriginCountry


def index(request):
    all_countries = CoffeeOriginCountry.objects.all()
    context = {'all_countries': all_countries}
    return render(request, 'harvest/index.html', context)
