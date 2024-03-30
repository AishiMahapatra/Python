coursenumber_roomnumber = {'CSC101': 3004,'CSC102':4501, 'CSC103':6755, 'NET110':1244, 'COM241':1411 }
coursenumber_instructor = {'CSC101': 'Haynes', 'CSC102':'Alvarado','CSC103':'Rich', 'NET110':'Burke', 'COM241':'Lee'}
coursenumber_meetingtime ={'CSC101':'8:00am', 'CSC102':'9:00am', 'CSC103':'10:00am', 'NET110':'11:00am', 'COM241':'1:00pm'}

def find_roomnumber(coursequery):
    if coursequery in coursenumber_roomnumber :
           print ('roomnumber is', coursenumber_roomnumber[coursequery])
           
def find_instructor(coursequery):
    if coursequery in coursenumber_instructor :
           print ('instructor is', coursenumber_instructor[coursequery])
           
def find_meetingtime(coursequery):
    if coursequery in coursenumber_instructor :
           print ('meeting time is', coursenumber_meetingtime[coursequery])
               
        
coursequery = str(input('Enter a course number'))
find_roomnumber(coursequery)
find_instructor(coursequery)
find_meetingtime(coursequery)
