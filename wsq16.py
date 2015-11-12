file = open("93cars.dat.txt",'r')


for line in file:
    x = line
    manu = x[:14]
    model = x[14:29]
    midp = x[42:47]
    cmpg = x[52:55]
    hmpg = x[55:58]
    print ("For the car ",manu," model ",model,", the miderange price is ", midp,", the city mpg is ",cmpg, ", and the highway mpg is ", hmpg)
