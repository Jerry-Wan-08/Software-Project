from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from urllib3 import request
from .models import Country, Rating, BlogPost
from django.contrib.auth.forms import UserCreationForm




def home(request):
  posts = BlogPost.objects.order_by('-created')
  return render(request, 'home.html', {'posts': posts})


@login_required
def rate_country(request):
  countries = Country.objects.all()
  if request.method == 'POST':
    country_id = request.POST['country']
    score = request.POST['score']
    Rating.objects.update_or_create(
      user=request.user,
      country_id=country_id,
      defaults={'score': score}

)
    return redirect('home')
  return render(request, 'rate.html', {'countries': countries})


def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('login')
  else:
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})