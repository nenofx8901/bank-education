from django.shortcuts import render, redirect
from .models import Reg, Transfer, History
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .forms import ProfileForm

# Create your views here.

def logoutUser(request):
    logout(request)

    return redirect ("home")
    # return render(request, "webpage/home.html")

@login_required(login_url='home')
def dashboard(request):
    transfer = Transfer.objects.filter(user=request.user)
    history = History.objects.all().order_by('-date')  # Most recent first
    context = {
        'transfer': transfer,
        'history': history,
    }
    return render(request, "users/dashboard.html", context)


@login_required(login_url='home')
def accountsummary(request):
   
    return render (request, "users/accountsummary.html")

@login_required(login_url='home')
def accountdetails(request):
   
    return render (request, "users/accountdetails.html")

@login_required(login_url='home')
def creditcards(request):
    return render (request, "users/creditcards.html")

@login_required(login_url='home')
def contactus(request):
    return render (request, "users/contactus.html")

@login_required(login_url='home')
def billpaycenter(request):

    return render(request, "users/billpaycenter.html")

@login_required(login_url='home')
def deletepaytoaccount(request):

    return render (request, "users/deletepaytoaccount.html")

@login_required(login_url='home')
def paynow(request):

    return render (request, "users/paynow.html")

@login_required(login_url='home')
def paynowc(request):

    return render (request, "users/paynowc.html")

@login_required(login_url='home')
def searchpaytolist(request):

    return render (request, "users/searchpaytolist.html")

@login_required(login_url='home')
def beneficiary(request):

    return render (request, "users/beneficiary.html")

@login_required(login_url='home')
def addbeneficiery(request):

    return render (request, "users/add-beneficiery.html")

def profile(request):
    
    reg = request.user.reg
    form = ProfileForm(instance=reg)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=reg)
        if form.is_valid():
            form.save()

    context ={'form':form}
    return render (request, "users/profile.html", context)

def changepin(request):

    return render(request, "users/pin.html")

def changepassword(request):

    
    return render(request, "users/changepassword.html")

def transfer(request):

    reg = Reg.objects.get(user=request.user)
    if reg.status == 'Suspended':
        messages.error(request, "This account is RESTRICTED and can't perform this operation")
        return redirect('dashboard')

    if request.method == 'POST':
        # Step 1: Form submitted, go to confirmation page
        from_account = request.POST.get('from_account', 'Checking')
        to_account_type = request.POST.get('to_account_type', '')
        bank_name = request.POST.get('bank_name', '')
        account_number = request.POST.get('account_number', '')
        account_name = request.POST.get('account_name', '')
        amount = request.POST.get('amount', '')
        description = request.POST.get('description', '')

        # Pass all data to confirmation page
        context = {
            'from_account': from_account,
            'to_account_type': to_account_type,
            'bank_name': bank_name,
            'account_number': account_number,
            'account_name': account_name,
            'amount': amount,
            'description': description,
        }
        request.session['transfer_data'] = context
        return redirect('confirmtransfer')

    return render(request, "users/transfer.html")

def enterpin(request):

    return render(request, "users/enterpin.html")


def confirm_transfer(request):

    transfer_data = request.session.get('transfer_data', {})
    reg = Reg.objects.get(user=request.user)
    if request.method == 'POST':
        # Get PIN from 4 fields
        pin = ''.join([
            request.POST.get('pin1', ''),
            request.POST.get('pin2', ''),
            request.POST.get('pin3', ''),
            request.POST.get('pin4', '')
        ])
        # Clean and parse amount (remove commas, $)
        raw_amount = str(transfer_data.get('amount', 0)).replace(',', '').replace('$', '').strip()
        try:
            amount = float(raw_amount)
        except Exception:
            amount = 0.0
        abc = reg.account_balance
        if amount > int(abc):
            messages.error(request, "Insufficient funds: You cannot transfer more than your available balance.")
            return redirect('confirmtransfer')
        if str(reg.account_pin) == str(pin):
            # Deduct balance and create transfer
            Reg.objects.filter(user=request.user).update(account_balance=int(abc)-amount)
            # Create Transfer record
            Transfer.objects.create(
                counter=1,
                description=transfer_data.get('description', ''),
                amount=amount,
                user=request.user,
                mode='modal'
            )
            # Create History record
            from datetime import datetime
            History.objects.create(
                icon="up",
                color="black",
                date=datetime.now(),
                description=transfer_data.get('description', 'WIRE TRANSFER'),
                amount=-amount,
                status="Approved"
            )
            # Generate reference and date
            import random
            reference = f"TX-{random.randint(100000,999999)}"
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Store for success page
            request.session['transfer_receipt'] = {
                **transfer_data,
                'amount': amount,
                'reference': reference,
                'date': date,
            }
            return redirect('successful')
        else:
            messages.warning(request, "Incorrect security pin!")
            return redirect('confirmtransfer')

    return render(request, "users/confirm_transfer.html", transfer_data)

def successful(request):

    receipt = request.session.get('transfer_receipt', {})
    return render(request, "users/successful.html", receipt)

@login_required(login_url='home')
def deposit(request):
    return render(request, 'users/deposit.html')

@login_required(login_url='home')
def spending(request):
    return render(request, 'users/spending.html')
