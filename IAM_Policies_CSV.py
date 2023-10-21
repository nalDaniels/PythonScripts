# Purpose: to create a csv file storing policy information from AWS IAM

# Import modules
import boto3
import csv

# Create a client for IAM to interact with the services
client = boto3.client('iam')

# Creates an iterator that will paginate through responses from IAM.Client.list_policies().
paginator = client.get_paginator('list_policies')

# Return 1000 policies per page/request
policiesiter = paginator.paginate(
    PaginationConfig={
        'PageSize': 1000}
)

# Create an empty list to append policies to
policies = []

# Iterate through items in pages and add to policies list, creating a two index list
for policy in policiesiter:
    policies.append(policy)

# Determine the data type 
print(type(policies[1]["Policies"]))

# Combine results from first and second pages to a new list
policieslist = policies[0]["Policies"] + policies[1]["Policies"]

# Get length of new list or all policies. Should be greater than 1000
numofpolicies = len(policieslist)
if numofpolicies >= 1000:
    print("Excellent, you have all the policies")
else:
    print("Make sure you have all the policies. ")

# Access data
print(policieslist[0]["PolicyName"]) # Expecting cloudwatch_policy
print(policieslist[0]["PolicyId"]) # Expecting ANPA6MNAXXTLQHJWWTTXG
print(policieslist[0]["Arn"]) # Expecting arn:aws:iam::988716448983:policy/cloudwatch_policy

# Create function that will make csv file of all IAM policies 
def IAM_CSV():
    # Create column names
    fieldnames = ['Policy ID', 'Policy Name', 'ARN']
    # Create an empty list for rows
    rows = []
    # Iterate through policies
    for i in range(len(policieslist)):
    # Append data to rows
        rows.append({"Policy ID": policieslist[i]["PolicyId"],
    "Policy Name": policieslist[i]["PolicyName"],
    "ARN": policieslist[i]["Arn"]})

    # Write to CSV file
    with open('IAMPolicies.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Creates column header
        writer.writeheader()
        # Writes in row data
        writer.writerows(rows)

    print("CSV created")

IAM_CSV()





