def calculate_e(estimation):
    r = 1
    limit = 0.0
    oldlimit = 1.0
    n = 1
    while ( abs(oldlimit - limit) > estimation):
        oldlimit = limit
        limit = (1+1/n)**n
        n = n+1
    return (limit)
    
est = float(input("Give me the estimation: "))
          
r = calculate_e(est)

print ("The result is: ",r)
