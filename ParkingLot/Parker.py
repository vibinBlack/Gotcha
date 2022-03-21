import pandas as pd

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

class vehicle:
    def __init__(self,owner,kind,name,number,intime,outime,charges):
        self.owner = owner
        self.kind = kind
        self.name = name
        self.number = number
        self.intime = intime
        self.outime = outime
        self.charges = charges
    def dimensions(self,length,width):
        self.length = length
        self.width = width
        self.area = self.length*self.width

class lot:
    def __init__(self,series, Bus, Bike, Car, leftover):
        self.series = series
        self.Bus = Bus
        self.Bike = Bike
        self.Car = Car
        self.leftover = leftover
    def dimensions(self,length,width):
        self.length = length
        self.width = width
        self.area = self.length*self.width

P_owner = list()
P_kind = list()
P_name = list()
P_number = list()
P_intime = list()
P_series = list()
P_outime = list()
P_charges = list()
P_c = list()
c = 0
obj_veh = [0 for i in range(500)]
vehnums = [0 for i in range(500)]

e = 0
obj_lot_A = lot('A',100,300,600,0)
obj_lot_A.dimensions(250,4)
obj_lot_B = lot('B',100,300,600,0)
obj_lot_B.dimensions(250,4)
obj_lot_C = lot('C',100,300,600,0)
obj_lot_C.dimensions(250,4)
obj_lot_D = lot('D',100,300,600,0)
obj_lot_D.dimensions(250,4)




