"""
Load a text file as a list. (Example and practice program, not realistic)

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
# Imports
import sys

# Program
def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [word.lower() for word in loaded_txt]
            return loaded_txt
    except IOError as err:
        print(f'{err}\nError opening {file}. Terminating program.', file=sys.stderr)
        sys.exit(1) # Unrealistics, would generally want to write an error before terminating