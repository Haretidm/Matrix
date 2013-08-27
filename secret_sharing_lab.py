# version code 988
# Please fill out this stencil and submit using the provided submission script.


import random
from GF2 import one
from vec import Vec
from vecutil import list2vec
from independence import is_independent



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])

def choose_secret_vector(s,t):
    u = list2vec([randGF2() for i in range(6) ])
    while not ( a0*u == s and b0*u == t ):
        u = list2vec([randGF2() for i in range(6) ])
    return u


# st_combos = [(0,0),(0,one),(one,0),(one,one)]
# vecs = [[choose_secret_vector(s,t) for _ in range(50)] for s, t in st_combos]
# M = map(lambda c: len(c) > 10, vecs)
# K= M.keys()
# V = M.values()
# L = list(M)
# print(L)

def combinations(rowset,setsize):
    cb = list()
    for i in range(pow(2,len(rowset))):
        bitmap = bin(i)[2:] #ommit 0b in beginning
        elements = {len(bitmap)-b-1 for b in range(len(bitmap)) if bitmap[b]=='1'}
        if len(elements) == setsize:
            cb.append([ rowset[e] for e in elements])
    return cb


def task2():
    
    
    row = [(a0,b0)] + [
                       ( list2vec([randGF2() for i in range(6) ]),
                         list2vec([randGF2() for i in range(6) ])
                       ) for j in range(4) ]
    
    while not all(is_independent(list(sum(x,()))) for x in combinations(row,3)):
        row = [(a0,b0)] + [
                       ( list2vec([randGF2() for i in range(6) ]),
                         list2vec([randGF2() for i in range(6) ])
                       ) for j in range(4) ]
        
    return row



## Problem 2
# Give each vector as a Vec instance

secret_a0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: one})
secret_b0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: one, 4: one, 5: one})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: 0, 4: 0, 5: 0})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: one, 5: one})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: 0, 4: one, 5: 0})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: one, 4: 0, 5: 0})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: one, 4: 0, 5: 0})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: 0, 4: one, 5: 0})


# vecs = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3),(secret_a4,secret_b4)]
# print(all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)))
#
# 

