from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon


def root_method(N):
    a = intsqrt(N)
    while a*a - N < 0:
      a += 1

    while (a*a-N) != intsqrt(a*a-N)*intsqrt(a*a-N):
      a += 1
          
    b = intsqrt(a*a-N)
    return a-b

# print(root_method(55))
# print(root_method(77))
# print(root_method(146771))


# N = 367160330145890434494322103
# a = 67469780066325164
# b = 9429601150488992
# print((a*a-b*b)/N)
# divisor1 = gcd(N , a-b)
# divisor2 = N/divisor1
# print(divisor1)
# print(divisor2)


# primeset= {2,3,5,7,11,13}
# print(dumb_factor(12, primeset))
# print(dumb_factor(154, primeset))
# print(dumb_factor(2*3*3*3*11*11*13, primeset))
# print(dumb_factor(2*17, primeset))
# print(dumb_factor(2*3*5*7*19, primeset))

## Task 1
def int2GF2(i):
    '''
Returns one if i is odd, 0 otherwise.

Input:
- i: an int
Output:
- one if i is congruent to 1 mod 2
- 0 if i is congruent to 0 mod 2
Examples:
>>> int2GF2(3)
one
>>> int2GF2(100)
0
'''
    return one if i%2 == 1 else 0

# print(int2GF2(3))
# print(int2GF2(100))

## Task 2
def make_Vec(primeset, factors):
    '''
Input:
- primeset: a set of primes
- factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
with p_i in primeset
Output:
- a vector v over GF(2) with domain primeset
such that v[p_i] = int2GF2(a_i) for all i
Example:
>>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
True
'''
    returnVecSet = {}
    for entry in factors:
      returnVecSet[entry[0]] = int2GF2(entry[1])

    return Vec(primeset, returnVecSet)

# print(make_Vec({2,3,5,7,11}, [(3,1)]) == Vec({3, 2, 11, 5, 7},{3: one}))
# print(make_Vec({2,3,5,7,11}, [(2,17), (3, 0), (5,1), (11,3)]) == Vec({3, 2, 11, 5, 7},{11: one, 2: one, 3: 0, 5: one}))


## Task 3
def find_candidates(N, primeset):
    '''
Input:
- N: an int to factor
- primeset: a set of primes

Output:
- a list [roots, rowlist]
- roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
over primeset
- rowlist: a list such that rowlist[i] is a
primeset-vector over GF(2) corresponding to a_i
such that len(roots) = len(rowlist) and len(roots) > len(primeset)
'''
    roots = []
    rowlist = []
    x = intsqrt(N)+2

    while len(roots) <= len(primeset):
      xSquareMinN = x*x - N
      factorPair = dumb_factor(xSquareMinN , primeset)
      if len(factorPair) > 0:
        vecF = make_Vec(primeset, factorPair)
        roots.append(x)
        rowlist.append(vecF)
      x += 1

    return (roots, rowlist)

# print(find_candidates(2419, primes(32)))


## Task 4
def find_a_and_b(v, roots, N):
    '''
Input:
- a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
- a list roots of integers
- an integer N to factor
Output:
a pair (a,b) of integers
such that a*a-b*b is a multiple of N
(if v is correctly chosen)
'''
    alist = [ roots[k] for k in v.D if v[k] == one]
    a = 1
    for i in alist:
      a = a*i
    c = 1
    for x in alist:
      c = c*(x*x-N)
    b = intsqrt(c)
    assert(b*b == c)

    return (a,b)



# v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: one, 2: one, 4: 0, 5: one, 11: one})
# N = 2419
# roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
# print(find_a_and_b(v, roots, N))

# v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})
# N = 2419
# roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
# print(find_a_and_b(v, roots, N))


## Task 5

# N = 2461799993978700679
# primelist = primes(10000)
# (roots,rowlist) = find_candidates(N, primelist)
# M = echelon.transformation_rows(rowlist,sorted(primelist, reverse=True))
# chosen_row = len(M)-1
# v = M[chosen_row]
# (a,b) = find_a_and_b(v, roots, N)

# while gcd(a-b,N) == 1:
# chosen_row -= 1
# v = M[chosen_row]
# (a,b) = find_a_and_b(v, roots, N)
  

# print(a)
# print(b)
# a = 1561013775490865479164576019873843952932792003446006038506066172004642900831604625028334082893638292298093457761994464845846601977721373722270810598635724466304559034512227486267040403044846375714165331621326331347367111467398099747964943167035592520654911915220416946552100867299651303888024448966844849377307301186817654175474037384408995546294096729007415341618329364076465463246320799723200496280585049718257662430590332089753307239072730891475730041268390605700466357738721315099396516948148851732023685253548039725450815994418298031974283672910698906144938050336209615471215403218406126104596209835536909813839758611286288744758890204657034889573185695147292561556614665095152406290607441275624755975994105576853865256963206740934007337628354392396708408978536479661319667314479061589591849877456538161418333175878872718324531200000000000000000000000
# b = 2164237433506392103020677286191026474505882811002838428346557468508595092945613858515988144351902891909860507757020811906018016322198497881313131747112869246661191146525785171470054643454374144185809692514453815732221567489127178315513856827475778019485910859828788146655939573355230315317226453754962031139641774746857801884105935674693012466457790348390968326610412841315579130249301711783428690119506564264438366439444921979671335337796550837796775754551557682277459221402133729559316616620237082163923665358126674207214062537886740294861176072596023175812522946428153896484375000000000000000000000000
# gcdN = gcd(a-b,N)
# print(gcdN)
smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561 
