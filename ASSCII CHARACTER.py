def number_to_ascii(number):
    if 0 <= number <= 127:  # Valid ASCII range
        return chr(number)
    else:
        return "Invalid ASCII code"

# Examples
print(number_to_ascii(65))
print(number_to_ascii(97))
print(number_to_ascii(48))
