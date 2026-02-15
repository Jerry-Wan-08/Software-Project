from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Country, Rating, BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-created')
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
        messages.success(request, 'Rating submitted successfully!')
        return redirect('home')
    return render(request, 'rate.html', {'countries': countries})

@login_required
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created')
    return render(request, 'blog_list.html', {'posts': posts})

@login_required
def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            BlogPost.objects.create(
                author=request.user,
                title=title,
                content=content
            )
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_list')
        else:
            messages.error(request, 'Both title and content are required.')
    
    return render(request, 'blog_form.html')

@login_required
def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})

@login_required
def blog_edit(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            post.title = title
            post.content = content
            post.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog_detail', post_id=post.id)
        else:
            messages.error(request, 'Both title and content are required.')
    
    return render(request, 'blog_form.html', {'post': post})

@login_required
def blog_delete(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog_list')
    
    return render(request, 'blog_confirm_delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to GeoRankings!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})