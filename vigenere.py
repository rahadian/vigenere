#python challenge
#vigenere cipher
#rahadian arya

from string import ascii_lowercase
import itertools  
import numpy as np

key = "cipher"
keytoarray = key.split()
input = raw_input('Enter the lowercase word (without space) : ')
inputarray = input.split(" ")
alpatoarray = map(chr, range(97, 123))
numtoarray = map(int,range(0,26))
alpaarray = np.array(alpatoarray)
x = [1,5,7]
out = alpaarray[x]
index = alpatoarray.index("b")

for i in alpatoarray:
    x = alpatoarray.index(i)
    print i," =",x

for a in numtoarray:
    x = alpatoarray[a]
    print a," =",x 

print "\r"
print "Arithmetic Substitution"
for (z,k) in zip(input,itertools.cycle(key)):
    hasil = alpatoarray.index(z)+alpatoarray.index(k)
    # hasilarray = hasil.split("\r")
    if hasil > 26:
        hasil = alpatoarray.index(z)+alpatoarray.index(k)-26
    print z,'=',alpatoarray.index(z),"+",k,'=',alpatoarray.index(k),'=',hasil

print "\r"
for (m,n) in zip(input,itertools.cycle(key)):
    hasil = alpatoarray.index(m)+alpatoarray.index(n)
    if hasil > 26:
        hasil = alpatoarray.index(m)+alpatoarray.index(n)-26
    hasilarray = np.asarray(hasil)
    print hasilarray,'=',alpatoarray[hasilarray]
print "\r"
print "Chipertext ",
print "\r"
for (m,n) in zip(input,itertools.cycle(key)):
    hasil = alpatoarray.index(m)+alpatoarray.index(n)
    if hasil > 26:
        hasil = alpatoarray.index(m)+alpatoarray.index(n)-26
    hasilarray = np.asarray(hasil)
    strhasil = str(alpatoarray[hasilarray])
    print strhasil.rstrip(),
    
    


    


