import imp
from django.contrib import admin
from .models import Room ,Message
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
#admin pass=12345