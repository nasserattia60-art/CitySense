
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def home(request):
  page = loader.get_template('home.html')
  cont={
    'file_css':"home.css",
    'file_js':"home.js"
   }
 
  return HttpResponse(page.render(cont,request))


def about(request):
  page =loader.get_template('about.html')
  return HttpResponse(page.render())
  

  