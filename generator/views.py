from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def password(request):
	
	
	thePassword = ''
	length = request.POST.get('length')
	special = request.POST.get('special')
	numbers = request.POST.get('numbers')
	uppercase = request.POST.get('uppercase')

	characters = list('abcdefghijklmnopqrstuvwxyz')
	UpChar = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	num = list('1234567890')
	spc = list('`!@#$%^&*()_+')
	if uppercase:
		characters.extend(UpChar)
	if numbers:
		characters.extend(num)
	if special:
		characters.extend(spc)
	for x in range(int(length)):
		thePassword += random.choice(characters)
 

	return render(request, 'generator/password.html', {'password':thePassword})	