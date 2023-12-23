from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Service, Guard, Contact,Registration,About
from django.contrib import messages

# from cms.models import contact

def index(request):
    listserdata=Service.objects.all()
    listgrdata=Guard.objects.all()
    listabdata=About.objects.all()
    listdataserver={
        'listdata':  listserdata,
        'listdata2': listgrdata,
        'listdata3': listabdata
        
    }
    return render(request,"index.html",listdataserver)

def about(request):
    listabdata=About.objects.all()
    listdataserver={
        'listdata3': listabdata
    }
    return render(request, "about.html",listdataserver)

def registration(request):

    if request.method=='POST':
        name = request.POST.get("fname")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        passwd = request.POST.get("passwd")
        formdata=Registration(rname=name,runame=uname, remail=email, rpass=passwd)
        formdata.save()
        messages.success(request, 'Thank you for Registration. Now Login')
        return render(request,"login.html")


    
    return render(request,"registration.html")

def contact(request):

    if request.method=='POST':
        name = request.POST.get("fname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        formdata=Contact(cname=name, cemail=email, cphone=phone, cmsg=message)
        formdata.save()
        messages.success(request, 'Thank you for contacting us')

    
    return render(request,"contact.html")

def guard(request):
    listgrdata=Guard.objects.all()
    listdataserver={
        'listdata2': listgrdata,
    }
    return render(request,"guard.html",listdataserver)

def service(request):
    listserdata=Service.objects.all()
    listdataserver={
        'listdata':  listserdata
     }
    return render(request,"service.html",listdataserver)

def login(request):
    return render(request,"login.html")
# Create your views here.
