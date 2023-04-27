from django import forms

PLANT_QUANTITY_CHOICES =[(i, str(i)) for i in range(1, 21)]

class CartAddPlantForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PLANT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)