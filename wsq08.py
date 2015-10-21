c = "y" 
#This is the condition to start over
while (c == "y"):
    x = input ("I will give you the factorial of?: ")
    x = int(x)
    n = 1
    fact = 1
    
    #This will do the multiplications
    
    while (n != (x+1)):
        fact = fact*n
        n = n+1
    print ("The result is: ", fact)
    
    #This changes the condition
    c = input("Do you want to check the factorial of another number? Type y for yes: ")
    c = c.lower()
print ("Bye bye")
