#Author: Sam Gaines
#Date: 2/6/2026
#Title: Age Classifer 

def categorize_age(age): 
    
    ######################
    if age <=1: return "infant"
    elif 1< age <13: return "child"
    elif 13<= age < 20: return "teenager"
    else: return "adult"
    ######################



#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
