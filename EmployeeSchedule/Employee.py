# importing csv module
import pandas as pd

def update(upemp, upans):
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
        return upemp


def meeting(memp, ech):
    mli = list()
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
        mli.append([a1,q2])
    elif q1 == a1 and a2 < q2:
        mli.append([a1,a2])
    elif q1 == a1 and q2 <  a2:
        mli.append([a1,q2])
    elif q1 < a1 < q2 and q2 == a2:
        mli.append([a1,a2])
    elif q1 < a1 < q2 and q2 < a2:
        mli.append([a1,q2])
    elif q1 < a1 < q2 and a2 < q2:
        
        mli.append([a1,a2])
    #print(li)
    return mli


def meetingscheduler(emp1,emp2,meetime):
    #print(emp1)
    #print(emp2)
    #print(meetime)
    #finding possible time intervals to schedule for emp1 and emp2
    dupli_final = list()
    final = list()
    last = list()
    for i in emp2:
        dupli_final.extend(meeting(emp1,i))
    for j in emp1:
        dupli_final.extend(meeting(emp2,j))
    dupli_final.sort()
    #print(dupli_final)
    for i in dupli_final:
        if i not in final:
            final.extend([i])
    #print(final)         #The final possible time intervals to schedule meeting
    
    durations = list()                   #finding the durations of time intervals
    for item in final:
        durations.append(item[1]-item[0])
    #print(durations)              #the possible durations for meeting
    ms_index = -1
    for i in range(len(durations)):
        if durations[i] >= meetime:
            ms_index = i
            break
    if ms_index == -1:
        return -1
    if durations[ms_index] > meetime:
        last = [final[ms_index][0],final[ms_index][0]+meetime]
    elif durations[ms_index]==meetime:
        last = final[ms_index]
    return last

'''
empid       in-time    break   back           out-time  
emp1          09:00    13:00  14:00            18:00       
emp2          10:00    13:30  14:30           18:30        
emp3          09:30    13:00  14:00           18:30       
emp4          10:20    14:00  15:00            18:30    

empid       in-time    break   back           out-time  
emp1          10:30    13:00  14:00            18:00       
emp2          10:00    12:00  13:00           17:00        
emp3          09:00    13:00  14:00           18:00       
emp4          09:30    12:30  13:30           18:30        
emp5          09:20    11:40  12:30           17:30
'''

def covert(cli):
    for i in range(len(cli)):
    #print(i)
        j = cli[i].split(':')
        item1 = int(j[0])
        item2 = int(j[1])
        item = item1*60 + item2 
        cli[i] = item 
    return cli




# reading csv file
ddf = pd.read_csv("C:/Users/Vinay Muthangi/Gotcha/EmployeeSchedule/EmployeeMeetingScheduler.csv")
#print(df)
Allmeets = list()
Allhosts = list()
Allattendees = list()

empname = ddf['Employee Name:'].to_list()

empid = ddf['Employee ID'].to_list()
#print(empid)

intime = ddf['In-Time'].to_list()
intime = covert(intime)
#print(intime)

breakt = ddf['Break'].to_list()
breakt = covert(breakt)
#print(breakt)

backt = ddf['Back'].to_list()
backt = covert(backt)
#print(backt)

outime = ddf['Out-Time'].to_list()
outime = covert(outime)
#print(outime)

n = len(empid)
emp_sch = list()
for i in range(len(empid)):
    emp_sch.append([[intime[i],breakt[i]],[backt[i],outime[i]]])
#print(emp_sch)
urcal = 1 
while urcal:
    cmp_emp1 = int(input("Meeting to schedule between empno:"))
    cmp_emp2 = int(input("and empno:"))
    meet_hrs = input("Meet in hrs : ")
    meet_hrs = meet_hrs.split(':')
    t1 = int(meet_hrs[0])
    t2 = int(meet_hrs[1])
    meet = int(t1*60 + t2)
    #print(meet)
    i = cmp_emp1 -1
    j = cmp_emp2 -1

    emp1 = emp_sch[i]
    emp2 = emp_sch[j]
    #print(emp1)
    #print(emp2)
    meetset = meetingscheduler(emp1,emp2,meet)
    #print(meetset)
    
    #print(df)

    
    #print(SchTime)

    if meetset == -1:
        print("The meeting is not possible.")
        urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))
        continue
    else:
        df = pd.DataFrame({'duration': meetset})
        f_df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
        SchTime = f_df.values.tolist()
        print("The meeting is scheduled for between : ", SchTime)
    confirm = int(input("Confirm the Meeting: \n Enter 1 for YES or 0 for NO :\n"))
    if confirm:
        print("Meeting is Successfully scheduled")
        Allmeets.append(SchTime)
        Allhosts.append(empname[i])
        Allattendees.append(empname[j])
        
        dic = {'Meet Time': Allmeets , 'Host' : Allhosts, 'Attendee': Allattendees}
        mdf = pd.DataFrame(dic)
        mdf.to_csv("C:/Users/Vinay Muthangi/Gotcha/EmployeeSchedule/Meeting.csv", index=False)
    #update employees free time 
    
        emp_sch[i] = update(emp1,meetset)
        emp_sch[j] = update(emp2,meetset)

    #print(emp_sch)
        
    
    urcal = int(input("Want to schedule another meeting \n Enter 0 or 1 : \n"))
