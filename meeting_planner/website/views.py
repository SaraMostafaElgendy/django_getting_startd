from django.shortcuts import render
from django.http import HttpResponse
from datetime import  datetime
from django.shortcuts import  render
from meetings.models import Meeting
# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html",{"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse("date now"+ str(datetime.now()))
def about(request):
    return HttpResponse("it's about page")