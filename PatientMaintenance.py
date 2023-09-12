import DBconnection
import pyodbc

def addPatient(i,name):
    x=DBconnection.connect()
    conn = pyodbc.connect(x)
    cursor = conn.cursor()
    cursor.execute("Insert into Patient values (" + i + "," + "'" + name +"'" + ")")
    conn.commit()
    return("Patient has been saved successfully")

def clearPatient():
    x=DBconnection.connect()
    conn = pyodbc.connect(x)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Patient")
    conn.commit()
    return("Cleared all Records")

def deletePatient(i):
    x=DBconnection.connect()
    conn = pyodbc.connect(x)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Patient WHERE PatientID=" + i)
    conn.commit()
    return("Record deleted successfully")

def displayPatient():
    x=DBconnection.connect()
    conn = pyodbc.connect(x)
    cursor = conn.cursor()
    cursor.execute('select * from Patient')
    for row in cursor.fetchall():
        print(row)

def updatePatient(patientId,patientName):
    x=DBconnection.connect()
    conn = pyodbc.connect(x)
    cursor = conn.cursor()
    cursor.execute("UPDATE Patient SET PatientName='"+ patientName + "' WHERE PatientID="+ patientId)
    conn.commit()
    return("Updated successfully")