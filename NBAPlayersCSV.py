#Purpose: To create a csv file containing information from an API for NBA player data

# Import modules
import json
import requests
import csv

# Make a GET request to the NBA API and get back JSON data
url = "https://free-nba.p.rapidapi.com/players"


headers = {'X-RapidAPI-Key': 'Enter API Key'}


response = requests.request("GET", url, headers=headers)

# Print response status code
print(response)

# Print data
print(response.text)

# Find data type of response
print(type(response.text))

# Turn string into dictionary
player_info = json.loads(response.text)

# Delete meta data
del player_info["meta"]

# Print dictionary
print(player_info)

#Find out how many players are in file
numofplayers = len(player_info["data"])


# Access data
# print(player_info["data"][0]["id"]) #Expecting 14
# print(player_info["data"][0]["first_name"]) #Expecting Ike
# print(player_info["data"][0]["last_name"]) #Expecting Anigbogu
# print(player_info["data"][0]["position"]) #Expecting C
# print(player_info["data"][0]["team"]["full_name"]) #Expecting Indiana Pacers

# If no position found, input 'Position Not Known'
for i in range(numofplayers):
    if bool(player_info["data"][i]["position"]) == 0:
        player_info["data"][i]["position"] = "Position Not Known"


# Create function that will make csv file of all NBA players
def Players_CSV():
    # Set fieldnames
    fieldnames = ['Player ID', 'First Name', 'Last Name', 'Position', 'Team Name']
    # Create rows
    rows = []
    # Iterate through list of player info
    for i in range(numofplayers):
    # Set row data to columns
        rows.append({"Player ID": player_info["data"][i]["id"],
        "First Name": player_info["data"][i]["first_name"],
        "Last Name": player_info["data"][i]["last_name"],
        "Position": player_info["data"][i]["position"],
        "Team Name": player_info["data"][i]["team"]["full_name"]})
    
    # Write to csv file
    with open('NBAPlayers.csv', 'w', encoding='UTF8', newline='') as file:
        # Set fieldnames variable to fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Writes fieldnames to header
        writer.writeheader()
        # Writes rows using row data
        writer.writerows(rows)

    print("CSV created")

# Call function to create csv
Players_CSV()
    
