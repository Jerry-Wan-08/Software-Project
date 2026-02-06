from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Country

def all_countries(request):
    countries = Country.objects.all().values()
    context = {
        'countries': countries,
    }
    return render(request, 'Countries/All_Countries.html', context)

def country_detail(request, id):
    country = get_object_or_404(Country, id=id)
    return render(request, 'Countries/Country_Detail.html', {'country': country})