run = int(input("Welcome to Parking lot: Enter 1 : "))
while run:
    inp = int(input("1 for Parking  2 for Departure :"))
    if inp == 1:
        if e == 0:
            obj_lot = obj_lot_A
        elif e == 1:
            obj_lot = obj_lot_B
        elif e == 2:
            obj_lot = obj_lot_C
        elif e == 3:
            obj_lot = obj_lot_D
        
        vehicle_owner = str(input("Enter the vehicle's owner: "))
        while True:
            vehicle_kind = str(input("Enter the kind of vehicle: "))
            if vehicle_kind not in ['Bike','Bus','Car']:
                print("Enter a valid kind of vehicle")
                continue 
            break
        vehicle_name = str(input("Enter the name of vehicle: "))
        vehicle_number = str(input("Enter the vehicle number: "))
        vehicle_intime = str(input("Enter the intime for parking: "))
            #vehicle_milage = str(input("Vehicle's milage: "))
            #vehicle_capacity = str(input("Vehicle's capacity is: "))
            #vehicle_manufacturer = str(input("Vehicle is manufactured by: ")
            #vehicle_fuel = str(input("Enter the vehicle's fuel type: "))

        vehicle_length = int(input("Enter the length of vehicle: "))
        vehicle_width = int(input("Enter the width of vehicle: "))
        #vehicle_area = vehicle_length*vehicle_width
        obj_veh[c] = vehicle(vehicle_owner,vehicle_kind,vehicle_name,vehicle_number,vehicle_intime,"None","None")
        obj_veh[c].dimensions(vehicle_length,vehicle_width)

        P_owner.append(obj_veh[c].owner)
        P_kind.append(obj_veh[c].kind)
        P_name.append(obj_veh[c].name)
        P_number.append(obj_veh[c].number)
        P_intime.append(obj_veh[c].intime)
        P_outime.append(obj_veh[c].outime)
        P_charges.append(obj_veh[c].charges)
        p = 0
        if obj_veh[c].kind == "Bus":
            while True:
                if obj_lot.Bus >= obj_veh[c].area:
                    obj_lot.Bus = obj_lot.Bus - obj_veh[c].area 
                    P_series.append(obj_lot.series)
                    P_c.append(c)
                    dic = {"Owner": P_owner, "Vehicle":P_kind, "Vehicle Number":P_number, "Model": P_name, "Series": P_series, "Intime": P_intime, "C": P_c, "Outime": P_outime, "Charges":P_charges }
                    p = 1
                    break
                else:
                    print(f"Your vehicle can't be parked {obj_lot.series} in this series")
                    e += 1 
                    if e == 0:
                        obj_lot = obj_lot_A
                    elif e == 1:
                        obj_lot = obj_lot_B
                    elif e == 2:
                        obj_lot = obj_lot_C
                    elif e == 3:
                        obj_lot = obj_lot_D
                    else:
                        break
        elif obj_veh[c].kind == "Car":
            while True:
                if obj_lot.Car >= obj_veh[c].area:
                    obj_lot.Car = obj_lot.Car - obj_veh[c].area 
                    P_series.append(obj_lot.series)
                    P_c.append(c)
                    dic = {"Owner": P_owner, "Vehicle":P_kind, "Vehicle Number":P_number, "Model": P_name, "Series": P_series, "Intime": P_intime, "C": P_c, "Outime": P_outime, "Charges":P_charges }
                    p = 1
                    break
                else:
                    print(f"Your vehicle can't be parked {obj_lot.series} in this series")
                    e += 1 
                    if e == 0:
                        obj_lot = obj_lot_A
                    elif e == 1:
                        obj_lot = obj_lot_B
                    elif e == 2:
                        obj_lot = obj_lot_C
                    elif e == 3:
                        obj_lot = obj_lot_D
                    else:
                        break
        elif obj_veh[c].kind == "Bike":
            while True:
                if obj_lot.Bike >= obj_veh[c].area:
                    obj_lot.Bike = obj_lot.Bike - obj_veh[c].area 
                    P_series.append(obj_lot.series)
                    P_c.append(c)
                    dic = {"Owner": P_owner, "Vehicle":P_kind, "Vehicle Number":P_number, "Model": P_name, "Series": P_series, "Intime": P_intime, "C": P_c, "Outime": P_outime, "Charges":P_charges }
                    p = 1
                    break
                else:
                    print(f"Your vehicle can't be parked {obj_lot.series} in this series")
                    e += 1 
                    if e == 0:
                        obj_lot = obj_lot_A
                    elif e == 1:
                        obj_lot = obj_lot_B
                    elif e == 2:
                        obj_lot = obj_lot_C
                    elif e == 3:
                        obj_lot = obj_lot_D
                    else:
                        break
        if p:
            print("Parking Done.. ")
            c += 1
            df = pd.DataFrame(dic)
            #df.to_csv("/home/vinay/Gotcha/ParkingLot/Parking.csv", index=False)
        else:
            print("Parking Unsuccessful. No space left")
            break
    elif inp == 2:

        ou_t = str(input("Enter the outime of the vehicle :"))
        id = 0
        while True:
            veh_num = str(input("Enter your vehicle number for generation of parking fee:"))
            for h in range(0,c):
                if obj_veh[h].number == veh_num:
                    id = h    
                    break
                else:
                    print("Enter your vehicle number correctly.")
                    continue
            break

        in_t = obj_veh[id].intime
        li = [in_t, ou_t]
        intime , outime = covert(li)
        duration = outime - intime

        #print(duration)
        amt = charge(duration)
        print(f"The parking charges for {veh_num} is : {amt}")
        print("Departure done.. ")
        P_charges[id] = amt
        P_outime[id] = ou_t

        obj_veh[id].charges = amt
        obj_veh[id].outime = ou_t

        
        c -= 1
    rdic = dic = {"Owner": P_owner, "Vehicle":P_kind, "Vehicle Number":P_number, "Model": P_name, "Series": P_series, "Intime": P_intime, "C": P_c, "Outime": P_outime, "Charges":P_charges }
    rdf = pd.DataFrame(rdic)
    rdf.to_csv("/home/vinay/Gotcha/ParkingLot/ParkingLot.csv", index=False)
    exit_ = int(input("Want to exit: "))
    if exit_:
        break

