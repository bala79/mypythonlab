import scrabble

longestpalindrome = ""
for word in scrabble.WORDLIST:
    if((list(word)== list(reversed(word))) and len(word)>len(longestpalindrome)):
        longestpalindrome = word

print("The longest palindrome is "+longestpalindrome)
