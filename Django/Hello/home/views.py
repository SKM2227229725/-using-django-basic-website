from urllib import request
from django.shortcuts import render ,HttpResponce


# Create your views here.
def index ( Request ):
 return render(request, 'index.html')
def index ( Request ):
 return HttpResponce( " Thish  is the home page ")
def about ( Request ):
 return HttpResponce( " Thish  is the about page ")
def services ( Request ):
 return HttpResponce( " Thish  is the services page ")
def contact ( Request ):
 return HttpResponce( " Thish  is the contact page ")
