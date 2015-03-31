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
header  = 'To:      ' + receiver + '\n'
header += 'From:    ' + sender + '\n'
header += 'Subject: ' + subject + '\n'
print (header)
msg = header + '\n' + message + ' \n\n'
smtpserver.sendmail(sender, receiver, msg)
smtpserver.close()