import scrabble

longestpalindrome = ""
for word in scrabble.WORDLIST:
    if((word == word[::-1]) and len(word)>len(longestpalindrome)):
        longestpalindrome = word

print("The longest palindrome is "+longestpalindrome)
