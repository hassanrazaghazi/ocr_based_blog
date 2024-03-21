from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Registeration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def check_username(self):
        if Registeration.objects.filter(username=self.username).exists():
            raise ValidationError("Username already exists")
        return

    def check_email(self):
        if Registeration.objects.filter(email=self.email).exists():
            raise ValidationError("Email already exists")
        return

    def password_match(self):
        if self.password == self.password2:
            return "Password Match"
        else:
            return "Password Doesn't Match. Please enter password again."
    
    def __str__(self):
        return self.username