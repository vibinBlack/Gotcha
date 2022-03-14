import pandas as pd

class vehicle:
    def __init__(self,owner,kind,name,number,intime,outime,charges):
        self.owner = owner
        self.kind = kind
        self.name = name
        self.number = number
        self.intime = intime
        self.outime = outime
        self.charges = charges
    def description(self,milage,capacity,manufacturer,fueltype):
        self.milage = milage
        self.capacity = capacity
        self.manufacturer = manufacturer
        self.fueltype = fueltype
    def dimensions(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height


class lot:
    def __init__(self,series,slots,occupancy):
        self.series = series
        self.slots = slots
        self.occupancy = occupancy
        
    def dimensions(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

def parker(A,B,C,D,vehicle):
    count = 0
    serial = 0
    index = 0
    if vehicle == 'Car':
        if count == 0 and A.count(vehicle)<6:
            for i in range(len(A)):
                if A[i] == 0:
                    A[i] = vehicle
                    count = 1
                    serial = "A"
                    index = i
                    break
        elif count == 0:
            print("The 60% of lot A is full of cars \nGo to lot B")
        if count == 0 and B.count(vehicle)<6:
            for i in range(len(B)):    
                if B[i] == 0:
                    B[i] = vehicle
                    count = 1
                    serial = "B"
                    index = i
                    break
        elif count == 0:
            print("The 60% of lot B is full of cars \nGo to lot C")
        if count == 0 and C.count(vehicle)<6:
            for i in range(len(C)):    
                if C[i] == 0:
                    C[i] = vehicle
                    count = 1
                    serial = "C"
                    index = i
                    break
        elif count == 0:
            print("The 60% of lot C is full of cars \nGo to lot D")
        if count == 0 and D.count(vehicle)<6:
            for i in range(len(D)):    
                if D[i] == 0:
                    D[i] = vehicle
                    count = 1
                    serial = "D"
                    index = i
                    break
        elif count == 0:
            print("The 60% of lot D is full of cars \n NO MORE CARS CAN BE PARKED")
            
    elif vehicle == "Bike":
        if count == 0 and A.count(vehicle)<3:
            for i in range(len(A)):
                if A[i] == 0:
                    A[i] = vehicle
                    count = 1
                    serial = "A"
                    index = i
                    break
        elif count == 0:
            print("The 30% of lot A is full of bikes \nGo to lot B")
        if count == 0 and B.count(vehicle)<3:
            for i in range(len(B)):    
                if B[i] == 0:
                    B[i] = vehicle
                    count = 1
                    serial = "B"
                    index = i
                    break
        elif count == 0 :
            print("The 30% of lot B is full of bikes \nGo to lot C")
        if count == 0 and C.count(vehicle)<3:
            for i in range(len(C)):    
                if C[i] == 0:
                    C[i] = vehicle
                    count = 1
                    serial = "C"
                    index = i
                    break
        elif count == 0 :
            print("The 30% of lot C is full of bikes \nGo to lot D")
        if count == 0 and D.count(vehicle)<3:
            for i in range(len(D)):    
                if D[i] == 0:
                    D[i] = vehicle
                    count = 1
                    serial = "D"
                    index = i
                    break
        elif count == 0 :
            print("The 30% of lot D is full of bikes \n NO MORE BIKES CAN BE PARKED")
            
    elif vehicle == 'Bus':
        if count == 0 and A.count(vehicle)<1:
            for i in range(len(A)):
                if A[i] == 0:
                    A[i] = vehicle
                    count = 1
                    serial = "A"
                    index = i
                    break
        elif count == 0 :
            print("The 10% of lot A is filled with buses \nGo to lot B")
        if count == 0 and B.count(vehicle)<1:
            for i in range(len(B)):    
                if B[i] == 0:
                    B[i] = vehicle
                    count = 1
                    serial = "B"
                    index = i
                    break
        elif count == 0 :
            print("The 10% of lot B is filled with buses \nGo to lot C")
        if count == 0 and C.count(vehicle)<1:
            for i in range(len(C)):    
                if C[i] == 0:
                    C[i] = vehicle
                    count = 1
                    serial = "C"
                    index = i
                    break
        elif count == 0 :
            print("The 10% of lot C is filled with buses \nGo to lot D")
        if count == 0 and D.count(vehicle)<1:
            for i in range(len(D)):    
                if D[i] == 0:
                    D[i] = vehicle
                    count = 1
                    serial = "D"
                    index = i
                    break
        elif count == 0 :
            print("The 10% of lot D is filled with buses")
            print("NO MORE BUSES CAN BE PARKED")
        
    return [A,B,C,D],serial, index

def covert(li):              #li consists time in hr:min
    for i in range(len(li)):
    #print(i)
        j = li[i].split(':')
        item1 = int(j[0])
        item2 = int(j[1])
        item = item1*60 + item2 
        li[i] = int(item) 
    return li[0] , li[1]

def charge(duration):
    amt = 0
    if duration <= 60:
        amt += 20
    elif duration > 60 and duration <= 660:
        duration -= 60
        amt += 20
        if duration%60 < 30:
            amt += (duration//60)*10
        elif duration%60 >= 30:
            amt += (duration//60 + 1)*10
    elif duration > 660:
        amt += 120
        duration -= 660
        if duration%60 < 30:
            amt += (duration//60)*5
        elif duration%60 >= 30:
            amt += (duration//60 + 1)*5
    return amt

A = [0,0,0,0,0,0,0,0,0,0]
B = [0,0,0,0,0,0,0,0,0,0]
C = [0,0,0,0,0,0,0,0,0,0]
D = [0,0,0,0,0,0,0,0,0,0]
owner = list()
kind = list()
name = list()
number = list()
intime = list()
outtime = list()
charges = list()
ser = list()
series = [A,B,C,D]

obj_lot = lot(series,len(A),0)
obj_lot.dimensions(14,4,4)
print(obj_lot.length)
print(obj_lot.width)
print(obj_lot.height)

obj_veh = [0 for i in range(len(A)*len(series))]
vehnums = [A,B,C,D]
f = 0
c = 0
index = 0
edic = {}
run = int(input("Welcome to Parking lot: Enter 1 : "))
while run:
    inp = int(input("1 for Parking  2 for Departure :"))
    if inp == 1:
        vehicle_owner = str(input("Enter the vehicle's owner: "))
        vehicle_kind = str(input("Enter the kind of vehicle: "))
        vehicle_name = str(input("Enter the name of vehicle: "))
        vehicle_number = str(input("Enter the vehicle number: "))
        vehicle_intime = str(input("Enter the intime for parking: "))
            #vehicle_milage = str(input("Vehicle's milage: "))
            #vehicle_capacity = str(input("Vehicle's capacity is: "))
            #vehicle_manufacturer = str(input("Vehicle is manufactured by: ")
        if vehicle_kind == 'Bus':
                #vehicle_fuel = str(input("Enter the vehicle's fuel type: "))
            vehicle_length = int(input("Enter the length of vehicle: "))
            vehicle_width = int(input("Enter the width of vehicle: "))
            vehicle_height = int(input("Enter the height of vehicle: "))
        obj_veh[c] = vehicle(vehicle_owner,vehicle_kind,vehicle_name,vehicle_number,vehicle_intime,"None","None")
        owner.append(obj_veh[c].owner)
        kind.append(obj_veh[c].kind)
        number.append(obj_veh[c].number)
        name.append(obj_veh[c].name)
        intime.append(obj_veh[c].intime)
        outtime.append(obj_veh[c].outime)
        charges.append(obj_veh[c].charges)
        
        
        if obj_veh[c].kind == "Bus":
            obj_veh[c].dimensions(vehicle_length,vehicle_width,vehicle_height)
            if obj_veh[c].length >= obj_lot.length or obj_veh[c].width >= obj_lot.width or obj_veh[c].height >= obj_lot.height:
                print("Your vehicle can't be parked as your vehicle size exceeds the parking lot size")
                continue
            else:
                series, serial, index = parker(A,B,C,D,obj_veh[c].kind)
                ser.append(serial)
        else:
            series, serial, index = parker(A,B,C,D,obj_veh[c].kind)
            print(serial)
            ser.append(serial)
        if serial == 'A':
            f = 0
        elif serial == 'B':
            f = 1
        elif serial == 'C':
            f = 2
        elif serial == 'D':
            f = 3
        vehnums[f][index] = obj_veh[c].number
        edic = { "Vehicle's Owner": owner, "Customer's Vehicle": kind, "Vehicle Number": number, "Vehicle Name":name, "Intime":intime, "Series": ser, "Outime": outtime,"Parking Charges": charges}    
        edf = pd.DataFrame(edic)
        edf.to_csv("/home/vinay/Gotcha/ParkingLot/Parking.csv", index=False)
        c += 1
        print(series)
    elif inp == 2:
        outime = str(input("Enter the outime of the customer :"))
        print(vehnums)
        veh_num = str(input("Enter your vehicle number for generation of parking fee:"))
        k = 0
        for i in range(len(vehnums)):
            if vehnums[i] == veh_num:
                k = i
        li = [obj_veh.intime, outime]
        intime , outime = covert(li)
        duration = outime - obj_veh
        #print(duration)
        amt = charge(duration)
        obj_veh[k].charges = amt
        rdic = { "Vehicle's Owner": owner, "Customer's Vehicle": kind, "Vehicle Number": number, "Vehicle Name":name, "Intime":intime, "Series": ser, "Outime": outime, "Parking Charges": amt }
        rdf = pd.DataFrame(edic)
        rdf.to_csv("/home/vinay/Gotcha/ParkingLot/Departure.csv", index=False)
        obj_veh[k] = 0 
        b = 0
        if k > 10:
            while k > 10:
                b += 1 
                k -= 10 
                    #print(b)
                    #print(k-1)
        series[f][index] = 0
        c -= 1
        print(f"The parking charges for {veh_num} is : {amt}")
        
        print(series)
    dic = { 'series A': series[0], 'series B': series[1], 'series C': series[2], 'series D': series[3]  }
    mdf = pd.DataFrame(dic)
    mdf.to_csv("/home/vinay/Gotcha/ParkingLot/Lot.csv", index=False)
    exit_ = int(input("Want to exit of the program :"))
    if exit_ == 1:
        break


            




    