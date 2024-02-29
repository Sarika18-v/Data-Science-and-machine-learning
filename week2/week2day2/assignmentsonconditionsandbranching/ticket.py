#Get the user's age and whether they are a student (True or False) as input.
#Define the ticket prices: Children (age 0-12): $10 Teenagers (age 13-17): $15 Adults (age 18 and above): $20 Students (regardless of age): $18 (discounted price). 
#Calculate and print the ticket price based on the user's age and student status.
#Handle cases where the entered age is not a valid numeric value.
#Provide a message for cases where the age is negative or non-integer.

#asking input from user about their age
User_age=int(input("Enter your age:"))
#checking if the provided value is valid or not
if(User_age<0):
        print("Enter a valid age")
else:
    #checking the given conditions and deciding the price of ticket
    user=input("Are you a student?(If YES: Enter True and If NO: Enter False )")
    if "True" in user:  
        print("Your Ticket price is $18(Discounted price regardless of age)") 
    elif User_age<12 and User_age>0: 
        print("Your ticket price is $10")
    elif User_age >=13 and User_age<=17:
        print("Your Ticket price is $15")
    else:
        print("Your Ticket price is $20")
        

