from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FresherRigister',views.FresherRigister,name="FresherRigister"),
    path('FresherData',views.FresherData,name="FresherData"),
    path('country_list',views.country_list,name='country_list'),
    path('FresherQualification',views.FresherQualification,name="FresherQualification"),
    path('load_Course', views.load_Course, name='load_Course')

]