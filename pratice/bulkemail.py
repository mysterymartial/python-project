
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("bolasax16@gmail.com","Mystery@ sax")
server.sendmail("bolasax16@gmail.com","olasoyinmiracle@gmail.com","hello world")
print("mail sent")