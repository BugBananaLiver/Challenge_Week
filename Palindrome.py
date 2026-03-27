def is_palindrome(string):
    lower_string = string.lower()
    stripped_lower_string = lower_string.strip()
    reverse_string = string[::-1]
    lower_reverse_string = reverse_string.lower()
    stripped_lower_reverse_string = lower_reverse_string.strip()
    if stripped_lower_reverse_string == stripped_lower_string:
        print("True")
    else:
        print("False")
    return

is_palindrome("Racecar")