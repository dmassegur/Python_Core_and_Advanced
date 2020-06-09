import smtplib  # allows to send out emails
from email.mime.text import MIMENonMultipart  # for the body of the email
from email.mime.text import MIMEText

body = 'This is a test email. how are you.'

# compose the email
msg = MIMEText(body)
msg['From'] = 'dmassegur@gmail.com'
msg['To'] = 'dmassegur@hotmail.com'
msg['Subject'] = 'python test'

# create a secure connection to the 'from' email server
server = smtplib.SMTP('smtp.gmail.com',587) # port 587 is the default port
server.starttls()  # starts/enables a secure connection

# login and pwd to your email account
server.login('dmassegur@gmail.com','ferrsch1269')

# send the message
server.send_message(msg)

print('Email sent!')

server.quit()  # instead of close