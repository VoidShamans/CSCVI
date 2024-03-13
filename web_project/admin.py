from django.contrib import admin
from django.contrib.auth.models import User  # or your custom user model

admin.site.unregister(User)