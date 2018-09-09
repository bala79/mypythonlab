def sumofprices(pricelist):
    total =0;
    for price in pricelist:
        total = total + price
    return total

pricelist = [10.5,11.5,30.56]

mytotal = sumofprices(pricelist)

print("Total Price is "+str(mytotal))    
