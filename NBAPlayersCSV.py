#Purpose: To create a csv file containing information from an API for NBA player data

# Import modules
import json
import requests
import csv


# Get JSON data from NBA players API using requests
url = "https://free-nba.p.rapidapi.com/players"


headers = {'X-RapidAPI-Key': '20aaee672fmsh52f6148adda23d3p1b9f4fjsne8316faadb28'}

# Define what page of data you start on and how many players you want to see per request. This will create 52 pages
params = {"page": '0', "per_page": '100'}
# Start a page 1
current_page = 1

# Create an empty list of players to append to later
players = []

#Create a while loop to iterate through 52 pages of information pulled from the API
while current_page < 53:
    # Send a get request for each page
    response = requests.request("GET", url, headers=headers, params=params)
    # Increment the pages by 1 to send a request for the next page
    current_page += 1
    # Update the param page key to the current page
    params["page"]=current_page
    # Transfrom the JSON string into a dictionary
    player_info = json.loads(response.text)
    # Iterate through the dictionary 
    for player in player_info["data"]:
        # Add players to the players from previous pages
        players.append(player)

# Get number of players and ensure you have the correct amount imported 
numofplayers = len(players)
if numofplayers != 5130:
    print("Make sure you got all the pages of API data")
else:
    print("Great! You were able to iterate through all pages.")

# print(players)


#If no position found, input Position Not Known
for i in range(numofplayers):
    if bool(players[i]["position"]) == 0:
        players[i]["position"] = "Position Not Known"

#Access Data
print(players[0]["id"]) #Expecting 14
print(players[0]["first_name"]) #Expecting Ike
print(players[0]["last_name"]) #Expecting Anigbogu
print(players[0]["position"]) #Expecting C
print(players[0]["team"]["full_name"]) #Expecting Indiana Pacers

#Create function that will make csv file of all NBA players
def Players_CSV():
    # Set fieldnames
    fieldnames = ['Player ID', 'First Name', 'Last Name', 'Position', 'Team Name']
    # Create rows
    rows = []
    #Iterate through list of player info
    for i in range(numofplayers):
    # Set row data to columns
        rows.append({"Player ID": players[i]["id"],
        "First Name": players[i]["first_name"],
        "Last Name": players[i]["last_name"],
        "Position": players[i]["position"],
        "Team Name": players[i]["team"]["full_name"]})
    
    # Write to csv file
    with open('NBAPlayers.csv', 'w', encoding='UTF8', newline='') as file:
        # Set fieldnames variable to fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        #writes fieldnames to header
        writer.writeheader()
        # writes rows using row data
        writer.writerows(rows)

    print("CSV created")

# Call function to create csv
Players_CSV()
    
