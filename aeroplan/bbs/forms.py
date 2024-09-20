from django import forms

class ConversionForm(forms.Form):
    departure = forms.CharField(label='Departure', max_length=100)
    arrival = forms.CharField(label='Arrival', max_length=100)
    base_fare = forms.IntegerField(label='base_fare', required=True)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    points1 = forms.IntegerField(label='Points 1', required=True)
    cash1 = forms.DecimalField(label='Cash 1', max_digits=10, decimal_places=2)
    points2 = forms.IntegerField(label='Points 2', required=False)
    cash2 = forms.DecimalField(label='Cash 2', max_digits=10, decimal_places=2, required=False)
    points3 = forms.IntegerField(label='Points 3', required=False)
    cash3 = forms.DecimalField(label='Cash 3', max_digits=10, decimal_places=2, required=False)
    points4 = forms.IntegerField(label='Points 4', required=False)
    cash4 = forms.DecimalField(label='Cash 4', max_digits=10, decimal_places=2, required=False)