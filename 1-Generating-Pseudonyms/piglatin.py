"""
Generate the Pig Latin equivalent to a word
"""

# Imports
import sys # Permits exiting from program directly

# Program

def main():
    """
    English word beginning with consonant:
        Move consonant to end
        Add 'ay' suffix
        Cow -> Owcay
    English word beginning with vowel:
        Add 'way' suffic
        Rotten -> Ottenray
    """

    print("Hello and welcome to the Pig Latinifier\n")

    # Keep looping until user exits
    while True:
        provided_word = input("\n\nPlease provide me with an English word: ")
        provided_word = provided_word.lower() # Work exclusively with lowercase
        
        # Make sure word length is sufficiently long
        while len(provided_word) < 3:
            provided_word = input('\nPlease provide a word at least three characters long: ').lower()

        if provided_word[0] not in ('aeiou'): # Word starts with consonant
            altered_word = ''.join([provided_word[1].upper(), provided_word[2:], provided_word[0], 'ay']) # Move con. to end, add 'ay'
        else: # Word starts with vowel
            altered_word = ''.join([provided_word[0].upper(), provided_word[1:], 'way'])
        print(f'\n\nYour Pig Latin translation is {altered_word}\n')

        try_again = input('\n\nTry again? (Press Enter else "n" to quit): ')
        if try_again.lower() == 'n':
            sys.exit()

if __name__ == "__main__":
    main()

