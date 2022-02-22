
from django.shortcuts import render,redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests import get
# Create your views here.








def index(request):
    return render (request , "temp/index.html" )





