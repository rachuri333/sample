from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def person(request):
    form=forms.persondetails()
    if request.method=='POST':
        form=forms.persondetails(request.POST)
        if form.is_valid():
            print('Name')
    return render(request,'testapp/person.html',{'form':form})