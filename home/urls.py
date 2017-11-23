from django.conf.urls import url
from . import views
app_name='home'
urlpatterns = [


#/home/
    url(r'^$', views.IndexView.as_view(), name="index"),

url(r'^student/$', views.StudentView.as_view(), name="student"),

url(r'^test/$', views.TestView.as_view(), name="test"),


#/home/faculty/<faculty-id>
    url(r'^faculty/(?P<pk>[0-9]+)/$', views.DetailFacView.as_view(), name="fac_detail"),
#create
#/home/faculty/add
    url(r'student/add/$',views.StudentCreate.as_view(), name="student_add"),
#/home/student/search?q=''
    url (r'student/search',views.SearchForm,name="search"),
    url(r'^student/(?P<pk>[0-9]+)/$', views.DetailStudentView.as_view(), name="student_detail")
]
