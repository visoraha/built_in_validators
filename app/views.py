from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'tfo':TFO}
    if request.method=='POST':
        SFD=TopicForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('data is invalid')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    WFO=WebpageForm()
    d={'wfo':WFO}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse(str(WFD.cleaned_data))
        else:
            return HttpResponse('it is invalid data')
    return render(request,'insert_webpage.html',d)
