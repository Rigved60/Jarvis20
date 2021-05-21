import datetime
from playsound import playsound
import pyttsx3 as py



E=py.init()
E.setProperty("RATE",30)
E.say("Type here for what do you want Alarm? ")
E.runAndWait()
act = str(input("for what do you want Alarm? :- "))
E.say("Type the time! ")
E.runAndWait()
alarmH =input("Enter the time:- ")
print("Alarm has been set for ", alarmH)
E.say(alarmH)
E.runAndWait()

while True:
    Time_Ac = datetime.datetime.now()
    now = Time_Ac.strftime("%H:%M")

    if now == alarmH:
        print("time to ", act)
        E.say(act)
        E.runAndWait()
        playsound("C:\Rigved\python\Python sounds. JARVIS\Alarm.mp3")


    elif now>alarmH:
        break