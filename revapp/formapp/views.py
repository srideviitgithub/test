from django.shortcuts import render

# Create your views here.

def firstform(req):
    return render(req,'formapp/firstform.html')
