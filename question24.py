"""24. Write a Python program to test whether a passed letter is a vowel or not. """

def vowel_check(letter):
        all_vowels ="aeiou"
        if letter in all_vowels:
                print("Vowel is present")
        else:
                print("Vowel is not present")

if __name__ == "__main__":
        vowel_check('c')
        vowel_check('i')
        
        

