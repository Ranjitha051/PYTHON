is_palindrome = lambda s: s == s[::-1]

s = input("Enter a string: ")

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")
