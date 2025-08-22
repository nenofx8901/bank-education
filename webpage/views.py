from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request,): 
    if request.user.is_authenticated:
        return redirect("users/dashboard")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('users/dashboard')
            else:
                messages.info(request, "username or password is incorrect")


    return render(request, 'webpage/home.html')

def checking(request):

    return render(request, 'webpage/checking.html')

def locationandhours(request):

    return render(request, 'webpage/location&hours.html')

def termsandcondition(request):

    return render(request, 'webpage/termsandcondition.html')

def rates(request):
    return render(request, 'webpage/rates.html')

def savings(request):
    return render(request, 'webpage/savings.html')

def healthsaving(request):
    return render(request, 'webpage/health-saving.html')

def cdira(request):
    return render(request, 'webpage/CD-Ira.html')

def personalLoan(request):
    return render(request, 'webpage/personal-loan.html')

def AdditionalServices(request):
    return render(request, 'webpage/Additional-Services.html')

def OnlineEducation(request):
    return render(request, 'webpage/online-education.html')

def atm(request):
    return render(request, 'webpage/ATM.html')

def BusinessChecking(request):
    return render(request, 'webpage/business-checking.html')

def BusinessSavings(request):
    return render(request, 'webpage/Business-Savings.html')

def cds(request):
    return render(request, 'webpage/CDs.html')

def BusinessLoan(request):
    return render(request, 'webpage/Business-Loan.html')

def LandTrust(request):
    return render(request, 'webpage/Land-Trust.html')

def notfound(request):
    return render(request, 'webpage/notfound.html')

def aboutus(request):
    return render(request, 'webpage/aboutus.html')
def team(request):
    return render(request, 'webpage/team.html')

def news(request):
    return render(request, 'webpage/news.html')

def contactus(request):
    return render(request, 'webpage/contactus.html')

def customercontent(request):
    return render(request, 'webpage/customercontent.html')

def faqs(request):
    return render(request, 'webpage/faqs.html')

def privacy(request):
    return render(request, 'webpage/privacy.html')
def disclousure(request):
    return render(request, 'webpage/disclousure.html')

def Accessibility(request):
    return render(request, 'webpage/Accessibility.html')

def security(request):
    return render(request, 'webpage/security.html')

def resources(request):
    return render(request, 'webpage/resources.html')