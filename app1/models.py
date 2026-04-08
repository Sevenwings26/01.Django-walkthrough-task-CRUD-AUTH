from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)
    company_address = models.CharField(max_length=200)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=20)
    opening_schedule = models.CharField(max_length=20, blank=True, null=True)
    # social_links 
    x_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    class Meta:
        # verbose_name = "Company Information"
        verbose_name_plural = "Company General Info"

    def __str__(self):
        return f"{self.company_name} - {self.company_email}"

from django.utils.text import slugify

# Service Model 
class Service(models.Model):
    service_icon = models.CharField(max_length=100)
    service_title = models.CharField(max_length=100)
    service_slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)  # for URL routing and SEO purposes, allowing us to create user-friendly URLs based on the service title.
    service_description = models.TextField()
    service_body = models.TextField()
    created_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.service_slug:
            self.service_slug = slugify(self.service_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.service_title
    

# Testimonial Model
class Testimonial(models.Model):
    client_photo = models.ImageField(upload_to='client_photos/', blank=True, null=True)
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_star_rating = models.IntegerField(blank=True, null=True)
    testimonial_text = models.TextField()

    def __str__(self):
        return f"{self.client_name} - {self.client_position}"


# Portfolio/Products

class PortfolioCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name    
    
class PortfolioItem(models.Model):
    # category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='portfolio_items')
    # category = models.ForeignKey('PortfolioCategory', on_delete=models.CASCADE, related_name='portfolio_items')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='portfolio_items/', blank=True, null=True)
    item_description = models.TextField()

    def __str__(self):
        return self.item_title

from ckeditor.fields import RichTextField

# Or 
class ProductItem(models.Model):
    # Select field for product category
    category_choice = [
        ('books', 'Books'),
        ('apps', 'Apps'),
        ('branding', 'Branding'),
        ('products', 'Products'),
    ]
    item_category = models.CharField(max_length=20, choices=category_choice)
    item_title = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='portfolio_items/', blank=True, null=True)
    item_description = models.TextField()
    # item_body = models.TextField(blank=True, null=True)
    item_body = RichTextField(blank=True, null=True)

    # client Info
    item_client = models.CharField(max_length=100, blank=True, null=True)
    item_delivery_date = models.DateField(blank=True, null=True, auto_created=True)
    item_project_url = models.URLField(blank=True, null=True)  # for apps and website jobs...

    def __str__(self):
        return self.item_title


