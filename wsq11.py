natural = 0
pali = 0
lycherel = 0

a = input ("Lower bound: ")
b = input ("Upper bound: ")
a = int(a)
b = int(b)

mainlist=[]
for i in range (a,b+1):
    mainlist.append(i)
    
lenght = len (mainlist)
n = 0
while (n != lenght):
    mainlist[n] = str(mainlist[n])
    n = n+1

for e in range (0,b):
    x = mainlist[e]
    y = x[::-1]
    
    if ( x == y):
        natural = natural + 1
    elif (x[-1] == "0"):
        pali = pali + 1
    else:
        
        p = 0
        while ((x != y) and (p != 30)):
            x = int(x)
            y = int(y)

            x = x + y
            
            x = str(x)
            y = x[::-1]
            
            if (x == y):
                pali = pali + 1
            p = p+1
            
        if ((x != y) and (p >= 30)):
            lycherel = lycherel + 1
                
print ("Total numbers: ",lenght)
print ("Natural palinndromes: ",natural)
print ("Become palindromes: ",pali)
print ("Lyrechel candidates: ", lycherel)
