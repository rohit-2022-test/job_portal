from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from master_table.models import Location
from softdelete.models import SoftDeleteModel

# Create your models here.
class Company(SoftDeleteModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    logo = models.ImageField(default='default_company_logo.jpg', upload_to='comapany/comapany_logo/%m', blank=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True)
    company_owner = models.CharField(max_length=255, blank=False, null=False)
    website_link = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone_no = models.CharField(max_length=14, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)
    zipcode = models.IntegerField()
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = "company"
        verbose_name_plural = "Comapanies"

class Comapany_images(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    image = models.ImageField(default='default_company_image.jpg', upload_to='comapany/comapany_image/%m', blank=True)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return f'{self.company_id.name}'
    
    class Meta:
        db_table = "company_image"
        verbose_name_plural = "Comapany Images"

