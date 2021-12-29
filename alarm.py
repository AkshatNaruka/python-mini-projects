from datetime import datetime
from playsound import playsound
alarm_time = input("enter when to set the alarm in format :HH::MM::SS\n")
alarm_hour = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting alarm..")
while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_second=now.strftime("%S")
    current_period=now.strftime("%p")
    if(alarm_period==current_hour):
        if(alarm_hour==current_hour):
            if(alarm_minutes==current_minute):
                if(alarm_seconds==current_second):
                    print("Wake Up....")
                    playsound('alarm_audio.mp3')
                    break