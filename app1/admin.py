from django.contrib import admin
from .models import CompanyInfo, Service, Testimonial

# Register your models here.
admin.site.register(CompanyInfo)
admin.site.site_header = "Company Information Admin"
admin.site.site_title = "Company Information Admin Portal"

admin.site.register(Service)
admin.site.register(Testimonial)


