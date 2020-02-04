from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TITLE_CHOICES = [
    ('male', 'Male.'),
    ('female', 'Female.'),
    ('other', 'Other'),
]
Qualification_CHOICES = [
    ('Doctorate/PhD', 'Doctorate/PhD'),
    ('Masters/Post-Graduation', 'Masters/Post-Graduation'),
    ('Graduation/Diploma', 'Graduation/Diploma'),
    ('12th','12th'),
    ('12th','10th'),
    ('below 10th','Below 10th')
]
class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Qualification_Course(models.Model):
    country = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Fresher(models.Model):
    FirstName = models.CharField(max_length=100,blank=False)
    SecondName = models.CharField(max_length=100,blank=False)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()
    UserName = models.CharField(blank=False,max_length=100)
    Password = models.CharField(blank=False,max_length=100)
    def __str__(self):
        return self.UserName
class FresherData(models.Model):
    Gender = models.CharField(max_length=4,choices=TITLE_CHOICES)
    Nationality = models.CharField(max_length=100,blank=False)
    Religion = models.CharField(max_length=100,blank=False)
    fresher = models.ForeignKey(Fresher,on_delete=models.CASCADE,null=True )
class FresherQualification(models.Model):   
    Highest_Qualification= models.ForeignKey(Qualification,on_delete=models.SET_NULL, null=True,max_length=100)
    Course = models.ForeignKey(Qualification_Course,on_delete=models.SET_NULL,blank=True,null=True,max_length=100)
    Specialization = models.CharField(max_length=100,)
    Course_Type = models.CharField(max_length=100)
    Passing_Year = models.CharField(max_length=100)
    Resume = models.FileField(upload_to = 'Resume')
    fresher = models.ForeignKey(Fresher,on_delete=models.CASCADE)
    def __str__(self):
        return self.Specialization
class JobRequirments(models.Model):
    CompanyName = models.CharField(max_length=100)
    Company_Description = models.CharField(max_length=100)
    Skills = models.CharField(max_length=100)
    Roles_and_Responsabulity = models.CharField(max_length=100)
    Iterview_Date = models.DateField()
    Interview_Location = models.CharField(max_length=100)
    First_HrName = models.CharField(max_length=100)
    Second_HrName = models.CharField(max_length=100)
    First_HrNumber = models.IntegerField()
    Second_HrNumber = models.IntegerField()
    manager = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self):
        return self.CompanyName

