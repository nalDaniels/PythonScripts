# Purpose:
# Create a date.py script that is a date simulator and does the following:

# User inputs who is on the date with them
# User inputs their budget for the date
# User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
# Script tells the user how much money they have left after each order.
# At the end of the date user must agree to pay the bill and then their final budget is shown to them.
# Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision. 


#Create a function to take the order and create a list
def takeorder(menu):
    order = input("What would you like to order? (Separate items with ', ') ")
    orderlist = order.split(", ")
    for item in orderlist:
        if item.title() == "Bottle Of Wine":
            #create a global variable to be used in another function
            global wine
            wine = input("White or Red? ")
        if item not in menu.keys():
            print("Sorry, we don't sell that here.")
        else: 
            print("Your order of " + ", ".join(orderlist) + " will be out shortly")
    return orderlist
    
#Create a function that shows the remaining budget after ordering food and drinks and returns the bill plus tip
def remaining(orderlist, budget, menu):
    bill = 0
    for item in orderlist:
        if item.title() == "Bottle Of Wine":
            bill = menu[item.title()][wine.title()] + bill
        else:
            bill = menu[item.title()] + bill
    if budget - bill < 0:
        print("You are over budget by " + str(bill - budget) + " dollars")
    else:
        print("You have " + str(budget - bill) + " dollars leftover in your budget")
    return float(bill) * 1.2


#Create a function that asks Jamie's date if he wants to pay the bill, so it can be used in next function
def pay_bill(bill, budget):
    answer = input(f"Would you like to pay your bill of {bill}? ").lower()
    if answer.lower() == "yes":
        print("Thank you for paying your bill")
        print("You have " + str(budget - bill) + " left in your budget.")
    elif answer.lower() == "no":
        print("Roll up your sleeves and join us in the back to wash some dishes")


#Create a function where Jamie tests date and determines whether he gets a second date
def second_date(date):
    answer2 = input(f"{date}, what is my favorite color? ").lower()
    if answer2.lower() == "orange":
        print(f"You listened! I've made my decision. {date} has earned a second date!")
    else:
        print(f"Were you even listening to me? I've made my decision. {date} won't be getting a second date!")


#Create the date simulator app
def Bachelorette():
    print("Welcome to this season's Bachelorette with Jamie! ")
    date = input("Which bachelor are you taking on a date to Black Sea, Jamie? ")
    budget = int(input("Black Sea is pretty expensive! What is your budget? "))

    print("Welcome to Black Sea! Take a look at our menu!")
    menu = {
    "Lobster": 89,
    "Caviar": 67, 
    "Truffle Fries": 38,
    "Chilean Sea Bass": 60,
    "Mocktail": 30,
    "Bottle Of Wine": {"Red": 60, "White": 50}}
    print(menu)

    order = takeorder(menu)


    try:
        bill = remaining(order, budget, menu)
    except KeyError:
        takeorder(menu)

    pay_bill(bill, budget)
    
    second_date(date)

#Run the date simulator function
Bachelorette()
