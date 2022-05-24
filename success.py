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
        print("proceed")
    else:
        from mail import  *
        send_mail(content2,subject2) 
else:
    from mail import *
    send_mail(content1,subject1)
