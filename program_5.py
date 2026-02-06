#Author: Sam Gaines
#Date: 2/6/2026
#Title: Hot Dog

hot_dog_price= 3.50 
chili_dog_price= 4.50
cheese_price= 0.50
peppers_price= 0.75
grilled_onions_price= 1.00

#Getting Hot Dog Types
def get_hot_dog_type():
    hot_dog_type = input("Hello would you like a hot dog or a chili dog? ").lower()
    if hot_dog_type == "hot dog":
        return hot_dog_price
    elif hot_dog_type == "chili dog":
        return chili_dog_price
    else:
        print("Please enter a valid hot dog type.")
        return get_hot_dog_type()


subtotal= get_hot_dog_type()

#Ask for toppings
cheese= input("Would you like a cheese?(Yes or No) ").lower()
if cheese == "Yes":
    subtotal+=cheese_price

Peppers= input("Would you like a peppers?(Yes or No) ").lower()
if Peppers == "Yes":
    subtotal+=peppers_price

grilled_onions= input("Would you like a grilled onions?(Yes or No) ").lower()
if grilled_onions == "Yes":
    subtotal+=grilled_onions_price

#Calcutate tax
tax= subtotal*0.07
total_cost= subtotal + tax

print("your subtotal is $",subtotal)
print("your tax amount is $",tax)
print("your total cost is $",total_cost)
print("Have a wonderful day!")
