from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        #ENVIANDO DATOS
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        #RECIVIENDO DATOS
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado correctamente')	
            except:
                return HttpResponse('El usuario ya existe')
        else:
            return HttpResponse('Las contraseñas no coinciden')
    