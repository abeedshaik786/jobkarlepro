from django import forms
from django.forms import ModelForm
from .models import Fresher,FresherData,FresherQualification,Qualification_Course

class FresherModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FresherModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
    class Meta:
        model = Fresher
        fields = '__all__'
class FresherDataModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FresherDataModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
            if field == 'Nationality':
                self.fields[field].widget.attrs["id"] = "id_country"
    class Meta:
        model = FresherData
        fields = '__all__'
class FresherQualificationModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FresherQualificationModel,self).__init__(*args,**kwargs)
        self.fields['Course'].queryset = Qualification_Course.objects.none()
        if 'country' in self.data:
             try:
                 Highest_Qualification_id = int(self.data.get('country'))
                 self.fields['Course'].queryset = Qualification_Course.objects.filter(country_id=Highest_Qualification_id).order_by('name')
             except (ValueError, TypeError):
                 pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Course'].queryset = self.instance.Highest_Qualification.Course_set.order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            self.fields[field].widget.attrs['placeholder'] = field
    class Meta:
        model = FresherQualification
        fields = '__all__'
