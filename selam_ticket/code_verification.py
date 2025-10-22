import smtplib
from django.conf import settings
import random
def OTP_REQUEST(email):
    code = random.randint(000000,999999)
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    reciever_email =email
    subject = "Verification Code From Selam Bus Webpage"
    message = f"Your Verification Code is {code}"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',settings.EMAIL_PORT) as server:
          server.login(sender_email,password)
          server.sendmail(sender_email,reciever_email,f"{subject} /n {message}")
          print("successfuly sends to "+f'{reciever_email}')
    except Exception as e:
       print("error")
    
    return(code)


