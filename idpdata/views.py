from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from django.http import HttpResponse
from .models import User

from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account
from .forms import IDPRegistration
def idpdata_view(request):
    if request.method == 'POST':
        fm  = IDPRegistration(request.POST)        
        if fm.is_valid():
            fm.save()
    else:
        fm  = IDPRegistration()
    stud = User.objects.all()
    return render(request, 'idpdata/idpdata.html', {'form':fm , 'stu':stud})

def add_data(request):    
	return render(request, "idpdata/addidpdata.html")

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/idpdata')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = IDPRegistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = IDPRegistration(instance = pi)

    return render(request, 'idpdata/updatedata.html', {'form': fm})
