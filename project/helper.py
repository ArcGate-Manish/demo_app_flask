import math
import smtplib
import os
import random
def generateOTP():
  string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  OTP = ""
  length = len(string)
  print("OTP Generation")
  for i in range(6):
        OTP += string[math.floor(random.random() * length)]

  return OTP


def sendEmail(email_id,otp):
      with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()


            # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.login('arcgatedemoacc@gmail.com', 'imezimfmnrnhnvjx')

            subject = 'Email Verification'
            body = 'This is your OTP: '+ otp


            msg = f'Subject:{subject}\n\n{body}'


            smtp.sendmail('arcgatedemoacc@gmail.com', email_id, msg)
  
  