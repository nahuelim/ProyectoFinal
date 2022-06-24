from django.shortcuts import render, redirect
#para el CRUD:
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
#importamos forms.py:
from BlogApp.forms import *
#mixin y decoradores:
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-fecha') [0:3]
    return render (request, 'BlogApp/home.html', {'posts': posts})

#---------creacion del CRUD mediante CBV (Clases basadas en vistas)------------------

class PostList(ListView):
    model = Post
    template_name = 'BlogApp/posts.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'BlogApp/post_detail.html'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'


#-------------------view Posts--------------------------------------------------
def posts(request):

    posts = Post.objects.all().order_by('-fecha')
    return render(request, "BlogApp/posts.html", {"posts":posts})

#------------nueva funcion para mi form que permite agregar Posts-------------------

@login_required
def postForm(request):

    if request.method == 'POST':
        myForm = PostForm(request.POST, request.FILES)
        print(myForm)

        if myForm.is_valid():
            info = myForm.cleaned_data
            post = Post(maquinaria=info['maquinaria'], marca=info['marca'], usuario=info['usuario'],imagen=info['imagen'], detalle=info['detalle'])
            post.save()
            return redirect('blogapp:Posts')
    else:
        myForm = PostForm()
    return render(request, 'BlogApp/post_form.html', {"myForm":myForm})

#---------------------------Edit post---------------------------------------

@login_required
def editPost(request, post_id):

    #recibe el id del post que vamos a modificar
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogapp:Posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'BlogApp/edit_post.html',{'form':form, 'maquinaria':post.maquinaria})


#-------------------searchPosts-------------------------------------------

def searchPost(request):

    return render(request, 'BlogApp/searchPost.html')

def searchResult(request):


    if request.GET["maquinaria"]:
        maquinaria = request.GET["maquinaria"]
        post = Post.objects.filter(maquinaria__icontains=maquinaria).order_by("-fecha")
        return render(request, 'BlogApp/searchPost.html', {"post":post})
    else:
        response="No ingreso ninguna informacion."
    return render(request, 'BlogApp/posts.html', {"response":response})


#-------------------------about us-------------------------------------------

def about(request):

    return render(request, "BlogApp/about.html")
