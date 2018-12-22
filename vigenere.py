# import string
from string import ascii_lowercase
import itertools  
import numpy as np


key = "cipher"
keytoarray = key.split()
# plain = "Universitas Airlangga"
input = raw_input('Masukkan kata : ')
inputarray = input.split(" ")
alpatoarray = map(chr, range(97, 123))
numtoarray = map(int,range(0,26))
alpaarray = np.array(alpatoarray)
x = [1,5,7]
out = alpaarray[x]
index = alpatoarray.index("b")

for i in alpatoarray:
    x = alpatoarray.index(i)
    print i," bernilai",x

for a in numtoarray:
    x = alpatoarray[a]
    print a," bernilai",x 

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
print "jadi chipertextnya ",
print "\r"
for (m,n) in zip(input,itertools.cycle(key)):
    hasil = alpatoarray.index(m)+alpatoarray.index(n)
    if hasil > 26:
        hasil = alpatoarray.index(m)+alpatoarray.index(n)-26
    hasilarray = np.asarray(hasil)
    strhasil = str(alpatoarray[hasilarray])
    print strhasil.rstrip(),
    
    


    


