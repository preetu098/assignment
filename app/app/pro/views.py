from django.shortcuts import render
from .models import AssignmentHelp
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
    if(request.method=='POST'):
        assignment=AssignmentHelp()
        assignment.email=request.POST['email']
        assignment.name=request.POST['name']
        assignment.location=request.POST['location']
        assignment.phone_code=request.POST['code']
        assignment.phone=request.POST['num']
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


