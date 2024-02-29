#Palindromic Anagram Checker
#Objective
#Create a program that checks if a given string can be rearranged to form a palindromic string.
#Requirements
#A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward.
#Ask the user to input a string.
#Check and print whether the given string can be rearranged to form a palindrome.
#Ignore spaces and consider the characters in a case-insensitive manner.
#Handle cases where the input is empty or contains non-alphabetic characters.
#define function that takes input as parameter
def plaindrome_Check(input_string):
    #case sensitivity removed
    lower_string = input_string.lower()
    reverse_string = lower_string[::-1]
    if reverse_string == lower_string:
        print(f"Given String {input_string} is Palindrome" )
    else:
        print("Given String is not Palindrome")

input_string = input("Please enter a string")
plaindrome_Check(input_string)
        