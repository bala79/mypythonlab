countries = open("countries.txt","r").readlines()
#print(type(f))
countries = [country.strip() for country in countries]
print(countries)
print(len(countries))

for country in countries:
    if country[0] == "I":
        print(country)
