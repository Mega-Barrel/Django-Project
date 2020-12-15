from django.shortcuts import render,HttpResponse
from home.models import Contact, signup

# Create your views here.
def index(request):
    return render(request, 'index.html')

def package(request):
    return render(request, 'package.html')

def about(request):
    return render(request, 'about.html')

def about_get_started(request):
    return render(request, 'package.html')

def contact(request):
    if request.method == 'POST':

        print('This is POST request')
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # print(name, email, subject, message)

        ins = Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
        print('Data Has Been Saved!')
    return render(request, 'contact.html')

def paris(request):
    return render(request, 'paris.html')

def cyprus(request):
    return render(request, 'cyprus.html')

def venice(request):
    return render(request, 'venice.html')

def tokyo(request):
    return render(request, 'tokyo.html')

def los_angeles(request):
    return render(request, 'los_angeles.html')

def prague(request):
    return render(request, 'prague.html')

def register_signin(request):
    if request.method == 'POST':
        name = request.POST['signup_name']
        email = request.POST['signup_email']
        phone = request.POST['signup_phone']
        password = request.POST['signup_password']

        data = signup(name = name, email = email, phone = phone, password = password)
        data.save()
        print('Data Has Been Saved!')

    return render(request, 'Register.html')
