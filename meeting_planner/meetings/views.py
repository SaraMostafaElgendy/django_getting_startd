from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting,Room
from django.forms import modelform_factory
# Create your views here.

def detail(request,id):
    meeting=get_object_or_404(Meeting,pk=id)
        #Meeting.objects.get(pk=id)
    return  render(request,"meetings/detail.html",{"meeting":meeting})

def room_list(request):
    return  render( request,"meetings/room_list.html",{"rooms": Room.objects.all()})
        #Meeting.objects.get(pk=id)
MeetingForm=modelform_factory(Meeting,exclude=[])
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm();
    return  render(request, "meetings/new.html", {'form': form})
