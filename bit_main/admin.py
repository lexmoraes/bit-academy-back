from django.contrib import admin

from bit_main import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    exclude = ()
