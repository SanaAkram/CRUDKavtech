from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import Student
from .models import User


# Add/View Function
def add_show(request):
    if request.method == 'POST':

        crud = Student(request.POST)
        if crud.is_valid():
            name = crud.cleaned_data['name']
            email = crud.cleaned_data['email']
            password = crud.cleaned_data['password']
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Already Exists in Record')
            else:
                add = User(name=name, email=email, password=password)
                add.save()
                messages.success(request, 'Record Added Successfully !')
            crud = Student()

    else:
        crud = Student()
    data = User.objects.all()

    return render(request, 'crud/addshow.html', {'form': crud, 'data': data})


# Update Function
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        crud = Student(request.POST, instance=pi)
        if crud.is_valid():
            crud.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        crud = Student(instance=pi)

    return render(request, 'crud/update.html', {'form': crud})


# Delete Function
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.warning(request, 'Record Deleted !')
        return HttpResponseRedirect('/')
