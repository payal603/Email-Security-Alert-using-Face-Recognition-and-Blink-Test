
from tkinter import *

def printMessage(message):
    root = Tk()
    root.geometry("300x200")
    
    w = Label(root, text ='Result', font = "40") 
    w.pack()
        
    msg = Message( root, text = message)  
        
    msg.pack()  
    
    root.mainloop() 


from recognition import *
from recognition import reco
from recognition import name
content1="An unknown face was detected  "
content2="An suspicious face recognition of "+name+" "
subject1=" Unknown Face Detected at "
subject2=" Suspicious Face Recognition of  "+name+" "

if reco==1:
        from blink import *
        from blink import blink
        if blink==1:
            printMessage("You have passed the blinking test....proceed")
        else:
            from mail import  *
            send_mail(content2,subject2) 
            printMessage("Blinking test failed..Access denied")
else:
    from mail import *
    send_mail(content1,subject1)
