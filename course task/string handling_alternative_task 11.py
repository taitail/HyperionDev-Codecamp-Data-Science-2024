""" Make each alternate character into an upper case and each other alternate character
a lower case character.
e.g. The string “Hello World” would become “HeLlO WoRlD
making each alternative word lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”.
Tip: Using the split() and join() functions will help you here"""

input_string = input("enter a string: ") # Example:"Hello World"
new_str = ""
i = 0  # Manual index counter

for char in input_string:
    if i % 2 == 0:
        new_str += char.upper() # Capitalise even index character
    else:
        new_str += char.lower() # lower case odd index character 
    i += 1  # Increment the counter manually

print(new_str)  # Expected output: "HeLlO WoRlD"

input_sentence = input("Enter a sentence: ")# Example:"I am learning to code"
words = input_sentence.split()
new_words = []
i = 0  # Manual index counter

for word in words:
    if i % 2 == 0:
        new_words.append(word.lower())# Capitalise even index word
    else:
        new_words.append(word.upper())# lower case odd index word
    i += 1  # Increment the counter manually

new_s = ' '.join(new_words)
print(new_s)  # Expected output: "i AM learning TO code"

