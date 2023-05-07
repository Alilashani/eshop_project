from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Admin)
admin.site.register(models.User)
admin.site.register(models.Customer)
