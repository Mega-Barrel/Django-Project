from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("{% url 'home-page' %}")
        else:
            form = UserCreationForm()
    # context = {'form': form}
    return render(request, 'webpages/home-page.html')


def about(request):
    return render(request, 'webpages/about_us.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact_us(request):
    return render(request, 'webpages/contact_us.html')


def login(request):
    return render(request, 'webpages/login.html')


def register(request):
    return render(request, 'webpages/register.html')
