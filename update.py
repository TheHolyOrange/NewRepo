import PatientMaintenance

def update():
    patientId=input("Enter the ID you want to change: ")
    patientName=input("Enter the name of the updated patient: ")
    print(PatientMaintenance.updatePatient(patientId,patientName))