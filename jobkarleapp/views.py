from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import  FresherModel,FresherDataModel,FresherQualificationModel,Qualification_Course
from .models import FresherQualification,JobRequirments,FresherData
from django.core.files.storage import FileSystemStorage
from .functions import handle_uploaded_file
from .models import Fresher,FresherData,JobRequirments,ProfileImg
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
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.urls import reverse

@requires_csrf_token

@csrf_exempt

@cache_page(60 * 15)
@csrf_protect





# Create your views here.
# def Home_of_jobkarle(Listview):
#     model = JobRequirments
#     template_name = jobkarleapp/ba
def FresherRigister(request):
    
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = User(first_name = firstname , last_name = lastname ,email = email , username = username ,password = password)
        obj.set_password(password)
        obj.is_student = True
        obj.save()
        return HttpResponseRedirect('Fresherdata')
           
    forms = FresherModel()
    latest_updates = JobRequirments.objects.latest('id')
    return render(request,'FresherRigister.html',{ 'forms':forms,'latest_updates':latest_updates})

def CompanyRegister(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = User(first_name = firstname , last_name = lastname ,email = email , username = username ,password = password)
        obj.set_password(password)
        obj.is_staff = True
        obj.save()
        return HttpResponseRedirect('FresherData')
def profileimg(request):
    pass
def ProfileData(request,User_id):
    user_data = User.objects.get(id=User_id)
    student_jobs = JobRequirments.objects.all()
    # import pdb;pdb.set_trace()
    user_personal_data = FresherData.objects.get(user_id=user_data.id)
    profilepic = ProfileImg.objects.get(user_id=user_data.id)
    return render(request,'userpage.html',{
        'user_data':user_data,
        'student_jobs':student_jobs,
        'user_personal_data':user_personal_data,
        'profilepic':profilepic,

    })
@ensure_csrf_cookie
@csrf_exempt
@cache_page(60 * 15)
@csrf_protect
@requires_csrf_token
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = authenticate(request,username = username , password = password)
        validation = User.objects.get(username=username)
        if validation.is_staff == False:
            if users is not None:
                login(request,users)
                user_data = User.objects.get(username=username)
                return HttpResponseRedirect(reverse('jobkarleapp:ProfileData', args={user_data.id}))
        else:
            if  validation.is_staff == True:
                if users is not None:
                    import pdb;pdb.set_trace()
                    login(request,users)
@ensure_csrf_cookie
@cache_page(60 * 15)                
@csrf_protect
def Logout(request):
    logout(request)
    return HttpResponseRedirect('FresherRigister')
def mulltisearch(request):
    if request.method == "GET":

        Role = request.GET.get('role')
        Location = request.GET.get('location')
        Experiance = request.GET.get('experiance')
        Salary = request.GET.get('salary')
        # sys.setrecursionlimit(10**6)
        filter_data = JobRequirments.objects.filter(Q(Interview_Location__iexact = Location) | Q(Skills__iexact = Role) ).order_by()
        # sys.setrecursionlimit(10**6)
        # import pdb;pdb.set_trace()
        return render(request,'multifilter.html',{'filter_data':filter_data})

def Fresherdata(request):
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
def Support_Course(request,Highest_Qualification_id):
    data_list = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by()
    return JsonResponse({'data':json.dumps(data_list)})
def load_Course(request):
    Highest_Qualification_id = request.POST.get('Highest_Qualification_id')
    import pdb;pdb.set_trace()
    #data = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by('name')
    courses_data = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by()
    data = courses_data.values_list('name',flat=True)
    data_list = [name for name in data]
    return HttpResponseRedirect(reverse('jobkarleapp:Support_Course',kwargs={'Highest_Qualification_id.id'}))
    
    #return HttpResponse(json.dumps(data))
    #return render(request, 'FresherQualification.html', {'data':data})
# def Users_Login(request):
#     if request.method =="POST":
#         Username = request.POST.get('username')
#         Password = request.POST.get('password')
#         user = auth
#         if Username and Password:
def room(request, room_name):
    return render(request, 'multifilter.html', {
        'room_name': room_name
    })
