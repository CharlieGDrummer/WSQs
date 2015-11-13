file = open("93cars.dat.txt",'r')

count = 0
for line in file:
    if (count % 2 == 0):
        manu = line[:14]
        model = line[14:29]
        midp = line[42:47]
        cmpg = line[52:55]
        hmpg = line[55:58]
        print ("For the car ",manu," model ",model,", the miderange price is ", midp,", the city mpg is ",cmpg, ", and the highway mpg is ", hmpg)
    count = count+1
