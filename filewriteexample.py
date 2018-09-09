import random

f = open("writefile.txt","w")

f1 = open("countries.txt","r")

for country in f1:
    country = country.strip()
    f.write(country+"|"+str(random.randint(1,10))+"\n")

f.close()
f1.close()
