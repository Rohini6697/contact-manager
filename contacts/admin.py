from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Contacts

# Register your models here.
admin.site.register(Contacts),
admin.site.register(User),