def bbsq(number):
    start = number
    
    close = number/2
    r = (close + number / close)/2.0   
    while ( abs(r*r - start) > 0.00000000001):
        r = (r + number/r)/2.0
    return (r)



x = input("Give me a number: ")
x = float(x)

result = bbsq(x)

print ("The result is: ",result)
