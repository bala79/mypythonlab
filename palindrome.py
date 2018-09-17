import scrabble

counter = 0
for word in scrabble.WORDLIST:
    palindrome = True
    for i in range(len(word)):
        if(word[i]!=word[-(i+1)]):
            palindrome=False

    if palindrome:
        counter =  counter+1
        print("Yes,"+ word + " is a Palindrome")

print ("There are total "+str(counter)+" words as palindrome")

# myword="kayak"
# mypalindrome = True
# for i in range(len(myword)):
#     print(myword[i])
#     if(myword[i]!=myword[-(i+1)]):
#         mypalindrome=False
#
# if mypalindrome:
#     print("Yes,"+ myword + " is a Palindrome")
# else:
#     print("Not a palindrome")
