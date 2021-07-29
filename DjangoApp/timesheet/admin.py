from django.contrib import admin
from .models import RC, SignInEntry, SignOutEntry

# Register your models here.
admin.site.register(RC)
admin.site.register(SignInEntry)
admin.site.register(SignOutEntry)