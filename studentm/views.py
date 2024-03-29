from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import student_data
def home(request):
    students=student_data.objects.all()
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        student_data.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            gender=gender
        )
        return HttpResponse("<a href='/first.html'>Go back</a>")
        
    return render(request,'first.html',{'students':students})
    
    