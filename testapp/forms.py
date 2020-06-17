from django import forms


class persondetails(forms.Form):
    Name=forms.CharField(max_length=100)
    Phone=forms.IntegerField()
    Address=forms.CharField(max_length=200)
    Email=forms.EmailField()