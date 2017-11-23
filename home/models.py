from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    course_fees = models.CharField(max_length=250)


    def __str__(self):
        return self.course_name

class Student(models.Model):
    f_name=models.CharField(max_length=250)
    m_name=models.CharField(max_length=250, blank=True)
    l_name=models.CharField(max_length=250)
    school=models.CharField(max_length=250)
    age=models.IntegerField()
    image=models.FileField(max_length=250, blank=True)
    about=models.CharField(max_length=500,blank=True)
    course_id=models.ManyToManyField(Course)

    def get_absolute_url(self):
        return reverse('home:student_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.f_name+''+self.l_name


class Takes (models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id= models.ForeignKey(Course, on_delete=models.CASCADE)


class Faculty(models.Model):
    course_id = models.ManyToManyField(Course)
    f_name = models.CharField(max_length=250)
    m_name = models.CharField(max_length=250, blank=True)
    l_name = models.CharField(max_length=250)
    semester=models.CharField(max_length=250)
    year=models.CharField(max_length=250)
    image = models.FileField(max_length=250, blank=True)
    about=models.CharField(max_length=500, blank=True)
    quote=models.CharField(max_length=250,blank=True)

    def get_absolute_url(self):
        return reverse('home:fac_detail', kwargs={'pk' :self.pk})

    def __str__(self):
        return self.f_name+''+self.l_name

class Test(models.Model):
    course_id= models.ForeignKey(Course, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    total=models.IntegerField()
    date=models.DateTimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name\

class Write(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    test_id=models.ForeignKey(Test,on_delete=models.CASCADE)
    score=models.IntegerField()




class Teaches(models.Model):
    faculty_id=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    course_id= models.ForeignKey(Course, on_delete=models.CASCADE)
    semester=models.IntegerField()
    year=models.IntegerField()

