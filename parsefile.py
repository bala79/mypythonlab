f = open("writefile.txt","r")
countryscoremap ={}
for countryscore in f:
    countrylist = countryscore.strip().split("|")
    countryscoremap[countrylist[0]]=countrylist[1]
    print(countrylist[0]+":"+countrylist[1])

print(countryscoremap)
f.close()
