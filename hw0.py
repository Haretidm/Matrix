# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [i for i in L if i%num!=0]



## Problem 2
def myLists(L): return [list(range(1, i+1)) for i in L]



## Problem 3
def myFunctionComposition(f, g): return {k:g[f[k]] for k in f.keys()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c = -1+0.001j
complex_addition_d = 0.001+9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    sum = 0
    for i in L:
        sum += i
    return sum



## Problem 7
def myProduct(L):
    pro = 1
    for i in L:
        pro *= i
    return pro



## Problem 8
def myMin(L):
    mini = L[0]
    for i in L:
        if i<mini:
            mini = i
    return mini



## Problem 9
def myConcat(L):
    con = ""
    for i in L:
        con += i
    return con



## Problem 10
def myUnion(L):
    uni = set()
    for i in L:
        uni |= i
    return uni

