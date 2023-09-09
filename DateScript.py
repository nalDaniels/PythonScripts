#TRY RUNNING ALL FUNCTIONS IN A BACHELORETTE FUNCTION

# Purpose:
# Create a date.py script that is a date simulator and does the following:

# User inputs who is on the date with them
# User inputs their budget for the date
# User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
# Script tells the user how much money they have left after each order.
# At the end of the date user must agree to pay the bill and then their final budget is shown to them.
# Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision. 


print("Welcome to this season's Bachelorette with Jamie! ")
date = input("Which bachelor are you taking on a date to Black Sea, Jamie? ")
budget = int(input("Black Sea is pretty expensive! What is your budget? "))

#print("Welcome to Black Sea! Take a look at our menu!")
menu = {
    "Lobster": 89,
    "Caviar": 67, 
    "Truffle Fries": 38,
    "Chilean Sea Bass": 60,
    "Mocktail": 30,
    "Bottle of Wine": 60}
print(menu)

#Create a function to take the order and create a list
def takeorder():
    order = input("What would you like to order? (Separate items with ', ') ")
    orderlist = order.split(", ")
    print("Your order of " + ", ".join(orderlist) + " will be out shortly")
    return orderlist
    
#Saves a list of the order inside a variable order, so we can use it in the remaining budget function 
order = takeorder()

#Create a function that shows the remaining budget after ordering food and drinks and returns the bill plus tip
#It refers back to the menu dictionary to get the prices for the items ordered, then sums up the cost of all items ordered
def remaining(orderlist, budget):
    bill = 0
    for item in orderlist:
        bill = menu[item] + bill
    if budget - bill < 0:
        print("You are over budget by " + str(bill - budget) + " dollars")
    else:
        print("You have " + str(budget - bill) + " dollars leftover in your budget")
    #calculate the bill and tip
    return float(bill) * 1.2

#Run the function using the order and budget and save output to variable bill
bill = remaining(order, budget)

#Create a function that asks Jamie's date if he wants to pay the bill, so it can be used in next function
def pay_bill(bill):
    answer = input(f"Would you like to pay your bill of {bill}? ").lower()
    if answer == "yes":
        print("Thank you for paying your bill")
    elif answer == "no":
        print("Roll up your sleeves and join us in the back to wash some dishes")

#Call the paybill function to see if Jamie's date pays bill
pay_bill(bill)

#Create a function where Jamie tests date and determines whether he gets a second date
def second_date(date):
    answer2 = input(f"{date}, what is my favorite color? ").lower()
    if answer2 == "orange":
        print(f"You listened! I've made my decision. {date} has earned a second date!")
    else:
        print(f"Were you even listening to me? I've made my decision. {date} won't be getting a second date!")

#Run the function 
second_date(date)

#Extras didn't like something?

