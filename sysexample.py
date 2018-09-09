import sys
import random

if(len(sys.argv)<2):
    print("Not suffient input to process")
    exit(1)
f = open(sys.argv[1],"r")

country_capital = {}

for country in f:
    countrycaplist = country.strip().split("|")
    country_capital[countrycaplist[0]]=countrycaplist[1]

print(country_capital)

countrylist = list(country_capital.keys())
while True:
    country = random.choice(countrylist)
    capital = country_capital[country]
    capitalinput = input("Enter the capital of "+country+">")
    if capitalinput == "quit":
        break
    elif capitalinput ==   capital:
        print("Good Work")
    else:
        print("Nice Try")


print("Bye !!!")
