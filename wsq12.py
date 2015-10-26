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

x = input()
y = input()

x = int(x)
y = int(y)

r = div(x,y)

print (r)

p = input()
