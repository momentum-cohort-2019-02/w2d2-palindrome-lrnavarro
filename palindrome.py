# request user input
user_text = input("Enter text here to check if it's a palindrome ")

# convert text to lower case        
lower_text = user_text.lower()

# remove spaces and special characters
no_spaces = (lower_text.replace(" ","").replace(",","").replace(":","").replace(".","").replace("!",""))

# compare text forwards and backwards
if no_spaces[:] == no_spaces[::-1]:
    print(no_spaces + ' is a palindrome')
else:
    print(no_spaces + ' is not a palindrome')