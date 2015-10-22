#The restart loop
c = "y"
while (c == "y"):
    x = []
    n = 0
    
    #The loop to recieve the list
    for e in range (0,10):
        e = input("Give me a number: ")
        x.append(e)
        x[n] = float(x[n])
        n = n+1

    #To get the total
    total = 0
    for e in range (0,10):
        total = total + x[e]
    #To get the average
    average = total/10
    
    #To get the variation
    vari = 0
    for e in range (0,10):
        vari = vari + (x[e] - average)**2
    
    #To gert the standard desviation
    desvi = (des / 10)**(1/2)

    print ("La lista es: ", x)
    print ("La sumatoria es: ", total)
    print ("El promedio es: ", average)
    print ("La desv. estandard es: ",desvi)
    
    #Restart option
    c = input("Restart? y for yes: ")
    c = c.lower()
