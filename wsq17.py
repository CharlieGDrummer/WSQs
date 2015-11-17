fil = open("movies.txt")
listmovies = []

listactors = []


count = 0
s = 0
e = 1
fileforactors = fil.readline()
print (len(fileforactors))
while (count != (len(fileforactors)-1)):
    
    actorname = fileforactors[s:e]
    
    while (actorname[-1] != ","):
        actorname = fileforactors[s:e]
        e =e+1
        if (count > 80):
            break
        
    if (actorname[-1] == ","):
        x = str(actorname)
        listactors.append(x)
        
        print (listactors) #Debug
                
    s = e
    e = e+1
    count = count+1

print (listactors)


x = input("DE")




'''
fileformovies = file.readline()
s = 0
e = 1

moviename = file[s:e]
if (moviename[-1] == ","):
    
    if (moviename not in listofmovies):
        



e = e+1


for line in file:
    s = 0
    e = 1
    moviename = file[s:e]

    while (moviename[-1] != ","):
        moviename = file[s:e]
        e = e+1
    if (moviename not in listmovies):
        listmovies.append(moviename)

print (listmovies)
'''
