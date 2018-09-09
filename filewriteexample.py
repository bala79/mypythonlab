f = open("writefile.txt","w")

f1 = open("countries.txt","r")

for country in f1:
    f.write(country)

f.close()
f1.close()
