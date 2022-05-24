import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

def send_mail(content,subject):
    fromaddr = "payalrgaik@gmail.com"
    toaddr = "payal.gaikwad@cumminscollege.in"
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address  
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr     
    # storing the subject
    now = datetime.datetime.now()   
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    msg['Subject'] = subject+" at date time:"+dt_string
    # datetime object containing current date and time
    
    # string to store the body of the mail
    body = (content+" at date time: "+dt_string)
    # attach the body with the msg instance
    msg.attach(MIMEText(body,'plain'))
    # open the file to be sent
    filename = "test.jpeg"
    attachment = open(r"C:\Users\dell\Downloads\Github projects\god\test.jpeg", "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
                
    # encode into base64
    encoders.encode_base64(p)
                
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
                
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
                
    # start TLS for security
    s.starttls()
                
    # Authentication
    s.login(fromaddr, "harshada")
                
    # Converts the Multipart msg into a string
    text = msg.as_string()
                
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
                
    # terminating the session
    s.quit()                   
                    
                    
                    
                
                    
                
                    
                
                
                        
                
                
                    
                
                    
                
                    
                
                    
    
                
                    
                
                    
                    
                
                    

        