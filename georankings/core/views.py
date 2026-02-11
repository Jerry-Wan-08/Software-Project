from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Country, Rating, BlogPost

def home(request):
    posts = BlogPost.objects.order_by('-created')
    countries = Country.objects.all()
    return render(request, 'home.html', {'posts': posts, 'countries': countries})

@login_required
def rate_country(request):
    countries = Country.objects.all()
    if request.method == 'POST':
        country_id = request.POST['country']
        score = int(request.POST['score'])
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
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
