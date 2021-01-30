import smtplib
sender_email="abhaywwe6@gmail.com"
receiver_email="19bcs1704@gmail.com"
password=input("enter your password: ")
message="Sending through python!!!"
s=smtplib.SMTP('smtp.gmail.com',587) #port number
s.starttls()
s.login(sender_email,password)
print("Logged in successfully")
s.sendmail(sender_email,receiver_email,message)
print("Email sent :)")
