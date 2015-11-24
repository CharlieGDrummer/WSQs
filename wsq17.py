fil = open("movies.txt")
listmovies = []

listactors = []


'''
The mothafucka actors, lee una linea de codigo hasta ahorita, almacena en   ""actorname""   el actor de dicha linea
'''
sactor = 0
eactor = 1
fileforactors = fil.readline()
while True:
    actorname = fileforactors[sactor:eactor]
    eactor = eactor + 1
    if (actorname[-1] == ","):
        break



'''
The mothafucka movies, lee una linea de codigo hasta ahorita, almacena en   ""moviename""   las peliculas de dicha linea
'''

#For movies



s = eactor
e = s + 1
fileformovies = fil.readline()
count = 0
while ():
    
    moviename = fileformovies[s:e]
    
    while (moviename[-1] != ","):
        moviename = fileformovies[s:e]
        e =e+1
        
        if (count > len(moviename)):
            break
        count = count + 1
    
        
    if (moviename[-1] == ","):
            x = str(moviename)
            listmovies.append(x)

                
    
    s = e
    e = e+1
    count = count+1







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





#para el actor

sactor = 0
eactor = 1
fileforactors = fil.readline()
while True:
    actorname = fileforactors[s:e]
    eactor = eactor + 1
    if (actorname[-1] == ","):
        break


'''
