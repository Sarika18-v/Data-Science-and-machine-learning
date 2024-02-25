def vowelConsonant(string):
    #check alphabet or not
    if not string.isalpha():
        return 'Neither'
    #check vowel or consonant
    if string.lower() in 'aeiou':
        return 'Vowel'
    else:
        return 'Consonant'

# take input
string = input('Enter any string: ')

# calling function and display result
for char in string:
    #print vowels and consonants
    print(char,'is',vowelConsonant(char),end=' : ')