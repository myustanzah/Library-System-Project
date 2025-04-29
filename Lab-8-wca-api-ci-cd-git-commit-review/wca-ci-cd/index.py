# Assisted by watsonx Code Assistant 
def is_number_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

# Example usage:
number = 12321
if is_number_palindrome(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")
