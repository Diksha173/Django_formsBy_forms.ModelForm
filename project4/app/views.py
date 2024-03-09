from django.shortcuts import render,HttpResponse
from app.forms import*

# Create your views here.
def create_Topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        TFDO.save()
        return HttpResponse('store successfully')
    return render(request,'page1.html',d)
def create_webpage(request):
    return render(request,'page2.html')