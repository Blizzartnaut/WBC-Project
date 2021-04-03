from django import forms
from .models import Temperature
from datetime import date, time
'''class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]'''

class RawProductForm(forms.Form):
    title = forms.CharField(),
    description = forms.CharField(),
    price = forms.DecimalField()

class TemperatureForm(forms.ModelForm):
    burnerzone = forms.IntegerField(label="BurnerZone", required=True)
    burner_1 = forms.IntegerField(label='Burner 1', required=False)
    burner_2 = forms.IntegerField(label='Burner 2', required=False)
    burner_3 = forms.IntegerField(label='Burner 3', required=False)
    burner_4 = forms.IntegerField(label='Burner 4', required=False)
    burner_5 = forms.IntegerField(label='Burner 5', required=False)
    burner_6 = forms.IntegerField(label='Burner 6', required=False)
    burner_7 = forms.IntegerField(label='Burner 7', required=False)
    burner_8 = forms.IntegerField(label='Burner 8', required=False)
    burner_9 = forms.IntegerField(label='Burner 9', required=False)
    burner_10 = forms.IntegerField(label='Burner 10', required=False)
    burner_11 = forms.IntegerField(label='Burner 11', required=False)
    burner_12 = forms.IntegerField(label='Burner 12', required=False)
    user = forms.CharField(label='User', max_length=30, required=True)
    class Meta:
        model = Temperature
        exclude = ['date_created', 'time']

'''class GetTemperature(forms.ModelForm):
    Date = forms.DateField(, required=True)
    class Meta:
        model = Temperature
        fields = "__all__"'''