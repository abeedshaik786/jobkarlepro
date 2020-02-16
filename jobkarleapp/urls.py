from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FresherRigister',views.FresherRigister,name="FresherRigister"),
    path('CompanyRegister',views.CompanyRegister,name="CompanyRegister"),
    path('Login',views.Login,name='Login'),
    path('ProfileData/(?P<User_id>[0-9]+)/$',views.ProfileData,name='ProfileData'),
    path('Support_Course/(?P<User_id>[0-9]+)/$',views.Support_Course,name='Support_Course'),
    path('load_Course',views.load_Course,name='load_Course'),
    path('mulltisearch',views.mulltisearch,name='mulltisearch'),
    path('Fresherdata',views.Fresherdata,name="Fresherdata"),
    path('country_list',views.country_list,name='country_list'),
    path('FresherQualification',views.FresherQualification,name="FresherQualification"),
    path('Logout',views.Logout,name='Logout'),
    


]