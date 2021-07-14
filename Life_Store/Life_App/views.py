from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from Life_Store import settings
from PIL import Image,ImageDraw,ImageFont
from Life_App.models import details
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth import login,authenticate
from . forms import*

# Create your views here.

def index(request):
	return render(request,"page/index.html")

def lifestyle(request):
	return render(request,"page/lifestyle.html")

def login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["pass"]
		user= authenticate(email=email,password=password)
		if user is not None :
			login(request,user)
			return redirect('afterlog')

		return redirect("afterlog")
	return render(request,"page/login.html")

def signup(request):
	if request.method=="POST":
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		phone=request.POST["phone"]
		age=request.POST["age"]
		dob=request.POST["dob"]
		address=request.POST["address"]
		email=request.POST["email"]
		pass1=request.POST["pass"]
		repass1=request.POST["repass"]

		data_db_table = details( fname= fname,lname= lname,phone_num= phone,age= age,dob=dob,address=address,email= email,password=pass1,re_password=repass1)

		data_db_table.save()

		data={"fname": fname,"lname": lname,"phone_num": phone,"age": age,"dob":dob,"address":address,"email":email,"password":pass1,"re_password":repass1}
		return render(request,"page/afterlog.html")

	return render(request,"page/signup.html")
def cameras(request):
	return render(request,"page/cameras.html")

def cart(request):
	return render(request,"page/cart.html")

def change(request):
	data=details.objects.get(email)
	if request.method=="POST":
		data.password=request.POST["npass"]
		data.re_password=request.POST["repass"]
		data.save()
		return redirect("afterlog")
	return render(request,"page/change.html")	

def children(request):

	return render(request,"page/children.html")	

def cre_deb(request):
	return render(request,"page/cre_deb.html")	

def discount(request):
	return render(request,"page/discount.html")	

def netbank(request):
	return render(request,"page/netbank.html")	

def others(request):
	return render(request,"page/others.html")	

def contin(request):
	return render(request,"page/contin.html")

def afterlog(request):
	return render(request,"page/afterlog.html")

def concart(request):
	return render(request,"page/concart.html")

def payment(request):
	return render(request,"page/payment.html")

def phone(request):
	return render(request,"page/phone.html")

def shirt(request):
	return render(request,"page/shirt.html")

def success(request):
	return render(request,"page/success.html")

def watches(request):
	return render(request,"page/watches.html")



