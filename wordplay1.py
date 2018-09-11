import scrabble
import string

for word in scrabble.WORDLIST:
    for letter in string.ascii_lowercase:
        if letter*2 in word:
            print(word)
