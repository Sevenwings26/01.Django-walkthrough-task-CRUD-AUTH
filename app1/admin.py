from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CompanyInfo)
admin.site.site_header = "Company Information Admin"
admin.site.site_title = "Company Information Admin Portal"

admin.site.register(models.Service)
admin.site.register(models.Testimonial)
admin.site.register(models.PortfolioCategory)
admin.site.register(models.PortfolioItem)   
admin.site.register(models.ProductItem) 
  


