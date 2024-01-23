# filename: palindrome_checker.py
def is_palindrom(text):
"""
Check if given text is a palindrome (reads the same backward as forward).
"""
 return text == text[::-1]

text = input("Enter a text to check: ")
result = is_palindrom(text)
print(f"'{text}' is a palindrome? {result}")