fil = open("movies.txt")

'''
init = 0
if (init = 0):
    justlist = fil.read
    text = fil.read()
    for f in justlist:
        f = justlist.readline()
'''
    
f = fil.readline()

sactor = 0
eactor = 1
while True:
    actorname = f[sactor:eactor]
    eactor = eactor + 1
    if (actorname[-1] == ","):
        break
print ("El actor es ",actorname)


count = 0
proof = 1
s = eactor
e = s + 1
while True:     
    moviename = f[s:e] #Just to start
    
    while (moviename[-1] != ","):
        moviename = f[s:e]
        e =e+1
    if (moviename[-1] == ","):
        proof = proof + 1
    s = e
    e = e+1
    count = count + 1
    if (count > proof ):
        break

    print (" count: ",count, "| proof: ",proof," E ES:",e)
x = input("DEV")






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
