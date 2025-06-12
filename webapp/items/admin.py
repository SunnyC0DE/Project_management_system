from django.contrib import admin

# Register your models here.
from .models import Categories, Items


admin.site.register(Categories)
admin.site.register(Items)