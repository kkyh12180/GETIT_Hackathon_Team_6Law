from django.contrib import admin
from .models import Check_table, Store, Review

# Register your models here.
admin.site.register(Store)
admin.site.register(Check_table)
admin.site.register(Review)
