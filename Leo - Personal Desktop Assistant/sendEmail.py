# #import smtplib
# #def sendEmail(to, content):
#  #   server = smtplib.SMTP('smtp.gmail.com', 587)
#   #  server.ehlo()
#    # server.starttls()

#     # Enable low security in gmail
#     server.login('email', 'password')
#     server.sendmail('email', to, content)
#     server.close()

# import smtplib
# import config
# from email.message import EmailMessage
# #from decouple import config
# EMAIL = config("EMAIL")
# PASSWORD = config("PASSWORD")


# def sendEmail(receiver_address, subject, message):
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_address
#         email["Subject"] = subject
#         email['From'] = EMAIL
#         email.set_content(message)
#         s = smtplib.SMTP("smtp.gmail.com", 587)
#         s.starttcls()
#         s.login(EMAIL, PASSWORD)
#         s.send_message(email)
#         s.close()
#         return True
#     except Exception as e:
#         print(e)
