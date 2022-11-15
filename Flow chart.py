# 15/11/22 made by Josh.B | Little script for a shopping cart made along side a flow chart with full quotation.
shopping_cart = 0
item_price = 1.75  # delcaring shopping cart value and item price


def total():  # fucntion for calculating and displaying the finnal cost and quantity of the shopping cart
    pay_loop = True  # delcaring while loop variable
    print("\nnumber in shopping cart: "+str(shopping_cart))
    print("total price "+str(item_price*shopping_cart))  # displaying finnal number of items in shopping cart and finnal price

    while pay_loop == True:  # while loop for option if user wants to pay
        pay = input("\ndo you wish to pay?\n(yes or no)  ")  # input if user wants to pay for the shopping cart
        if pay == "yes":  # if yes thanks user and ends script
            print("\nitems payed for thank you :)")
            exit()
        elif pay == "no":  # if no starts the script over again
            print("\nitems not payed for :(\nstarting again...")
            add_cart()


def add_cart():  # function for adding item to the shopping cart
    cart_loop = True
    more_loop = True  # delcaing while loop variables
    many_loop = True
    global shopping_cart  # calls global variable for shopping cart value
    shopping_cart = 0  # sets shopping cart value to 0 incase user does not pay

    while cart_loop == True:  # while loop for option to add items to the shopping cart
        print("\nthe price is £" + str(item_price))
        add = input("add item to shopping cart? \n(yes or no)  ")  # input if user wants to add the item to the shoppin cart yes or no
        if add == "yes":  # if yes will break loop
            print("\nitem added to shopping cart")
            break
        elif add == "no":  # if no will end the function
            print("\nitem not added to shopping cart")
            return
        else:  # error handling for incorrect input
            print("\nincorrect input")
    
    while more_loop == True:  # while loop for option to add more than 1 item to shopping cart
        more = input("\ndo you want more than 1?\n(yes or no)  ")  # input if user wants more than 1 item in the shopping cart yes or no
        if more == "yes":  # if yes will break loop
            break
        elif more == "no":  # if no will add 1 item to shoppin cart and end the function
            shopping_cart = shopping_cart + 1
            total()
        else:  # error handling for incorrect input
            print("\nincorrect input")

    while many_loop == True:  # while loop for input of number of items into the shopping cart 
        num = input("\nhow many?  ")  # input for the number of items user wants to add to the shopping cart
        try:  # error handling checking the input is a integer uses try to avoid script crashing due to data type error
            num = int(num)
            shopping_cart = shopping_cart+num
            total()  # if input is a number runs calculation function
        except ValueError:  # error handling for if input is not number
            print("\nincorrect input")


add_cart()