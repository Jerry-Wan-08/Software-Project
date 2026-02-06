from django.http import HttpResponse
from django.template import loader
from .models import Country

def all_countries(request):
    countries = Country.objects.all().values()
    template = loader.get_template('Countries/All_Countries.html')
    context = {
        'countries': countries,
    }
    return HttpResponse(template.render(context, request))

