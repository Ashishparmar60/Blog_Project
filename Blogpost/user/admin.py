from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Blog)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class Comments(admin.ModelAdmin):
    pass

