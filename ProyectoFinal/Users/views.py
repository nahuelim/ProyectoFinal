from django.shortcuts import render, redirect
from django.urls.base import reverse

from .models import *
from .forms import *

#para el login:
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
#mixin y decoradores:
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test

#for complex lookups (AND/OR)
from django.db.models import Q

# Create your views here.

#---------------login-------------------------------------------------------

def login_request(request):

      if request.method == "POST":
            form = AuthenticationForm(request=request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')   #este usuario es el que ingresa por teclado la persona, idem la clave de abajo
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)   #este user es el que está en mi BD, si existe seguiria abajo

                  if user is not None:         #si el usario ingresado no es None (quiere decir que existe), listo, pedir que se loguee
                        login(request, user)
                        return render(request,"BlogApp/home.html",  {"mensaje":f"Bienvenido al blog, {usuario}"})   #si es correcto, loguea y me responde welcome
                  else:
                        return render(request,"Users/login.html", {"form":form, "mensaje":"Error, el username es incorrecto. Intentelo nuevamente."})   #y si el usuario que ingresó no corresponde a nadie en la BD, me pasa que es incorrecto

            else:
                        return render(request,"Users/login.html" ,  {"form":form, "mensaje":"Error, la informacion es incorrecta. Intentelo nuevamente."})  #esto se hace si no se cumple la condicion de que el formulario sea valido

      form = AuthenticationForm()    #si no viene por POST, tenemos que mostrar un formulario vacio para que se ingrese
      return render(request,"Users/login.html", {'form':form})

# y despues creamos el Logout directamente en urls.py


#--------------------registrar nuevo usuario----------------------------
#para esto creamos un nuevo form

def register(request):

      if request.method == 'POST':
            form = UserRegisterForm(data=request.POST)
            if form.is_valid():
                  new_user = form.save()
                  login(request, new_user)
                  return redirect(reverse('users:Profile', args=[id]))
            else:
                return render(request, 'Users/register.html', {"form":form, "mensaje": "El user no pudo ser creado. Intentelo nuevamente."})
      
      else:      
            form = UserRegisterForm()     
      return render(request, 'Users/register.html',  {"form":form})


#---------------------editarPerfil---------------------------------------
#para esto creamos un nuevo form

@login_required
def editProfile(request):

      user = request.user
      #buscamos si el usuario tiene avatar:
      try:
          avatar = Avatar.objects.get(user=request.user.id)
          avatar = avatar.avatar.url
      except:
          avatar = ''
     
      if request.method == 'POST':
            myForm = UserEditForm(request.POST, instance=user) 
            if myForm.is_valid():

                  info = myForm.cleaned_data
                  #Datos que se modificarán
                  user.username = info['username']
                  user.email = info['email']
                  user.nombre = info['nombre']
                  user.apellido = info['apellido']
                  user.password1 = info['password1']
                  user.password2 = info['password1']
                  user.save()

                  return redirect(reverse('users:Profile', args=[id]))
            else:
                return render(request, 'Users/edit_profile.html', {"myform":myForm, "mensaje": "El user no pudo ser actualizado. Intentelo nuevamente."})

      else: 
            myForm= UserEditForm(initial={'username':user.username, 'email':user.email, 'nombre':user.nombre, 'apellido':user.apellido}) #Creo el formulario con los datos que voy a modificar
      return render(request, 'Users/edit_profile.html', {"myForm":myForm, "user":user})  #Voy al html que me permite editar


#-----------------------Ver/Editar el perfil de user---------------------------------

@login_required
def profile(request, user_id):
    
    user = request.user
    # buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {'user': user, 'avatar': avatar, 'title': 'Profile'}
    return render(request, 'Users/profile.html', context)


@user_passes_test(lambda u: u.is_superuser)   # solo los superusers pueden cambiar el avatar
def editAvatar(request):
    
    user = request.user
    # buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method == 'POST':
        form_avatar= AvatarForm(request.POST, request.FILES, instance=user)
        if form_avatar.is_valid():
            u = User.objects.get(username=request.user)
            new_avatar = Avatar(user=u, avatar=form_avatar.cleaned_data['avatar'])
            new_avatar.save()
            return redirect(reverse('users:Profile', args=[id]))
        else:
            return render(request, 'Users/edit_avatar.html', {"form_avatar":form_avatar, "mensaje": "El avatar no pudo ser actualizado. Intentelo nuevamente."})
    else:
        form_avatar= AvatarForm()
    return render (request, 'Users/edit_avatar.html', {"form_avatar":form_avatar, "avatar":avatar})


#--------------------------Messages (Inbox and send new msg)--------------------------------------------

@login_required
def messages(request):
    
    user = request.user
    # buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    messages = Messages.objects.filter(Q(receiver=user) | Q(sender=user)).order_by('-sent_at')
    received = messages.filter(receiver=user).order_by('-sent_at')
    sent = messages.filter(sender=user).order_by('-sent_at')

    context = {'title': 'Inbox', 'user': user, 'messages': messages, 'received': received, 'sent':sent, 'avatar': avatar}
    return render(request, 'Users/messages.html', context)


@login_required
def new_message(request):
    
    user = request.user
    # buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        form = MessageForm()
    else:
        # Data submitted > form con datos ingresados por POST
        form = MessageForm(data=request.POST)
        if form.is_valid():

            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect ('blogapp:Messages')
    
    context = {'form': form,'title': 'New message','avatar':avatar}
    return render(request, 'Users/new_msg.html', context)
