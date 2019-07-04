from django.contrib import admin
from ams import models
# Register your models here.
admin.site.register(models.SubjectByFaculty)
admin.site.register(models.Attendance)
admin.site.register(models.Students)
admin.site.register(models.StudentByClass)
admin.site.register(models.Branch)
admin.site.register(models.Faculty)
admin.site.register(models.AcademicYear)
admin.site.register(models.Semester)
admin.site.register(models.Subject)
