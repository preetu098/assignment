from .models import AssignmentHelp
from django.conf import settings
from django import render
from django.core.mail import send_mail
# home page
def index(request):
    return render(request,"index.html")

def payment(request):
    return render(request,"Payment.html")

def requestTutor(request):
    return render(request,"requestTutor.html")

def register(request):
    return render(request,"register.html")

def assignmenthelp(request):
    secret=b'86di#w(le=dcg)&20e9+7#fuj73*um+19vdj@3$gz3rx+3vd=t'
    if(request.method=='POST'):
        assignment=AssignmentHelp()
        assignment.email=request.POST['email']
        e=request.POST['email']
        em=AssignmentHelp.objects.filter(email=e)
        if (em):
            print("email already exist")
            pass

        else:
            assignment.name=request.POST['name']
            assignment.location=request.POST['location']
            assignment.phone_code=request.POST['code']
            assignment.phone=request.POST['num']
            assignment.email=request.POST['email']   
            assignment.details=request.POST['details']
            assignment.subject=request.POST['subject']
            assignment.want=request.POST['want']
            assignment.meeting=request.POST['meeting']
            assignment.date=request.POST['date']
            assignment.budget=request.POST['price']
            assignment.workmode=request.POST['pricemode']
            assignment.gender=request.POST['gender']
            assignment.language=request.POST['lan']
            assignment.documents=request.POST['doc']
            assignment.save()
        
        
            message="Thankyou for register."
            subject="Thankyou message. "
            receipent=[e]
            sender=settings.EMAIL_HOST_USER
            send_mail(subject,message,sender,receipent)
            xy="worktest101test@gmail.com"
            a=request.POST['name']
            b=request.POST['num']
            c=request.POST['subject']
            d=request.POST['price']
            message="Email:"+e+"\n Name:"+a+"\n Number:"+b+" \n Subject:"+c+"\n Budget:"+d
            subject="New registration"
            receipent=[xy]
            sender=settings.EMAIL_HOST_USER
            send_mail(subject,message,sender,receipent)
            return render(request,"assignmenthelp.html",{'msj':'submitted succesfully'})

    return render(request,"assignmenthelp.html")

#after Login Pages    

def dashboard(request):
    return render(request,"dashboard.html")

def mobile(request):
    return render(request,"mobileVerified.html")


def getCoins(request):
    return render(request,"buycoins.html")

def coinsform(request):
    return render(request,"coins.html")

def coinStatus(request):
    return render(request,"coinsstatus.html")

def promote(request):
    return render(request,"promote.html")

def invite(request):
    return render(request,"invite.html")

def searchRecord(request):
    return render(request,"searchRecord.html")


