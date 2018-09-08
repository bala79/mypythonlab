f = open("countries.txt","r")
#print(type(f))
countries = []
for country in f:
    country =  country.strip()
    countries.append(country)
f.close()
print(countries)
print(len(countries))

for country in countries:
    if country[0] == "I":
        print(country)
