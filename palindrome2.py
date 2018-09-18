import scrabble


palindrome_list = [word for word in scrabble.WORDLIST if word == word[::-1]]
print(palindrome_list)
print ("There are total "+str(len(palindrome_list))+" words as palindrome")

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
