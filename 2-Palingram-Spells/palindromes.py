"""Find palindromes in a dictionary file."""

# Imports
import load_dictionary # Our helper function to load in dictionary files

# Program
word_list = load_dictionary.load('2of4brif.txt') # Load in dictionary list
pali_list = [] # Init list to append confirmed palindromes

for word_ in word_list:
    if len(word_) > 1 and word_ == word_[::-1]:
        pali_list.append(word_)

print(f'\nNumber of palindromes: {len(pali_list)}\n')
print(*pali_list, sep='\n') # Use *arg/splat operator, *