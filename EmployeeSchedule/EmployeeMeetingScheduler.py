# importing csv module
#pandas is used to extract csv file and print into new csv
import pandas as pd

#Function to update the employee timings.
#removing the meet schedule from employee work time.
def update(upemp, upans):            # (upemp - Host/Attendee) and (upans - Meetime) 
    upemp.sort()
    #print(upemp)
    upstart = upans[0]
    upend = upans[1]
    upduration = upend - upstart
    upfirsts = list()
    updurations = list()
    for i in upemp:
        updurations.append(i[1]-i[0])
    for i in upemp:
        upfirsts.append(i[0])
    #print(firsts)
    upindex = 0
    for i in range(len(upemp)):
        if upemp[i][0] <= upstart:
            upindex = i
    upque = upemp.pop(upindex)
    #print(que)
    #print(ans)
    if updurations[upindex] < upduration:
        return -1
    else:
        upq1 = upque[0]
        upq2 = upque[1]
        upa1 = upans[0]
        upa2 = upans[1]
        if upq1 < upa1 and upa2 < upq2:
            upemp.append([upq1,upa1])
            upemp.append([upa2,upq2])
        elif upq1 < upa1 and upa2 == upq2:
            upemp.append([upq1,upa1])
        elif upq1 == upa1 and upa2 < upq2:
            upemp.append([upa2,upq2])
        elif upq1 == upa1 and upa2 == upq2:
            pass
        upemp.sort()
        return upemp                 #returns updated Host/Attendee, removing the meet schedule

#function to find all possible common intervals between employees
def meeting(memp, ech):   #(memp - Host) and (ech - each of Attendee) >vice-versa<
    li = list()
    memp.sort()  
    #print(memp)
    start = ech[0]
    end = ech[1]
    
    #duration = end - start
    firsts = list()
    for i in memp:
        firsts.append(i[0])
    #print(firsts)
    index = 0
    for i in range(len(memp)):
        if memp[i][0] <= start:
            index = i
    que = memp[index]
    #print(start)
    #print(que)
    #print(ech)
    #if durations[index] < duration:
     #   return -1
    q1 = que[0]
    q2 = que[1]
    a1 = ech[0]
    a2 = ech[1]
    
    if q1 == a1 and q2 == a2:
        li.append([a1,q2])
    elif q1 == a1 and a2 < q2:
        li.append([a1,a2])
    elif q1 == a1 and q2 <  a2:
        li.append([a1,q2])
    elif q1 < a1 < q2 and q2 == a2:
        li.append([a1,a2])
    elif q1 < a1 < q2 and q2 < a2:
        li.append([a1,q2])
    elif q1 < a1 < q2 and a2 < q2:
        li.append([a1,a2])
    #print(li)
    return li


def meetingscheduler(emp1,emp2,meetime):   #(Host - emp1)   (Attendee - emp2)  (meetime in minutes ex- 120)
    #print(emp1)
    #print(emp2)
    #print(meetime)
    #finding possible time intervals to schedule for Host and Attendee
    dupli_final = list() #list to store all possible time intervals between Host and Attendee to schedule meet
    final = list()       #list to store all possible time intervals between Host and Attendee to schedule meet
    last = list()        #list to return meet schedule
    for i in emp2:
        dupli_final.extend(meeting(emp1,i)) #meeting
    for j in emp1:
        dupli_final.extend(meeting(emp2,j))
        
    dupli_final.sort()
    #print(dupli_final) #It consists duplicate elements
    for i in dupli_final:
        if i not in final:
            final.extend([i])
    #print(final)           #Duplicates removed
    
    durations = list()                   #list for the durations of time intervals
    for item in final:
        durations.append(item[1]-item[0])
    #print(durations)                    #the possible durations
    ms_index = -1                        #initializing to an unknown index
    for i in range(len(durations)):
        if durations[i] >= meetime:
            ms_index = i                 #index of the possible meet from starting
            break
    if ms_index == -1:
        return -1                         #returns -1, if meet scheduling is not possible
    if durations[ms_index] > meetime:     
        last = [final[ms_index][0],final[ms_index][0]+meetime]
    elif durations[ms_index]==meetime:
        last = final[ms_index]
    return last                       #returns a list of finalised meet schedule ex: [540, 720]

'''
Example : 1
empid       in-time    break   back           out-time  
emp1          09:00    13:00  14:00            18:00       
emp2          10:00    13:30  14:30           18:30        
emp3          09:30    13:00  14:00           18:30       
emp4          10:20    14:00  15:00            18:30    

Example : 2
empid       in-time    break   back           out-time  
emp1          10:30    13:00  14:00            18:00       
emp2          10:00    12:00  13:00           17:00        
emp3          09:00    13:00  14:00           18:00       
emp4          09:30    12:30  13:30           18:30        
emp5          09:20    11:40  12:30           17:30
'''
#function to convert time from hr:min format to 540 format 
def covert(li):              #li consists time in hr:min
    for i in range(len(li)):
    #print(i)
        j = li[i].split(':')
        item1 = int(j[0])
        item2 = int(j[1])
        item = item1*60 + item2 
        li[i] = item 
    return li               #returns li consists time in minutes format






