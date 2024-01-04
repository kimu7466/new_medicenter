from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import CounterTable, doctor
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(CounterTable)
admin.site.register(doctor)