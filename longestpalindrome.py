import scrabble

longestpalindrome = ""
for word in scrabble.WORDLIST:
    palindrome = True
    for i in range(len(word)):
        if(word[i]!=word[-(i+1)]):
            palindrome=False
    if (palindrome and len(word)>len(longestpalindrome)):
        longestpalindrome = word

print("The longest palindrome is "+longestpalindrome)
