import pywhatkit as kit
import datetime
now = datetime.datetime.now()
a=int(input("after how many hours you want to send a message "))
b=int(input("after how many minutes you want to send a message"))
a = a + datetime.hours
b = b + datetime.minutes
try:
    kit.sendwhatmsg("+919*********","your message content here",a,b)
except:
    print("an unexpected error occurred")