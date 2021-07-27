from django.contrib import admin
from timesheet.models import RC, SignInEntry

# Register your models here.
admin.site.register(RC)
admin.site.register(SignInEntry)