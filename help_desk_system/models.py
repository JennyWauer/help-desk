from django.db import models
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    admin_level = models.IntegerField(validators=[validate_max, validate_min], default=1)
    role = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()