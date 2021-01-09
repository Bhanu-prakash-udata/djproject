from django.shortcuts import render,redirect
from django.http import HttpResponse
from bike import settings
from bikebook.forms import Userreg,Ad,Add
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Addbike
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request,'btm/home.html')

def abt(request):
	return render(request,'btm/about.html')

def regis(request):
	if request.method == "POST":
		f = Userreg(request.POST)
		#print(f)
		if f.is_valid():
			r = f.save()
			rc = r.email
			sb = "message from bikebook.com"
			msg ="thankyou for registering into bikebook.com your username is {} and password is {}".format(r.username,r.password)
			sd = settings.EMAIL_HOST_USER
			sm = send_mail(sb,msg,sd,[rc])
			if(sm==1):
				messages.success(request,"your registration  succefull")
				return redirect('log')
	f = Userreg()
	return render(request,'btm/register.html',{'y':f})

def LoginView(request):
	return render(request,'btm/login.html')

@login_required
def LogoutView(request):
	return render(request,'btm/logout.html')

@login_required
def bookbike(request):
	return render(request,'btm/book.html')

@login_required
def honda(request):
	return render(request,'btm/honda.html')

@login_required
def royal(request):
	return render(request,'btm/royal.html')

@login_required	
def bmw(request):
	return render(request,'btm/bmw.html')

@login_required	
def address(request):
    if request.method == "POST":
    	a = Ad(request.POST)
    	if a.is_valid():
    		p = a.save()
    		rc = p.emailid
    		sb = "message from bikebook.com"
    		msg ="thankyou for booking the bike mr/mrs {} you can pay the cash in bike delivery time, if any doubts call us tollfree:12150 ".format(p.username)
    		sd = settings.EMAIL_HOST_USER
    		sm = send_mail(sb,msg,sd,[rc])
    		if(sm==1):
    			messages.success(request,"your vehicle booked succefully")
    			return render(request,'btm/home.html')
    a = Ad()
    return render(request,'btm/address.html',{'f':a})

def addbike(request):
	if request.method == "POST":
		b = Add(request.POST,request.FILES)
		if b.is_valid():
			b.save()
			# messages.success(request,'bike added')
			return redirect('allbikes')
	else:
		b = Add()
		return render(request,'btm/addbike.html',{'s':b})
def allbike(request):
	data = Addbike.objects.all()
	return render(request,'btm/allbikes.html',{'d':data})

def viewmore(request,id):
	view = Addbike.objects.get(id=id)
	return render(request,'btm/viewmore.html',{'v':view})

def profile(request):
	return render(request,'btm/profile.html')

def allbrands(request):
	brands = Addbike.objects.all()
	return render(request,'btm/allbrands.html',{'b':brands})

def viewbikes(request):
	 return render(request,'btm/viewbikes.html')