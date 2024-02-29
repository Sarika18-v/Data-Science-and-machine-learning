#Q.1 Write a python program that initializes non empty list of words with length = 5. Display longest word with its length.**

s= ['mango', 'banana', 'kiwi', 'apple', 'grapes']
if len(s[0])>len(s[1]):
    print(s[0])
    print(len(s[0]))

else:
    if len(s[1])>len(s[2]):
        print(s[1])
        print(len(s[1]))
    else:
        if len(s[2])>len(s[3]):
            print(s[2])
            print(len(s[2]))
        else:
            if len(s[3])>len(s[4]):
                print(s[3])
                print(len(s[3]))
            else:
                print(s[4])
                print(len(s[4]))
      
