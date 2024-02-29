#Create a simple grading system where a student's score is entered, and the program determines the corresponding grade.

#Get the student's score as input.
#Use the following grading scale:
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#Print the grade based on the input score.
#Handle cases where the entered score is not within the valid range (0-100).

#Asking for input
grade = float(input("Enter the grade: "))
#Checking if provided grade is within range or not
if grade<0:
    print("Invalid grade.")
elif grade>100:
    print("Invalid grade.")
    #Printing grades according to marks
else:
    if(grade>90 and grade<=100):
        print("Your grade is A")
    elif(grade>80 and grade<=90):
        print("Your grade is B")
    elif(grade>80 and grade<=670):
        print("Your grade is C")
    elif(grade>70 and grade<=60):
        print("Your grade is D")
    else:
         print("Your grade is F")