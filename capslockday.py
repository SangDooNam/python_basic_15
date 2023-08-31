"""Task

October 22nd is CAPS LOCK DAY. Apart from that day, 
every sentence should be lowercase, so write a program to normalize a sentence.

Create a program that takes a string. 
If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end. 
Each string is a normalized sentence and should start with an uppercase character."""


text = input("Enter any text.: ")

new_text = ""

width = 40


empty_space = " " * (width - len(text))

if text.isupper():
    new_text = text.lower().capitalize() +"!"
    

else:
    new_text = text.capitalize()



print(f'Enter string: {text}{empty_space}-->  "{new_text}"')
        



# text = input("Enter any text.: ")

# print(text.isupper())