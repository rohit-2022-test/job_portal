from django.db import models
from django.utils import timezone

# Register your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    is_solved = models.BooleanField(default=False)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, default=timezone.now)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "contact"
        verbose_name_plural = "Contact"
