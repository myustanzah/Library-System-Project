# Assisted by watsonx Code Assistant 

import re

def is_palindrome(input_string):
    input_string = input_string.lower()
    input_string = re.sub(r'[^a-z0-9]', '', input_string)
    return input_string == input_string[::-1]

test_string = "A man, a plan, a canal: Panama"
if is_palindrome(test_string):
    print(test_string, "is a palindrome.")
else:
    print(test_string, "is not a palindrome.")

