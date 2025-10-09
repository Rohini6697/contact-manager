from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout

from contacts.models import Contacts

from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admindashboard')
            return redirect('home')
        return render(request,'login.html',{'error':'invalid username or password'})
    return render(request,'login.html')


def dashboard(request):
    return render(request,'admindashboard.html')
def home(request):
    contact_list = Contacts.objects.all().values()
    return render(request,'home.html',{'contact_list':contact_list})
def addcontact(request):
    return render(request,'addcontact.html')
def add_new_contact(request):
    name = request.POST['user_name']
    number = request.POST['user_number']
    new_contact = Contacts(name=name,number=number)
    if name and number: 
        new_contact.save()
        return redirect('home')
    else:
        error='please fill all th field'
        return redirect('add_new_contact' ,{'error':error})
def delete_contact(request,id):
    delete_contact = Contacts.objects.get(id=id)
    delete_contact.delete()
    return redirect('home')

def update_contact(request,id):
    contact = get_object_or_404(Contacts,id=id)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        number = request.POST.get('user_number')
        contact.name = name
        contact.number = number
        contact.save()
        return redirect('home')
    # return render(request,'home.html',{'contact':contact})
    return render(request,'updatecontact.html',{'contact':contact})