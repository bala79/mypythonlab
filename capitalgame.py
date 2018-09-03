country_capital_dict = {
"India":"New Delhi",
"USA":"Washington D.C.",
"France":"Paris",
"England":"London"
}

import random

country_list = list(country_capital_dict.keys())

for i in range(1,5):
    country = random.choice(country_list)
    capital = country_capital_dict[country]
    capital_input= input("what is the capital of "+country+"?")


    if capital_input == capital:
        print("Good Job, Correct")
    else:
        print("Nice Try, Try Again !!!")

print("Thank you !!!")
