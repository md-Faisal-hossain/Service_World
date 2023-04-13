from django.contrib import admin
from .models import Member, ProviderMember

# Register your models here.

admin.site.register(Member)
admin.site.register(ProviderMember)
