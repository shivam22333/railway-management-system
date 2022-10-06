from django.shortcuts import render,redirect
from .models import Register,Station,Train,Detail,Contact
from django.contrib.auth.hashers import make_password,check_password
from .forms import RegisterForm,MyPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from random import *
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from RMS import settings
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	if request.method=='POST':
		fm=RegisterForm(request.POST)
		if fm.is_valid():
			email=fm.cleaned_data['email']
			s=User.objects.filter(email=email)
			if s:
				error="Account with this email id already exists"
				return render(request,'register.html',{'fm':fm,'error':error})
			else:
				fm.save()
				return redirect('login')

		else:
			
			return render(request,'register.html',{'fm':fm})
	else:
		fm=RegisterForm()
		return render(request,'register.html',{'fm':fm})

def logins(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('index')
		else:
			error="Invalid Username/Password"
			return render(request,'login.html',{'error':error})
	else:
		return render(request,'login.html')

def logouts(request):
	logout(request)
	return redirect('index')

def contact(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		message=request.POST.get('message')
		Contact.objects.create(name=name,email=email,message=message)
	return render(request,'contact.html')


def route(request):
	if request.method=='POST':
		dest1=request.POST.get('sele')
		dest2=request.POST.get('sel')
		datet=request.POST.get('datet')
		request.session['datet']=datet
		request.session['dest1']=dest1
		request.session['dest2']=dest2
		print(datet)
		if dest1=='Choose' or dest2=='Choose' or datet=='':
			error="Select an correct option"
			a=Station.objects.all()
			return render(request,'route.html',{'error':error,'a':a})
		m=Station.objects.filter(station=dest1)
		n=Station.objects.filter(station=dest2)
		train=Train.objects.filter(dest_1__in=m,dest_2__in=n)
		return render(request,'book_ticket.html',{'train':train})
	else:
		a=Station.objects.all()
		return render(request,'route.html',{'a':a})

def book_ticket(request,t_id,t,s):
	user=request.user
	if request.user.is_authenticated:
		if s<1:
			error="Coach is full"
			m=Station.objects.filter(station=request.session['dest1'])
			n=Station.objects.filter(station=request.session['dest2'])
			train=Train.objects.filter(dest_1__in=m,dest_2__in=n)
			return render(request,'book_ticket.html',{'train':train,'error':error})
		request.session['t_id']=t_id

		request.session['t']=t
		return redirect('pass_Details')
	else:
		return redirect('login')

def pass_detail(request):
    if request.method=='POST':
    	c=0
    	pas1=request.POST.get('pas1')
    	if pas1!="":
    		g1=request.POST.get('g1')
    		age1=request.POST.get('age1')
    		request.session['pas1']=pas1
    		request.session['g1']=g1
    		request.session['age1']=age1
    		c=c+1
    	

    	pas2=request.POST.get('pas2')
    	if pas2!="":
    		g2=request.POST.get('g2')
    		age2=request.POST.get('age2')
    		request.session['pas2']=pas2
    		request.session['g2']=g2
    		request.session['age2']=age2
    		c=c+1

    	pas3=request.POST.get('pas3')
    	if pas3!="":
    		g3=request.POST.get('g3')
    		age3=request.POST.get('age3')
    		request.session['pas3']=pas3
    		request.session['g3']=g3
    		request.session['age3']=age3
    		c=c+1
    		
    	pas4=request.POST.get('pas4')
    	if pas4!="":
    		g4=request.POST.get('g4')
    		age4=request.POST.get('age4')
    		request.session['pas4']=pas4
    		request.session['g4']=g4
    		request.session['age4']=age4
    		c=c+1

    	a=Train.objects.get(id=request.session['t_id'])
    	n=request.session['t']
    	if n=='sc_price':
    		m=a.sc_price*c
    	if n=='third_price':
    		m=a.third_price*c
    	if n=='second_price':
    		m=a.second_price*c
    	if n=='first_price':
    		m=a.first_price*c
    	request.session['m']=m
    	l=request.session['m']
    	d=float(l)+11.80

    	return render(request,'pass_Details.html',{'m':m,'d':d})
    else:
    	
    	return render(request,'pass_Details.html')

def saved(request):
	c=0
	n=request.session['t']
	a=Train.objects.get(id=request.session['t_id'])
	print(a)
	u=Detail()
	u.passenger1=request.session['pas1']
	u.gender1=request.session['g1']
	u.age1=request.session['age1']
	c=c+1
	if n=='sc_price':
		u.seat1=(a.tsc-a.sc)+c
	if n=='third_price':
		u.seat1=(a.tthird_ac-a.third_ac)+c
	if n=='second_price':
		u.seat1=(a.tsecond_ac-a.second_ac)+c
	if n=='first_price':
		u.seat1=(a.tfirst_ac-a.first_ac)+c
	
	if 'pas2' in request.session: 
		u.passenger2=request.session['pas2']
		u.gender2=request.session['g2']
		u.age2=request.session['age2']
		c=c+1
		if n=='sc_price':
			u.seat2=(a.tsc-a.sc)+c
		if n=='third_price':
			u.seat2=(a.tthird_ac-a.third_ac)+c
		if n=='second_price':
			u.seat2=(a.tsecond_ac-a.second_ac)+c
		if n=='first_price':
			u.seat2=(a.tfirst_ac-a.first_ac)+c
	if 'pas3' in request.session: 
		u.passenger3=request.session['pas3']
		u.gender3=request.session['g3']
		u.age3=request.session['age3']
		c=c+1
		if n=='sc_price':
			u.seat3=(a.tsc-a.sc)+c
		if n=='third_price':
			u.seat3=(a.tthird_ac-a.third_ac)+c
		if n=='second_price':
			u.seat3=(a.tsecond_ac-a.second_ac)+c
		if n=='first_price':
			u.seat3=(a.tfirst_ac-a.first_ac)+c
	
	if 'pas4' in request.session: 
		u.passenger4=request.session['pas4']
		u.gender4=request.session['g4']
		u.age4=request.session['age4']
		c=c+1
		if n=='sc_price':
			u.seat4=(a.tsc-a.sc)+c
		if n=='third_price':
			u.seat4=(a.tthird_ac-a.third_ac)+c
		if n=='second_price':
			u.seat4=(a.tsecond_ac-a.second_ac)+c
		if n=='first_price':
			u.seat4=(a.tfirst_ac-a.first_ac)+c
	u.amount=request.session['m']
	u.train=Train.objects.get(id=request.session['t_id'])
	
	if n=='sc_price':
		a.sc=a.sc-c
		u.coach="Sleeper"
		u.coach_train='S1'
		
	if n=='third_price':
		b=a.third_ac-c
		a.third_ac=b
		u.coach="3AC"
		u.coach_train='AS-1'
		
	if n=='second_price':
		a.second_ac=a.second_ac-c
		u.coach="2AC"
		u.coach_train='A-1'
		
	if n=='first_price':
		a.first_ac=a.first_ac-c
		u.coach="1AC"
		u.coach_train='H-1'
		
	a.save()
	u.pnr=randint(1000000000,9999999999)
	request.session['pnr']=u.pnr
	user=request.user
	u.user=user
	u.date=request.session['datet']
	u.save()

	return redirect('delete')

def deletesession(request):
    del request.session['t_id']
    del request.session['t']
    del request.session['pas1']
    del request.session['g1']
    del request.session['age1']
    if 'pas2' in request.session: 
    	del request.session['pas2']
    	del request.session['g2']
    	del request.session['age2']
    if 'pas3' in request.session: 
    	del request.session['pas3']
    	del request.session['g3']
    	del request.session['age3']
    if 'pas4' in request.session: 
    	del request.session['pas4']
    	del request.session['g4']
    	del request.session['age4']
    del request.session['m']
    del request.session['dest1']
    del request.session['dest2']
    del request.session['datet']
    return redirect('transaction')

def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		c=0
		d=0
		a=Detail.objects.get(pnr=request.session['pnr'])
		if a.age1>5:
			d=d+1
		else:
			c=c+1
		if a.age2 is not None:
			if a.age2>5:
				d=d+1
			else:
				c=c+1
		if a.age3 is not None:
			if a.age3>5:
				d=d+1
			else:
				c=c+1
		if a.age4 is not None:
			if a.age4>5:
				d=c+1
			else:
				c=c+1
		b=float(a.amount)+11.80
		data = {'a':a,'b':b,'c':c,'d':d}
		pdf = render_to_pdf('ticket.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		c=0
		d=0
		a=Detail.objects.get(pnr=request.session['pnr'])
		if a.age1>5:
			d=d+1
		else:
			c=c+1
		if a.age2 is not None:
			if a.age2>5:
				d=d+1
			else:
				c=c+1
		if a.age3 is not None:
			if a.age3>5:
				d=d+1
			else:
				c=c+1
		if a.age4 is not None:
			if a.age4>5:
				d=c+1
			else:
				c=c+1
		b=float(a.amount)+11.80
		data = {'a':a,'b':b,'c':c,'d':d}
		pdf = render_to_pdf('ticket.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Ticket.pdf"
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			
			content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not found")
		



def transaction(request):
    c=0
    d=0
    a=Detail.objects.get(pnr=request.session['pnr'])
    print(request.session['pnr'])
    if a.age1>5:
    	d=d+1
    else:
    	c=c+1
    if a.age2 is not None:
	    if a.age2>5:
	    	d=d+1
	    else:
	    	c=c+1
    if a.age3 is not None:
	    if a.age3>5:
	    	d=d+1
	    else:
	    	c=c+1
    if a.age4 is not None:
	    if a.age4>5:
	    	d=c+1
	    else:
	    	c=c+1
    b=float(a.amount)+11.80
    m='Thankyou for using rail reservation facility.Your booking details are indicated below.'
    data = {'a':a,'b':b,'c':c,'d':d,'m':m}
    dat = {'a':a,'b':b,'c':c,'d':d}
    template = get_template('ticket.html')
    html  = template.render(dat)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    pdf = result.getvalue()
    filename = 'Ticket.pdf'
    user=request.user
    c=User.objects.get(username=user)
    
    to=c.email
    subject = 'Ticket Confirmation'
    message='Thankyou for using rail reservation facility.Your booking details are indicated below.'
    template = get_template('ticket.html')
    text_content = template.render(data)
    email = EmailMultiAlternatives(subject,message,settings.EMAIL_HOST_USER,[to])
    email.attach_alternative(text_content, "text/html")
    email.attach(filename, pdf, 'application/pdf')
    email.send(fail_silently=False)
                    
    return redirect('complete')


def pnr(request):
	if request.method=='POST':
		c=0
		d=0
		search=request.POST.get('search')
		try:
			a=Detail.objects.get(pnr=search)
			if a.age1>5:
				d=d+1
			else:
				c=c+1
			if a.age2 is not None:
				if a.age2>5:
					d=d+1
				else:
					c=c+1
			if a.age3 is not None:
				if a.age3>5:
					d=d+1
				else:
					c=c+1
			if a.age4 is not None:
			    if a.age4>5:
			    	d=c+1
			    else:
			    	c=c+1
			b=float(a.amount)+11.80
			data={'a':a,'b':b,'c':c,'d':d}
			return render(request,'pnr.html',{'a':a,'b':b,'c':c,'d':d})
		except:
			error="Enter correct pnr no"
			return render(request,'pnr.html',{'error':error})

	else:
		return render(request,'pnr.html')

def complete(request):
	return render(request,'complete.html')


def change(request):
    if request.method=='POST':
        l=MyPasswordChangeForm(user=request.user,data=request.POST)
        if l.is_valid():
            l.save()
            update_session_auth_hash(request,l.user)
            return redirect('index')
        else:
        	return redirect('change')
    else:
        l=MyPasswordChangeForm(user=request.user)
        return render(request,'change.html',{'l':l})


def about(request):
	return render(request,'about.html')