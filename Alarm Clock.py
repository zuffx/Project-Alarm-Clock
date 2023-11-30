import time
import datetime
import winsound

alarm_time = input("Enter the alarm time in HH:MM format: ")

alarm_hour, alarm_minute = alarm_time.split(":")
alarm_datetime = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, int(alarm_hour), int(alarm_minute))

time_to_alarm = alarm_datetime - datetime.datetime.now()

if time_to_alarm.total_seconds() <= 0:
    print("Wake up!")
    winsound.Beep(1000, 1000)
else:
    
    time.sleep(time_to_alarm.total_seconds())

    winsound.Beep(1000, 1000)
    print("Wake up!")
