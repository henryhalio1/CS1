import time
import datetime

current_time = datetime.datetime(2024, 12, 16, 7, 00, 0)    #sets current time to 7:00 AM      
print(current_time.strftime("%H:%M:%S"))                    #displays current time as hours, minutes, seconds

while True:                                                 #forever loop
   print ("ALARM!")                                         #displays message "ALARM!"
   time.sleep(1)                                            #pauses program for 1 second 
   snooze = str.lower(input("Snooze? y/n:"))                #asks user whether or not they want to snooze
   if snooze == "y":
        print ("Sleep for 5 more minutes")                  #if user inputs "y" displays message "sleep for 9 more minutes"
        current_time += datetime.timedelta(minutes=5)    
        print(current_time.strftime("%H:%M:%S"))            #displays current time as hours, minutes, seconds
   elif snooze == "n":                           
        break                                               #if user inputs "n" breaks forever loop                           
   else:
        print("Invalid Response")                           #if user inputs something else, print "invalid response"

print(current_time.strftime("%H:%M:%S"))                    #displays current time as hours, minutes, seconds
print ("Get up")                                            #displays message "get up"
time.sleep(1)                                               #pauses program for 1 second
print ("Take a shower")                                     #displays message "take a shower"
time.sleep(1)                                               #pauses program for 2 seconds

current_time += datetime.timedelta(minutes=5)
print(current_time.strftime("%H:%M:%S"))                    #displays current time as hours, minutes, seconds
brush_teeth = str.lower(input("brush teeth? y/n:"))         #asks user whether or not they want to brush their teeth

while True:
    if brush_teeth == "n":
        print ("Get Dressed")
        break
    elif brush_teeth == "y":                                #if user inputer "y" display message "brush them"
        print ("Brush them")
        print ("Then, get dressed")                         #displays message "then, get dressed"
        break
    else:
        print("Invalid Response")
    time.sleep(1)                                           #pauses program for 1 second
current_time += datetime.timedelta(minutes=5)
print(current_time.strftime("%H:%M:%S"))                    #displays current time as hours, minutes, seconds


while brush_teeth == "y": 
    cold_outside = str.lower (input("cold outside? y/n:"))  #asks user whether or not it is cold outside
    if cold_outside == "y":                                 #if user inputs "y" displays message "wear pants and sweater
        print ("Wear pants and sweater")
        current_time += datetime.timedelta(minutes=5)
        print(current_time.strftime("%H:%M:%S"))    
        break
    elif cold_outside == "n":                               #if user inputs "n" displays message "wear shorts and button down or sweater"
        print ("Wear shorts and button down or sweater")
        current_time += datetime.timedelta(minutes=5)
        print(current_time.strftime("%H:%M:%S"))    
        break
    else:
        print("Invalid Response")
    time.sleep(1)
current_time += datetime.timedelta(minutes=5)
print(current_time.strftime("%H:%M:%S"))                    #displays current time as hours, minutes, seconds

while brush_teeth == "n":                                   #if the user does not brush their teeth
    cold_outside = str.lower (input("Is it Cold Outside? y/n:"))  #asks user whether or not it is cold outside
    if cold_outside == "y":                                 #if user inputs "y" displays message "wear pants and sweater
        print ("wear pants and sweater")
        current_time += datetime.timedelta(minutes=5)
        print(current_time.strftime("%H:%M:%S"))    
        break
    elif cold_outside == "n":                               #if user inputs "n" displays message "wear shorts and button down or sweater"
        print ("wear shorts and button down or sweater")
        current_time += datetime.timedelta(minutes=5)
        print(current_time.strftime("%H:%M:%S"))    
        break
    else:
        print("Invalid Response")
    time.sleep(1)
    print("Now, brush teeth")
    break


print ("put clothes on")                                    #displays message "put clothes on"
print ("pack bag")                                          #displays message "pack bag"
time.sleep(1)                                               #pauses program for 1 second

while True:
    do_i_have_a_game_today = str.lower (input("do i have a game today? y/n:"))  #asks user whether or not they have a game that day
    if do_i_have_a_game_today == "y":                       #if user inputs "y" displays message "pack jersey in soccer bag"
        print ("pack jersey in soccer bag")
        break
    elif do_i_have_a_game_today == "n":                     #if user inputs "n" displays message "pack stuff for    practice"
        print ("pack stuff for practice")
        break
    else:
        print("Invalid Response")
    time.sleep(1)                                           #pauses the program for 1 second
current_time += datetime.timedelta(minutes=5)
print(current_time.strftime("%H:%M:%S"))                    #displays current time as hours, minutes, seconds

print ("then, go downstairs")                               #displays message "then, go downstairs"

food_in_fridge = str.lower (input("food in fridge? y/n:"))  #asks user whether or not there is food in the fridge

while True:
    if food_in_fridge == "y":                               #if user inputs "y" displays message "eat it"
        print("Eat the food in the fridge")
        break
    elif food_in_fridge == "n":                             #if user inputer "n" displays message eat cheese stick
        print ("Eat a cheese stick and then have breakfast at school")
        break
    else:
        print("Invalid Response")
    time.sleep(1)                                           #pauses the program for 1 second

print(current_time.strftime("%H:%M:%S"), end='\r')          #displays current time

print ("go on phone")                                       #displays message "go on phone"

time.sleep(1)                                               #pauses program for 1 second

print ("put shoes on and get ready to leave")               #displays message "put shoes on and get ready to leave"

current_time = datetime.datetime(2024, 12, 16, 7, 30, 0)    #displays current time
