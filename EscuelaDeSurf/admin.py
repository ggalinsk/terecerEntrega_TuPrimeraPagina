from django.contrib import admin

# Register your models here.
from .models import SurfClass, MembershipPlan, Products

admin.site.register(SurfClass)
admin.site.register(MembershipPlan)
admin.site.register(Products)