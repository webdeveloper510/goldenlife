from django.db import models
from django.db import models
from adminapp.manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AbstractTimestampedModel(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
      abstract = True
      
      
class User(AbstractBaseUser,PermissionsMixin,AbstractTimestampedModel):
    CHOICES=(
      ("1","admin"),
      ("2","doctor")
    )
    username=models.CharField(max_length=30,blank=True,default="")
    email=models.EmailField(_('email'),unique=True)
    password=models.CharField(max_length=255,default="")
    is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_active 	= models.BooleanField(default=True,
		help_text='Designates whether this user should be treated as active.\
		Unselect this instead of deleting accounts.')
    user_type = models.CharField(default="",max_length=30,choices=CHOICES)
    
    
    USERNAME_FIELD='email'
    
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

