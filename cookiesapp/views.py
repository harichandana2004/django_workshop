from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def set_cookie(_____):
    response=HttpResponse("Cookie set!")
    response.set_cookie('username','hari')
    return response
def get_cookie(request):
    username=request.COOKIES.get('username','Guest')
    return HttpResponse(f"Hello, {username} !")