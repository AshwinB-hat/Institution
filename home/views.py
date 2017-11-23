from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Student,Course,Faculty,Takes,Test,Teaches
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth   import authenticate,login
from django.views.generic import View
from .forms import UserForm

from django import forms
import operator
from django.template import RequestContext



class IndexView(generic.TemplateView):
    template_name='home/home.html'


    def facultys(self):
        return Faculty.objects.all()

    def course(self):
        return Course.objects.all()

class StudentView(generic.ListView):
    template_name='home/student.html'

    def get_queryset(self):
        return Student.objects.all()

class DetailFacView(generic.DetailView):
    model=Faculty
    template_name='home/fac_detail.html'

class DetailStudentView(generic.DetailView):
    model=Student
    template_name='home/student_detail.html'


class StudentCreate(CreateView):
    model=Student
    fields=['f_name','m_name','l_name','school','age','about','image','course_id']

class Search(generic.TemplateView):
    template_name='home/search.html'

class TestView (generic.TemplateView):
    template_name='home/test.html'
    def test(self):
        return Test.objects.all()

def SearchForm(request):
    query=request.GET.get('q')

    if query:
        results=Student.objects.filter(f_name=query)
        context=RequestContext(request)

        return render(request,'home/search.html',{"results":results})

