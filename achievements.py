from datetime import datetime

now = datetime.now()

print(datetime.now())

current_time = now.strftime("%H:%M:%S")
hours = int(current_time[0:2])
minutes = int(current_time[3:5])
seconds = int(current_time[6:8])
print("current hour is: ", hours)
print("Current Time is :", current_time)
timeachieved = 0
#if logging in first time reward
#if first acknowledgement reward
#if acknowledged all reminders in the day
#if acknowledge all reminders in the day multiple time
#if acknowledged reminder multiple times reward
#if used site multiple days rewards
#achieved several reminders in one day reward
#