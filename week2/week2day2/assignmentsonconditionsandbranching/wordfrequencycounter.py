#Create a program that analyzes a given text and counts the frequency of each unique word.
#Ask the user to input a paragraph or sentence.
#Tokenize the input into words (ignoring punctuation and case sensitivity).
#Count the frequency of each unique word.
#Display the word frequencies in alphabetical order.
#Handle cases where the input is empty.

import string


def count_words(text):
    if not text:
        print("Oops! You didn't provide any text.")
        return

    # Removing punctuation and converting to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_freq = {}

    # Counting word frequencies
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Displaying word frequencies
    for word, freq in sorted(word_freq.items()):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    paragraph = input("Please enter  sentence or paragraph : ")
    count_words(paragraph)





