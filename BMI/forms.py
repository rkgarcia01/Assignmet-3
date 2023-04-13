from django import forms 
from .models import Patient
from django.forms import ModelForm


class BmiForm(forms.Form): 
    height = forms.FloatField(label="Height in Inches:", required=True, min_value = 0)
    weight = forms.FloatField(label="Weight in Pounds:", required = True, min_value = 0)

class PatientForm(ModelForm):
    class Meta: 
        model = Patient
        fields = '__all__'
'''
#working 2

class BmiForm(forms.Form): 
    height = forms.FloatField(label="Height in meters:", required=True, min_value = 0)
    weight = forms.FloatField(label="Weight in Kg:", required = True, min_value = 0)

class PatientForm(ModelForm):
    class Meta: 
        model = Patient
        fields = '__all__'
'''
'''
#Height is in Meters
#Weight is in Kilograms
class BmiForm(forms.Form): 
    height = forms.FloatField(label="Height in meters", min_value = 0 )
    weight = forms.FloatField(label="Weight in Kilograms", min_value = 0)

class BmiMeasurementForm(forms.ModelForm): 
    class Meta: 
        model = BmiMeasurement
        #fields = ["id", "height_in_meters", "weight_in_kg", "measured_at"]
        fields = '__all__'
'''
'''
#working

class PatientForm(ModelForm):
    class Meta: 
        model = Patient
        fields = '__all__'
'''
'''
class InputForm(forms.Form): 
    Height = forms.CharField(max_length = 200)
    Weight = forms.CharField(max_length = 200)
'''