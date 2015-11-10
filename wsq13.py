def bbsq(number):
    start = number
    
    close = number/2
    first = (close + number / close)/2.0
    r = (first + number/first)/2.0
    
    while (r*r != start):
        r = (r + number/r)/2.0
    return (r)



x = input("Give me a number: ")
x = float(x)

result = bbsq(x)

print ("The result is: ",result)
