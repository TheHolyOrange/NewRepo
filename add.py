import PatientMaintenance

def add():
    flag=1
    while(flag):
        a=int(input("press 1 if you want to add a record press 0 if you want to end: "))
        if a == 1:
            i=str(input("Enter id: "))
            name=input("Enter name: ")
            print(PatientMaintenance.addPatient(i,name))
        else:
            print("end")
            flag=0

   


