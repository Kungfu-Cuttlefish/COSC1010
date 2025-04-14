#
# Syrus Freeman
# 4/13/2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def main ():
    # Get characters from the user
    user_str = input ('Enter a string of characters: ')
    # Give the number of vowels and consonants
    print ('That string has', num_vowels (user_str), 'vowels, and', num_consonants (user_str), 'consonants.')
def num_vowels(s):
    # Create List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize an accumulator
    v_count = 0

    # count the vowels (lowercase)
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1
    # Return vowel count
    return v_count

def num_consonants(s):
    # Create List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize an accumulator
    c_count = 0

    # count the consonants (lowercase)
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1
    # Return C count
    return c_count
main ()

