from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()


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
    contact_count =Contacts.objects.count()
    user_count = User.objects.count()
    return render(request,'admindashboard.html',{'contact_count':contact_count,'user_count':user_count})
def home(request):
    contact_list = Contacts.objects.filter(user=request.user)
    return render(request,'home.html',{'contact_list':contact_list})
def addcontact(request):
    return render(request,'addcontact.html')

def add_new_contact(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        number = request.POST.get('user_number')

        if name and email and number:
            new_contact = Contacts(user=request.user, name=name, email=email, number=number)
            new_contact.save()
            return redirect('home')
        else:
            error = 'Please fill all the fields.'
            return render(request, 'addcontact.html', {'error': error})
    else:
        return redirect('addcontact')

def delete_contact(request,id):
    delete_contact = Contacts.objects.get(id=id)
    delete_contact.delete()
    if request.user.is_superuser:
        return redirect('contactlist')
    else:
        return redirect('home')

def delete_user(request,id):
    delete_contact = User.objects.get(id=id)
    delete_contact.delete()
    return redirect('userslist')

    

def update_contact(request,id):
    contact = get_object_or_404(Contacts,id=id)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        number = request.POST.get('user_number')
        contact.name = name
        contact.number = number
        contact.save()
        if request.user.is_superuser:
            return redirect('contactlist')
        else:
            return redirect('home')
    return render(request,'updatecontact.html',{'contact':contact})

def update_user(request,id):
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        number = request.POST.get('user_number')
        user.username = name
        user.phonenumber = number
        user.save()
        return redirect('userslist')
        
    return render(request,'updateuser.html',{'user':user})




def contactlist(request):
    contactlist = Contacts.objects.all().values()

    return render(request,'contactlist.html',{'contactlist':contactlist})
def userslist(request):
    users_only = User.objects.filter(is_superuser=False)
    userslist = []
    for user in users_only:
        
        contact = user.contacts.first() if hasattr(user, 'contacts') else None

        userslist.append({
            'user_id':user.id,
            'username':user.username,
            'email':user.email,
            'phone':user.phonenumber if user.phonenumber else None,
            'contact_id':contact.id if contact else 0,  
            'super_user':user.is_superuser, 
        })


    return render(request,'userslist.html',{'userslist':userslist})
def profile(request):
    return render(request,'profile.html')