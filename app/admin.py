from django.contrib import admin

from .models import User, Grievance

admin.site.site_header = "Student Grievance System Admin Interface"
admin.site.site_title = "Student Grievance System"
admin.site.index_title = "Welcome to Student Grievance System Admin Panel"


admin.site.register(User)
admin.site.register(Grievance)