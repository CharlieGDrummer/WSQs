def div(x,y):
    if ( x < y):
        p = x
        q = y
        x = q
        y = p
    
    while (y != 0):
        i = x%y
        x = y
        y = i      
        
    return (x)

x = input("Give me a number: ")
y = input("Give me a number: ")

x = int(x)
y = int(y)

r = div(x,y)

print ("The result is: ",r)
