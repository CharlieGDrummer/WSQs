fil = open("movies.txt")
listmovies = []

listactors = []


#For actors
e = 1
s = 0
fileforactors = fil.readline()
while True:
    actorname = fileforactors[s:e]
    e = e + 1
    if (actorname[-1] == ","):
        break
print ("Actro",actorname) #Debug
    



#For movies
count = 0
s = e
e = s + 1
fileformovies = fil.readline()
print (len(fileformovies)) #Debug
while (count != (len(fileformovies)-2)):
    
    moviename = fileformovies[s:e]
    
    while (moviename[-1] != ","):
        moviename = fileformovies[s:e]
        e =e+1
        if (count > 80):
            break
        
    if (moviename[-1] == ","):
        x = str(moviename)
        listmovies.append(x)
        
        print (listmovies) #Debug
                
    s = e
    e = e+1
    count = count+1

print ("movies",listmovies) #Debug


x = input("DEBUG")




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
