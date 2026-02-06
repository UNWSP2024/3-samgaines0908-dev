#Author: Sam Gaines
#Date: 2/6/2026
#Title: Shipping Charges 

def weight_conversion(weight):
    # Calculate the shipping charge.
    
    ######################
    if weight <= 2:
        total = weight * 1.50
    elif weight <= 6:
        total = weight * 3.00
    elif weight <= 10:
        total = weight * 4.00
    else:
        total = weight * 4.75

    return total
   ######################
    
#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
