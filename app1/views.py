from django.shortcuts import render, get_object_or_404, redirect
from .models import CompanyInfo, Service, Testimonial, ProductItem
# Create your views here.


# 15th April, 2026. 
"""
AUTHENTICATION PROCESSES
1. Default Django Auth: It uses Django's in-built models and auth flow. It request for username and password
2. Custom Auth -- i.e. You cna alter the Django's default flow, by using email over username... 
"""

from .forms import UserRegistrationForm
from blog.models import AuthourProfile
from django.shortcuts import render, redirect
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            form.save()
            # Associate a user to the authorprofile 
            # AuthourProfile.objects.create(user=user, bio='Update soon')

            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form':form})

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_user(request):
    if request.method == 'POST':
        # AuthenticationForm is built into Django
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Verify the user exists
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'auth/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


def home(requests):
    company_data = CompanyInfo.objects.first()  # Get you the first row in the DB
    # company_data = CompanyInfo.objects.all()[1:].get()  # Get you the second row in the 
    
    # Get all services from the DB
    services =  Service.objects.all()
    testimonials = Testimonial.objects.all()
    portfolioitems = ProductItem.objects.all()

    context = {
        'name':company_data.company_name,
        'address':company_data.company_address,
        'phone':company_data.company_phone,
        'email':company_data.company_email,
        'open_hours':company_data.opening_schedule,
        'x_link':company_data.x_link,
        'linkedin_link':company_data.linkedin_link,
        'facebook_link':company_data.facebook_link,
        'instagram_link':company_data.instagram_link,
        # services 
        'services':services,
        # testimonials
        'testimonials':testimonials,
        # portfolio
        'portfolioitems':portfolioitems,

    }
    return render(requests, 'index.html', context)


# Portfolio Details View - index.html, we will link each portfolio item to this view, and pass the id of the item as a parameter
def portfolio_details(requests, pk):
    portfolio_item = get_object_or_404(ProductItem, id=pk)

    context = {
        'portfolio_item': portfolio_item
    }
    return render(requests, 'portfolio_detail.html', context)


# def portfolio_details(requests, pk):
#     portfolio_item = ProductItem.objects.get(id=pk)

#     context = {
#         'portfolio_item': portfolio_item
#     }
#     return render(requests, 'portfolio_details.html', context)


# def home(requests):
#     company_name = CompanyInfo.objects.first().company_name  # Assuming you want to display the first company info
#     company_address = CompanyInfo.objects.first().company_address
#     company_email = CompanyInfo.objects.first().company_email

#     context = {
#         'name':company_name,
#         'address':company_address,
#         'email':company_email,
#     }
#     return render(requests, 'index.html', context)


# service detail page view
def service_details(requests, s_slug):
    service = get_object_or_404(Service, service_slug=s_slug)

    context = {
        'service': service
    }
    return render(requests, 'service/service_detail.html', context)

