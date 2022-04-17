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
time = "12:00"
eventlist = []
class Event:
    def __init__(self, name, time, day = None, description = None):
        self.name = name
        self.day = day
        self.time = time
        self.description = description
def addEvent(name, time, day = None, description = None):
   if day == None and description == None:
      eve = Event(name, time)
   elif day == None:
      eve = Event(name, time, None ,description)
   elif description == None:
      eve = Event(name, time, day)
   else:
      eve = Event(name, time, day, description)
e1 = Event("Breakfast", "10:00:00")
eventlist.append(e1)
e2 = Event("Lunch", "01:00:00")
eventlist.append(e2)
e3 = Event("Dinner", "07:00:00")
eventlist.append(e3)

print(e1.name)

