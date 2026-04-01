from django.shortcuts import render
from .models import CompanyInfo, Service, Testimonial, ProductItem
# Create your views here.


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
