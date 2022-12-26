# Write a Python program to test whether a passed letter is a vowel or not.

# my solution
letter = str(input("Enter Any Alphabet : " ))
if letter in str("aeiou"):
    print("Letter Is Vowel : ", True)
else:
    print("Letter Is Not Vowel : ", False)


# common solution
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

'''
output = 
Case-1
Enter Any Alphabet : a
Letter Is Vowel :  True
False
True

Case-2
Enter Any Alphabet : b
Letter Is Not Vowel :  False
False
True
'''