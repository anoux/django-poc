from django.http import HttpResponse
from random import randint as ran
from django.shortcuts import render

# Create your views here.

# Osiris: think about views.py as a place that handles my pages
# Osiris: you can have as many vies as you want

def home_view(request, *args, **kwargs): # *args, # **kwargs are python specfic
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "this is about Nadin",
		"my_text": "I am Nadin, 42 years old, backend developer",
		"my_number": 1578657165,
		"my_list": ["vegan", "best decision maker", "professional sailer"],
		"my_html":"<h1>Hello World</h1>" #Check the safe filter in about.html
	} 

	return render(request, "about.html", my_context)

# bwords = ["puta", "trola", "cornudo", "hdp"]
# return render(request, "home.html", { "asd": bwords[ran(0,3)]}) # With this, django returns a template html