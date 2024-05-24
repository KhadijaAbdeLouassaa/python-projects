import smtplib
#------------------
print("start...")

from_address = 'from_address@gmail.com'
to_address  = 'to_address@gmail.com'
subject = 'Your subject'
msg = 'Message you need to send'

# get message with subject
message = 'Subject: {}\n\n{}'.format(subject, msg)

useremail = 'youremail@gmail.com'
# don't put your personal password | made a fake password in AppPasswords
password = '**************'
server = smtplib.SMTP('smtp.gmail.com:587')
# start TLS for security
server.starttls()
# authentication
server.login(useremail,password)
server.sendmail(from_address, to_address, message,subject)
# quit the session
server.quit()

print("done.")




