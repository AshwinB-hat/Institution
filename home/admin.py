from django.contrib import admin
from .models import Student, Faculty, Course, Teaches
from .models import Takes,Test,Write,Teaches

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Takes)
admin.site.register(Write)
admin.site.register(Test)
admin.site.register(Teaches)