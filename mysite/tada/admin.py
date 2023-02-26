from django.contrib import admin

# Register your models here.

from .models import Tada, Module, Setting

admin.site.register(Tada)

admin.site.register(Module)

admin.site.register(Setting)