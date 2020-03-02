from django.shortcuts import render,redirect
from .forms import EmpForm
from main.models import Emp

# Create your views here.
def home_view(request):
	post = Emp.objects.all()
	return render(request,'home.html',{'post':post})

def create_view(request):
	if request.method=='POST':
		form = EmpForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = EmpForm()
	return render(request,'create.html',{'form':form})