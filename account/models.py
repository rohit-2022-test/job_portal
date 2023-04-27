from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from master_table.models import (
    Location,
    Industry
)
from PIL import Image

class UserDetail(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    profile_img = models.ImageField(default='default_profile.jpg', upload_to='profile/profile_img/%m', blank=True)
    bg_img = models.ImageField(default='default_bg.jpg', upload_to='profile/profile_img/%m', blank=True)
    resume = models.FileField(upload_to='resume', blank=True)
    date_of_birth = models.DateField(blank=True, null=True, default=timezone.now)
    phone_no = models.CharField(max_length=15, blank=False, null=False)
    address = models.TextField(blank=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)
    zip_code = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True)
    headline = models.CharField(max_length=255, blank=False, null=False)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    class Meta:
        db_table = "user_detail"
        verbose_name_plural = "User Detail"
