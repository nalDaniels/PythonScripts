# Purpose: To create a csv file containing information about the running processes on the system

import psutil
import os
import csv

#create a dictinary of process names, PIDs, and username of who initiated the process
procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}

#print dictionary
print(procs)


#determine how to iterate through dictionary items and access information
# for key, value in procs.items():
#     print(key) #Expecting PID
#     print(value['name']) #Expecting Process Name

#iterate through items in procs and add the executable path if it exists. otherwise add 'Not Found'
for key, value in procs.items():
    try:
        procs[key]["Exec Path"]=psutil.Process(key).exe()
    except (psutil.AccessDenied, psutil.PermissionError):
        procs[key]["Exec Path"]="Not Found"

print(procs)

#make a csv function
def Process_CSV():
    #create column names
    fieldnames = ['PID', 'Process Name', 'Exec Path', 'CPU Usage', 'Memory Usage']
    #create rows
    rows = []
    #create a for loop to iterate through dictionary of processes and assign column to data 
    for key, value in procs.items():
        rows.append({"PID": key,
        "Process Name": value["name"],
        "Exec Path": value["Exec Path"],
        "CPU Usage": psutil.Process(key).cpu_percent(),
        "Memory Usage": psutil.Process(key).memory_percent()
    })

    with open('Processes.csv', 'w', encoding='UTF8', newline='') as file:
    #sets field names to fieldnames variable
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    #writes fieldnames to header
        writer.writeheader()
        writer.writerows(rows)
  
#call function to create csv
Process_CSV()
