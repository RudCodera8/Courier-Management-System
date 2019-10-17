from django.contrib import admin
from .models import student 

# Register your models here.

admin.site.register(student)

admin.site.site_header = "Courier Management System"
admin.site.site_title = "Courier Management System"
admin.site.index_title = "Management Hub - Student List"
