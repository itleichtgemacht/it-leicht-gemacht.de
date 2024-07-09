
from django.utils import timezone


import json
from django.http import HttpRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


from .models import *
# ### AH
# Authentication
# ###
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import EigeneUserCreationForm
from .forms import PostFormular



def home(request):
    # home.html aus dem Template Verzeichnis laden.
    # home.html muss noch erstellt werden
    posts = Post.objects.filter(typ='home').order_by('published_date')
    return render(request, 'home.html', {'posts': posts})

def impressum(request):
    posts = Post.objects.filter(typ='impressum').order_by('published_date')
    return render(request, 'impressum.html', {'posts': posts})

def post_list_categorie(request, filter: str):
    # ### AH
    # order_by('-published_date'): das Minuszeichen sortiert das jüngste zu erst
    # ###
    posts = Post.objects.filter(categorie=filter).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})


def loginSeite(request):
    seite = 'login'
    if request.method == 'POST':
        benutzername = request.POST['benutzername']
        passwort = request.POST['passwort']

        benutzer = authenticate(request, username=benutzername, password=passwort)

        if benutzer is not None:
            login(request, benutzer)
            return redirect('post_list')
        else:
            messages.error(request, "Benutzername oder Passwort nicht korrekt.")

    return render(request, 'login.html', {'seite': seite})

def logoutBenutzer(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

def regBenutzer(request):
    seite = 'reg'
    form = EigeneUserCreationForm

    if request.method == 'POST':
        form = EigeneUserCreationForm(request.POST)
        if form.is_valid():
           benutzer = form.save(commit=False)
           benutzer.save()

           kunde = Staff(name=request.POST['username'],email=request.POST['email'], benutzer=benutzer)
           kunde.save()
           #bestellung = Bestellung(kunde=kunde)
           #bestellung.save()
           username = form.cleaned_data.get('benutzer')
           messages.success(request=f"Neuer Benutzer erstell: {username}")
           login(request, benutzer)
           return redirect('home')
        else:
            messages.error(request, "Fehlerhafte Eingabe! Bitte prüfe deinen Benutzer oder das Passwort!")

    ctx = {'form': form, 'seite': seite}
    return render(request, 'login.html', ctx)

# ############################################################
# Blog
# ###

def post_list(request):
    # ### AH
    # order_by('-published_date'): das Minuszeichen sortiert das jüngste zu erst
    # ###
    posts = Post.objects.filter(typ='blog').order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

@login_required(login_url='login')
def post_create(request: HttpRequest):
    if request.method == "POST":
        if 'Speichern' in request.POST:
            form = PostFormular(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Post wurde erfolgreich aktualisiert.")    
        elif 'Abbruch' in request.POST:
                messages.success(request, "Post wurde NICHT aktualisiert.")    
        return redirect("post_list")
    else:
        form = PostFormular()
    ctx = {"form": form}                     
    return render(request, "post_form.html", ctx)   
    
def post_detail(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    context = {"post": post}
    return render(request, "post_detail.html", context)


@login_required(login_url='login')
def post_update(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostFormular(request.POST, instance=post)
        
        
        if 'Speichern' in request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, "Post wurde erfolgreich aktualisiert.")    
        elif 'Abbruch' in request.POST:
                messages.success(request, "Post wurde NICHT aktualisiert.")    
        return redirect("post_list")
    else:
        form = PostFormular(instance=post)
    context = {"form": form, "post": post}
    return render(request, "post_form.html", context)


@login_required(login_url='login')
def post_delete(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post wurde erfolgreich gelöscht.")
        return redirect("post_list")
    context = {"post": post}
    return render(request, "post_confirm_delete.html", context)

