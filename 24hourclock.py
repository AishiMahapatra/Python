current_hours = int(input('Enter current time in hours (in 24 hour format): '))
wait_hours = int(input('Enter number of hours to wait for the alarm:'))
alarm_hours = current_hours + wait_hours%24
print ('Alarm hours',alarm_hours)
    
