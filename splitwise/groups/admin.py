from django.contrib import admin
from .models import GroupMembership,Group

# Register your models here.
admin.site.register(Group)
admin.site.register(GroupMembership)
