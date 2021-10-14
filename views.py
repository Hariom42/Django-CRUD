from django.shortcuts import render ,HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

from .models import users

# view for the add and show the data
def add_show(request):
    if request.method =='POST':
        fm =StudentRegistration(request.POST)
        #below for save data into database
        if fm.is_valid():
            #fm.save()   by these 2 line our code can stored into the database at a single command
            nm =fm.cleaned_data['name']
            em =fm.cleaned_data['email']
            pw =fm.cleaned_data['password']
            req =users(name=nm,email=em,password=pw)
            req.save()
            fm =StudentRegistration()
    else:
        fm =StudentRegistration()
    stud=users.objects.all()

    return render(request,'enroll/addnshow.html',{'form':fm,'stu':stud})
    #return render(request,'enroll/addnshow.html')


# delete the data
def delete_data(request,id):
	if request.method == 'POST':
		pi =users.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')


# Update data
def update_data(request,id):
    if request.method =='POST':
        pi = users.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = users.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render (request ,'enroll/updatestudent.html',{'formm':fm})
































