from django.contrib import admin
from .models import Country, BlogPost, Rating

admin.site.register(Country)
admin.site.register(BlogPost)
admin.site.register(Rating)