# reading csv file
ddf = pd.read_csv("C:/Users/Vinay Muthangi/Gotcha/EmployeeSchedule/EmployeeMeetingScheduler.csv")
#print(df)
#storing all confirmed meets into Allmeets list
Allmeets = list()
#storing the information of host
Allhosts = list()
#storing the information of attendees
Allattendees = list()

#Extracting EmployeeName into empname
empname = ddf['Employee Name:'].to_list()
#Extracting EmployeeID into empid
empid = ddf['Employee ID'].to_list()
#print(empid)

#Extracting In-Time of all employees into intime
intime = ddf['In-Time'].to_list()
intime = covert(intime)               #converting time hr:min to minutes format ex: 09:00 -> 540
#print(intime)

breakt = ddf['Break'].to_list()
breakt = covert(breakt)               #converting time hr:min to minutes format 
#print(breakt)

backt = ddf['Back'].to_list()
backt = covert(backt)                 #converting time hr:min to minutes format 
#print(backt)

outime = ddf['Out-Time'].to_list()
outime = covert(outime)               #converting time hr:min to minutes format 
#print(outime) 

n = len(empid)                        #Number of employees 
emp_sch = list()                      #List of all employee schedules  
for i in range(len(empid)):
    emp_sch.append([[intime[i],breakt[i]],[backt[i],outime[i]]])
#print(emp_sch)
urcal = int(input("Want to schedule meeting \n Enter 0 or 1 : \n"))                             #To schedule a meet or not
while urcal:
    print("\nKnow your Staff")
    print(''' 1 for Vinay        7 for Hari sir \n 2 for Nagaraju     8 for Ram \n 3 for Shyam        9 for Pawan \n 4 for Prashanth    10 for Sravanthi \n 5 for Irfan        11 for Aditya \n 6 for Sharma sir   12 for Deepthi''')
    print()
    cmp_emp1 = int(input("Meeting to schedule between Host:"))    #Host 
    cmp_emp2 = int(input("and Attendee:"))                            #Attendee
    meet_hrs = input("Meet in hrs : ")                             #Meet time in hr:min format
    meet_hrs = meet_hrs.split(':')                                 #storing hrs and mins into a list
    t1 = int(meet_hrs[0])                                          
    t2 = int(meet_hrs[1])
    meet = int(t1*60 + t2)                                         #Meet time in minutes format
    #print(meet)
    i = cmp_emp1 -1                             #to meet actual indicies in list subtracting -1
    j = cmp_emp2 -1                             

    emp1 = emp_sch[i]                           #Host employee time schedule [intime,breakt,backt,outime]
    emp2 = emp_sch[j]                           #Attendee employee time schedule [intime,breakt,backt,outime]
    #print(emp1)
    #print(emp2)
    #calling meetingscheduler to finalize first possible meet
    #between Host and Attendee from their schedules
    meetset = meetingscheduler(emp1,emp2,meet)    
    #if possible returns the first possible meet schedule between Host Attendee
    #else returns -1
    #print(meetset)

    if meetset == -1:
        print("The meeting is not possible.")   #Meet Not possible
        urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))  #Input for the next meet
        continue  
    else:
        df = pd.DataFrame({'duration': meetset})   #converting the minutes schedule into hours schedule
        f_df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
        SchTime = f_df.values.tolist()       #[540, 720] into 09:00 - 11:00 
        #print(SchTime)
        print("The meeting is scheduled for between : ", SchTime)   
    confirm = int(input("Confirm the Meeting: \n Enter 1 for YES or 0 for NO :\n"))
    #Making the meet confirmation.
    if confirm:
        print("Meeting is Successfully scheduled")      
        Allmeets.append(SchTime)            #Appending final meet schedule into Allmeets
        Allhosts.append(empname[i])         #Appending Host name into Allhosts
        Allattendees.append(empname[j])     #Appending Attendee name into Allattendees
        
        dic = {'Meet Time': Allmeets , 'Host' : Allhosts, 'Attendee': Allattendees} #storing them into a dictionary
        mdf = pd.DataFrame(dic)   #storing dictionary into a dataframe
        mdf.to_csv("C:/Users/Vinay Muthangi/Gotcha/EmployeeSchedule/Meeting.csv", index=False) #writing the dataframe into csv

        #update employees free time
        emp_sch[i] = update(emp1,meetset)
        emp_sch[j] = update(emp2,meetset)

        #print(emp_sch)
    #Input for the next meet
    urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))
