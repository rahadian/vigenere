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
# print input,'=',alpatoarray.index(input)

# for k in key:
#     print k
#     alpatoarray.index(k)
    # print k,'=',alpatoarray.index(k)

for (z,k) in zip(input,itertools.cycle(key)):
    hasil = alpatoarray.index(z)+alpatoarray.index(k)
    # hasilarray = hasil.split("\r")
    if hasil > 26:
        hasil = alpatoarray.index(z)+alpatoarray.index(k)-26
    print z,'=',alpatoarray.index(z),"+",k,'=',alpatoarray.index(k),'=',hasil
print "jadi hasilnya ",
print "\r"
for (m,n) in zip(input,itertools.cycle(key)):
    hasil = alpatoarray.index(m)+alpatoarray.index(n)
    if hasil > 26:
        hasil = alpatoarray.index(m)+alpatoarray.index(n)-26
    hasilarray = np.asarray(hasil)
    print hasilarray,'=',alpatoarray[hasilarray]

    # index = [hasilarray]
    
    


    


