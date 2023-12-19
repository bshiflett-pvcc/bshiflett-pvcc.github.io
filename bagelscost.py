# Brayden Shiflett
# Prog Purpose: This program cretaes a sales receipt for Brownsville bagels
#   Price for one bagel: $2.25
#   Price for cream cheese: $1.25
#   Sales tax rate: 6%
import datetime

############# define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .06
PR_BAGEL= 2.25
PR_ CREAMCH = 1.25
SyntaxError: invalid syntax

#define global variables
num_bagels = 0
num_creamch = 0
cost_bagels = 0
cost_creamch = 0
subtotal = 0
sales_tax = 0
total = 0

############## Define program functions ##############
def main():
    get_user_data()
    perfrom_calculations()
    display_results()

def get_user_data():
    global num_bagels, num_creamch
    num_bagels = int(input("Number of bagels:9"))
    num_creamch = int(input("Number of creamcheese:3"))
def perform_calculations():
    global cost_bagels, cost_creamch, subtotal, sales_tax, total
    cost_bagels = num_bagels * PR_BAGEL
    cost_creamch = num_creamch * PR_CREAMCH
    subtotal = cost_bagels * SALES_TAX_RATE
    total = subtotal + slaes_tax

def display_result():
    print('--------------------------------')
    print('BROWNSVILLE BAGEL COMPANY')
    print('Fresh-baked bagels every day!')
    print('--------------------------------')
    print('Bagels       $ ' + format(cost_bagels,'8,.2f'))
    print('Cream Cheese $ ' + str(cost_creamch))
    print('--------------------------------')
    print('Subtotal     $ ' + str(cost_creamch))
    print('--------------------------------')
    print('Subtotal     $ ' + str(subtotal))
    print('Sales TAx    $ ' + str(sales_tax))
    print('Total        $ ' + str(total))
    print('--------------------------------')
    print(str(datetime.datetime.now()))
    ##########  call on main program to execute ##########
    main()
