from django import forms
from .models import SurfClass, MembershipPlan, Products

class SurfClassForm(forms.ModelForm):
    class Meta:
        model = SurfClass
        fields = ['titulo', 'instructor', 'precio']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = ['nombre', 'descripcion', 'precio']

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['nombre', 'descripcion', 'precio']

