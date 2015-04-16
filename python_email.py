import smtplib

user = 'gmail_email'
password = 'password'

receiver = '' # outlook_email, yahoo_email, gmail_email
sender = '' # user

subject  = 'Test Python Send Email'
message = 'Hello, this is a test about use Python to send email, LOL'

smtpserver = smtplib.SMTP("smtp.gmail.com",587) 
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(user, password)
msg = MIMEText(message, _charset="UTF-8")
msg['TO'] = receiver
msg['FROM'] = sender
msg['Subject'] = Header(subject, "utf-8")
smtpserver.sendmail(sender, receiver, msg.as_string())
smtpserver.close()