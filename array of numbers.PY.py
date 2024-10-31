def replace_vowel_codes(arr):
    # Dictionary to map ASCII codes to their corresponding vowels
    vowel_codes = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}

    # Replace numbers with vowels if they are in the vowel_codes dictionary
    return [vowel_codes.get(num, num) for num in arr]


# Examples
print(replace_vowel_codes([97, 98, 99, 100, 101]))  # Output: ['a', 98, 99, 100, 'e']
print(replace_vowel_codes([105, 106, 107, 108, 109]))  # Output: ['i', 106, 107, 108, 109]
print(replace_vowel_codes([117, 120, 121, 122]))  # Output: ['u', 120, 121, 122]
