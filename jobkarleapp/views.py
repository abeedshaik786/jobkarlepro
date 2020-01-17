from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import  FresherModel,FresherDataModel,FresherQualificationModel,Qualification_Course
from .models import Fresher,FresherData,JobRequirments
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.
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
    return render(request,'FresherRigister.html',{ 'forms':forms })
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
        forms = FresherQualificationModel()
        if forms.is_valid():
            forms.save()
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