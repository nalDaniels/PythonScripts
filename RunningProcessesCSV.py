# Purpose: To create a csv file containing information about the running processes on the system

import psutil
import os
import csv

# Create a dictinary of process names, PIDs, executable path, cpu and memory percentage
procs = {p.pid: p.info for p in psutil.process_iter(['name', 'exe', 'cpu_percent', 'memory_percent'])}

# Print dictionary of processes
print(procs)


# Determine how to iterate through dictionary items and access information
# for key, value in procs.items():
#     print(key) #Expecting PID
#     print(value['name']) #Expecting Process Name
#     print(value['cpu_percent']) #Expecting CPU percentage
#     print(value['memory_percent']) #Expecting Memory percentage



# Iterate through items in procs and add the executable path if it exists; otherwise, add 'Not Found'
for key, value in procs.items():
    try:
        procs[key]["Exec Path"]=psutil.Process(key).exe()
    except (psutil.AccessDenied, psutil.PermissionError):
        procs[key]["Exec Path"]="Not Found"

# Print dictionary with new path information
print(procs)

# Make a csv function
def Process_CSV():
    # Create column names
    fieldnames = ['PID', 'Process Name', 'Exec Path', 'CPU Usage', 'Memory Usage']
    # Create rows
    rows = []
    # Create a for loop to iterate through dictionary of processes and assign column to data 
    for key, value in procs.items():
        rows.append({"PID": key,
        "Process Name": value["name"],
        "Exec Path": value["Exec Path"],
        "CPU Usage": value["cpu_percent"],
        "Memory Usage": value["memory_percent"]
    })
    # Write to csv file
    with open('Processes.csv', 'w', encoding='UTF8', newline='') as file:
    # Set field names to fieldnames variable
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Writes fieldnames to header
        writer.writeheader()
    # Write in row data
        writer.writerows(rows)
    
    print("CSV created")
  
# Call function to create csv
Process_CSV()
