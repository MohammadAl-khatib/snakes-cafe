menu = {
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,
    "Ice Cream":0,
    "Cake":0,
    "Pie":0,
    "Coffee":0,
    "Tea":0,
    "Unicorn Tears":0
}

print ("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************""")

def cafe_orders_handler():

    """  
    This function takes orders from a user and displays them back

    input:
    order (string)

    output:
    string of orders taken
    """

    order = input('> ')
    while order != 'quit':
        # menu[order]=0     # uncomment for letting user choose out from the menu without a warning
        if order in menu:
            menu[order]+=1
            print (f"** {menu[order]} orders of {order} have been added to your meal **")
            order = input('> ')
        else:
            print ('Pleae choose from our menu')
            order = input('> ')
    print ('Thanks for chosing our snakes-cafe, see you soon')


if __name__ == '__main__':
    cafe_orders_handler()
    