from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import  FresherModel,FresherDataModel,FresherQualificationModel,Qualification_Course
from .models import FresherQualification,JobRequirments
from django.core.files.storage import FileSystemStorage
from .functions import handle_uploaded_file
from .models import Fresher,FresherData,JobRequirments
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
import json
import datetime
from .filters import snippetFilter
from django.views.generic import ListView,DetailView
from django.db.models import Q
import sys
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth import login,logout,authenticate




# Create your views here.
# def Home_of_jobkarle(Listview):
#     model = JobRequirments
#     template_name = jobkarleapp/ba
def FresherRigister(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        Fresher_id = request.POST.get("Fresher_id")
        forms = FresherModel(request.POST)
        # import pdb;pdb.set_trace()
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('FresherData')
           
    forms = FresherModel()
    latest_updates = JobRequirments.objects.latest('id')
    return render(request,'FresherRigister.html',{ 'forms':forms,'latest_updates':latest_updates})
def mulltisearch(request):
    if request.method == "GET":

        Role = request.GET.get('role')
        Location = request.GET.get('location')
        Experiance = request.GET.get('experiance')
        Salary = request.GET.get('salary')
        # sys.setrecursionlimit(10**6)
        filter_data = JobRequirments.objects.filter(Q(Interview_Location__iexact = Location) | Q(Skills__iexact = Role) ).order_by()
        # sys.setrecursionlimit(10**6)
        import pdb;pdb.set_trace()
        return render(request,'multifilter.html',{'filter_data':filter_data})

def FresherData(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        forms = FresherDataModel(request.POST)
        import pdb;pdb.set_trace()
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('FresherQualification')
        return render(request,'FresherData.html',{'forms':forms})
    forms = FresherDataModel()
    return render(request,'FresherData.html',{'forms':forms})
def FresherQualification(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        forms = FresherQualificationModel(request.POST, request.FILES)
        import pdb;pdb.set_trace()
        if forms.is_valid():
            forms.save()
            dump = request.POST.get('#id_Course_Type')
           
        else:
              return render(request,'FresherQualification.html',{'forms':forms})
    forms = FresherQualificationModel()
    return render(request,'FresherQualification.html',{'forms':forms})
def country_list(request):
    country_data1 = []
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        # to read the data from COUNTRIES2.json in this project
        country_data = json.loads(open(settings.COUNTRIES2[0], 'r').read())
        return HttpResponse(json.dumps(country_data))
    else:
        pass

def load_Course(request):
    Highest_Qualification_id = request.POST.get('Highest_Qualification_id')
    import pdb;pdb.set_trace()
    #data = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by('name')
    courses_data = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by('name')
    data = courses_data.values_list('name',flat=True)
    data_list = [name for name in data]
    return JsonResponse({'data':json.dumps(data_list)})
    #return HttpResponse(json.dumps(data))
    #return render(request, 'FresherQualification.html', {'data':data})
# def Users_Login(request):
#     if request.method =="POST":
#         Username = request.POST.get('username')
#         Password = request.POST.get('password')
#         user = auth
#         if Username and Password:



