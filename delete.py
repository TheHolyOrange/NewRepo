import PatientMaintenance

def delete():
    i=str(input("Enter the patient id you want to delete: "))
    print(PatientMaintenance.deletePatient(i))
    
