from django.contrib import admin
from advertisement.models import database
from advertisement.models import File

# Register your models here.
admin.site.register(database)
admin.site.register(File)