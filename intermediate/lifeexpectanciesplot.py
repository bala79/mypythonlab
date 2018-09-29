from matplotlib import pyplot

data = open("life_expectancies_usa.txt","r").readlines()
datelist = []
male_expect_list = []
female_expect_list =[]
for elt in data:
    date, male_expect, female_expect = elt.split(",")
    datelist.append(date)
    male_expect_list.append(male_expect)
    female_expect_list.append(female_expect)

pyplot.plot(datelist,male_expect_list,"bo-",label="Men")
pyplot.plot(datelist,female_expect_list,"mo-",label="Women")

pyplot.legend(loc="upper left")
pyplot.ylabel("Age")
pyplot.xlabel("Year")
pyplot.title("Life Expetancies in USA")
pyplot.show()
