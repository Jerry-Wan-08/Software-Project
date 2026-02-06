from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Country

def all_countries(request):
    countries = Country.objects.all().values()
    template = loader.get_template('Countries/All_Countries.html')
    context = {
        'countries': countries,
    }
    return HttpResponse(template.render(context, request))

def country_detail(request, id):
    country = get_object_or_404(Country, id=id)
    return render(request, 'Countries/Country_Detail.html', {'country': country})