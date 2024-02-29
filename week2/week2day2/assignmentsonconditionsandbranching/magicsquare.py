#Magic Square Validator
#Objective
#Create a program that checks if a given 3x3 matrix forms a magic square.

#Requirements
#A magic square is a square matrix where the sums of the numbers in each row, column, and both main diagonals are the same.
#Ask the user to input a 3x3 matrix (nine integer values).
#Check and print whether the given matrix forms a magic square.
#Handle cases where the input matrix is not of size 3x3 or contains non-integer values
#initializing matrix
a=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("Enter the number"))
        b.append(j)
    a.append(b)
print("your matrix is: ")
for i in range(3):
    for j in range(3):
       print(a[i][j])
    print(" ")
if a[i] != a[j]:
    print("Invalid matrix")
else:
    #checking if the diagonals are equal
    sumd1=0
    sumd2=0
    for i in range(3):
        for j in range(3):
            if i==j:    #locations equalled as the first element in diagonal is 11 another is 22 and another is 33
                sumd1=sumd1+a[i][j]
            if i+j==3-1:    #location are calculated as i+j=n-1
                sumd2=sumd2+a[i][j]
                #checking if diagonals are equal
if sumd1   != sumd2:
    f=1
else:
     #sum of row and column
    for i in range(3):
        sumr=0 
        sumc=0
        for j in range(3):
            sumr=sumr + a[i][j]
            sumc=sumc + a[j][i]
            #checking if row and diagonal1 are equal
        if sumr !=sumd1:
            f=1
            #checking if column and diagonal1 are equal
        elif sumc!= sumd1:
            f=1
        else:
            f=0
    #if f not equal to 1 it gives result as sum of row column diagonal1 and diagonal 2 are equal
if f==0:
    print("Square is magic matrix.")
else:
    print("matrix isnot magic square")