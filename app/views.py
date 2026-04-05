from django.shortcuts import render,redirect,HttpResponse
from .models import Acc_details
from .forms import Acc_creationForm
from django.core.mail import send_mail
from django.conf import settings
from .utils.otp import otp
from hashlib import sha256
# Create your views here.
def index(request):
    return render(request,'index.html')
def acc_creation(request):
    form1 = Acc_creationForm()
    context = {'form':form1}
    if request.method == 'POST':
        form = Acc_creationForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                mail = form.cleaned_data['email']
                acc = form.save()
                send_mail(f'Account Created {acc.first_name}',f'Your account number is {acc.acc_number}',settings.EMAIL_HOST_USER,[mail])
                return redirect('index')
            except Exception as e:
                request.session['exception']= str(e)
                print('yes')
                return redirect('error')
        else:
            request.session['exception']= form.errors
            return redirect('error')

    return render(request,'acc_creation.html',context)

def pin_generation(request):
    if request.method == 'POST':
        try:
            acc_number = request.POST.get('acc_number')
            mail = request.POST.get('email')
            acc = Acc_details.objects.get(acc_number=acc_number)
            o = otp()
            request.session['otp'] = o
            request.session['acc_number'] = acc_number
            send_mail('do not send otp',f'your otp is : {o}',settings.EMAIL_HOST_USER,[mail],fail_silently=True)
            return redirect('pin_generation2')
        except Exception as e:
            request.session['exception']= str(e)
            return redirect('error')

    return render(request,'pin_generation.html')


def pin_generation2(request):
    if request.method == 'POST':                                             
        pin = request.POST.get('pin')
        c_pin = request.POST.get('c_pin')
        if request.session.get('otp') == int(request.POST.get('otp')):
            if pin == c_pin:
               acc = Acc_details.objects.get(acc_number=request.session.get('acc_number'))
               acc.pin = pin
               acc.save()
               return redirect('index')
            else:
                request.session['exception']= 'pin mismatch try again latter'
                return redirect('error')
        else:
            request.session['exception']= 'otp mismatch try again latter'
            return redirect('error')
    return render(request,'pin_generator2.html')

def check_balance(request):
    if request.method == 'POST':                                             
        acc_number = request.POST.get('acc_number')
        pin = request.POST.get('pin')
        acc = Acc_details.objects.get(acc_number=acc_number)
        if acc.pin == pin:
            request.session['balance'] = (f'your account balance is : {acc.balance}')
            return redirect('balance')
    return render(request,'check_balance.html')


def deposit(request):
    if request.method == 'POST':                                             
        acc_number = request.POST.get('acc_number')
        pin = request.POST.get('pin')
        amount = int(request.POST.get('amount'))
        acc = Acc_details.objects.get(acc_number=acc_number)
        if acc.pin == pin:
            balance = acc.balance
            acc.balance = balance + amount
            acc.save()
            return redirect('index')
        else:
            request.session['exception']= 'pin is incorrect try again latter'
            return redirect('error')
    return render(request,'deposit.html')


def withdraw(request):
    if request.method == 'POST':                                             
        acc_number = request.POST.get('acc_number')
        pin = request.POST.get('pin')
        amount = int(request.POST.get('amount'))
        acc = Acc_details.objects.get(acc_number=acc_number)
        if acc.pin == pin:
            balance = acc.balance
            acc.balance = balance - amount
            acc.save()
            return redirect('index')
        else:
            request.session['exception']= 'pin is incorrect try again latter'
            return redirect('error')
    return render(request,'withdraw.html')


def transfer(request):
    if request.method == 'POST':                                             
        acc_number = request.POST.get('acc_number')
        t_acc_number = request.POST.get('t_acc_number')
        pin = request.POST.get('pin')
        amount = int(request.POST.get('amount'))
        acc = Acc_details.objects.get(acc_number=acc_number)
        if acc.pin == pin:
            try:
                t_acc = Acc_details.objects.get(acc_number=t_acc_number)
                t_balance = t_acc.balance
                balance = acc.balance
                t_acc.balance = t_balance + amount
                acc.balance = balance - amount
                acc.save()
                t_acc.save()
                return redirect('index')
            except Exception as e:
                request.session['exception']= str(e)
                return redirect('error')
        else:
            request.session['exception']= 'pin is incorrect try again latter'
            return redirect('error')
    return render(request,'transfer.html')

def bal(request):
    msg = request.session.get('balance')
    context = {'msg':msg}
    return render(request,'bal.html',context)

def err(request):
    msg = request.session.get('exception')
    context = {'msg':msg}
    return render(request,'error.html',context)
