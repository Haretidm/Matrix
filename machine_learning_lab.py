import math
from mat import *
from vec import *
from cancer_data import *

## Task 1 ##
def signum(u):
    '''
Input:
- u: Vec
Output:
- v: Vec such that:
if u[d] >= 0, then v[d] = 1
if u[d] < 0, then v[d] = -1
Example:
>>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
True
'''
    return Vec(u.D , { k: 1 if u[k] >= 0 else -1 for k in u.D })

# print(signum(Vec({1,2,3},{1:2, 2:-1})))

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
Input:
- A: a Mat with rows as feature vectors
- b: a Vec of actual diagnoses
- w: hypothesis Vec
Output:
- Fraction (as a decimal in [0,1]) of vectors incorrectly
classified by w
'''
    diff = (signum(A*w)-b)
    return (diff*diff/4)/len(w.D)

# from mat import Mat
# from vec import Vec
# from vecutil import list2vec
# from matutil import listlist2mat
# A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
# b1 = list2vec([1, 1, -1, -1, 1])
# A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})
# b2 = Vec(A2.D[0], {x:(-1)**i for i, x in enumerate(sorted(A2.D[0]))})
# print(fraction_wrong(A1, b1, Vec(A1.D[1], {}))) #0.400000
# print(fraction_wrong(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}))) #0.60000
# print(fraction_wrong(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}))) #0.400000
# print(fraction_wrong(A2, b2, Vec(A2.D[1], {}))) #0.500000
# print(fraction_wrong(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}))) #0.500000
# print(fraction_wrong(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}))) #0.538462

## Task 3 ##
def loss(A, b, w):
    '''
Input:
- A: feature Mat
- b: diagnoses Vec
- w: hypothesis Vec
Output:
- Value of loss function at w for training data
'''
    diff = (A*w-b)
    return diff*diff

# from mat import Mat
# from vec import Vec
# from vecutil import list2vec
# from matutil import listlist2mat
# A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6],[10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
# b1 = list2vec([1, 1, -1, -1, 1])
# A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})
# b2 = Vec(A2.D[0], {x:(-1)**i for i,x in enumerate(sorted(A2.D[0]))})

# print(loss(A1, b1, Vec(A1.D[1], {}))) #5.000000
# print(loss(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}))) #23549.000000
# print(loss(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}))) #671.000000
# print(loss(A2, b2, Vec(A2.D[1], {}))) #26.000000
# print(loss(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}))) #340786090.000000
# print(loss(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}))) #37288544.000000

## Task 4 ##
def find_grad(A, b, w):
    '''
Input:
- A: feature Mat
- b: diagnoses Vec
- w: hypothesis Vec
Output:
- Value of the gradient function at w
'''
    diff = (A*w-b)
    return 2*diff*A


# from vec import Vec
# from mat import Mat
# from vecutil import list2vec
# from matutil import listlist2mat
# A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
# b1 = list2vec([1, 1, -1, -1, 1])
# A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})
# b2 = Vec(A2.D[0], {x:1 for x in A2.D[0]})

#print(find_grad(A1, b1, Vec(A1.D[1], {})))
#Vec({0.000000, 1.000000, 2.000000, 3.000000, 4.000000}, {0.000000: 6.000000, 1.000000: 28.000000, 2.000000: -28.000000, 3.000000: -34.000000, 4.000000: -36.000000})

# print(find_grad(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]})))
#Vec({0.000000, 1.000000, 2.000000, 3.000000, 4.000000}, {0.000000: -4474.000000, 1.000000: -4568.000000, 2.000000: -5896.000000, 3.000000: -3434.000000, 4.000000: -5108.000000})

# print(find_grad(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))})))
#Vec({0.000000, 1.000000, 2.000000, 3.000000, 4.000000}, {0.000000: 686.000000, 1.000000: 582.000000, 2.000000: 1082.000000, 3.000000: 550.000000, 4.000000: 748.000000})

# print(find_grad(A2, b2, Vec(A2.D[1], {})))
#Vec({65.000000, 66.000000, 67.000000, 68.000000, 69.000000, 70.000000, 71.000000, 72.000000, 73.000000, 74.000000, 75.000000, 76.000000, 77.000000, 78.000000, 79.000000, 80.000000, 81.000000, 82.000000, 83.000000, 84.000000, 85.000000, 86.000000, 87.000000, 88.000000, 89.000000, 90.000000}, {65.000000: -11102.000000, 66.000000: -1638.000000, 67.000000: 7826.000000, 68.000000: 17290.000000, 69.000000: -5208.000000, 70.000000: -3354.000000, 71.000000: 6110.000000, 72.000000: 15574.000000, 73.000000: 686.000000, 74.000000: -5070.000000, 75.000000: 4394.000000, 76.000000: 13858.000000, 77.000000:6580.000000, 78.000000: -6786.000000, 79.000000: 2678.000000, 80.000000: 12142.000000, 81.000000: 10952.000000, 82.000000: -8502.000000, 83.000000: 962.000000, 84.000000: 10426.000000, 85.000000: 16846.000000, 86.000000: -10218.000000, 87.000000: -754.000000, 88.000000: 8710.000000, 89.000000: 18174.000000, 90.000000: -7368.000000})

# print(find_grad(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]})))
#Vec({65.000000, 66.000000, 67.000000, 68.000000, 69.000000, 70.000000, 71.000000, 72.000000, 73.000000, 74.000000, 75.000000, 76.000000, 77.000000, 78.000000, 79.000000, 80.000000, 81.000000, 82.000000, 83.000000, 84.000000, 85.000000, 86.000000, 87.000000, 88.000000, 89.000000, 90.000000}, {65.000000: 39580534.000000, 66.000000: 5662286.000000, 67.000000: -28255962.000000, 68.000000: -62174210.000000, 69.000000: 16537064.000000, 70.000000: 11812298.000000, 71.000000: -22105950.000000, 72.000000: -56024198.000000, 73.000000: -1824734.000000, 74.000000: 17962310.000000, 75.000000: -15955938.000000, 76.000000: -49874186.000000, 77.000000: -22454312.000000, 78.000000: 24112322.000000, 79.000000: -9805926.000000, 80.000000: -43724174.000000, 81.000000: -38434180.000000, 82.000000: 30262334.000000, 83.000000: -3655914.000000, 84.000000: -37574162.000000, 85.000000: -60829278.000000, 86.000000: 36412346.000000, 87.000000: 2494098.000000, 88.000000: -31424150.000000, 89.000000: -65342398.000000, 90.000000: 23928512.000000})

# print(find_grad(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))})))
#Vec({65.000000, 66.000000, 67.000000, 68.000000, 69.000000, 70.000000, 71.000000, 72.000000, 73.000000, 74.000000, 75.000000, 76.000000, 77.000000, 78.000000, 79.000000, 80.000000, 81.000000, 82.000000, 83.000000, 84.000000, 85.000000, 86.000000, 87.000000, 88.000000, 89.000000, 90.000000}, {65.000000: -7825916.000000, 66.000000: -3615892.000000, 67.000000:594132.000000, 68.000000: 4804156.000000, 69.000000: 4685612.000000, 70.000000: -4379248.000000, 71.000000: -169224.000000, 72.000000: 4040800.000000, 73.000000: 14880656.000000, 74.000000: -5142604.000000, 75.000000: -932580.000000, 76.000000: 3277444.000000, 77.000000: 19284490.000000, 78.000000: -5905960.000000, 79.000000: -1695936.000000, 80.000000: 2514088.000000, 81.000000: 18021918.000000, 82.000000: -6669316.000000, 83.000000: -2459292.000000, 84.000000: 1750732.000000, 85.000000: 10843332.000000, 86.000000: -7432672.000000, 87.000000: -3222648.000000, 88.000000: 987376.000000, 89.000000: 5197400.000000, 90.000000: -1620988.000000})

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
Input:
- A: feature Mat
- b: diagnoses Vec
- w: hypothesis Vec
- sigma: step size
Output:
- The vector w' resulting from 1 iteration of gradient descent
starting from w and moving sigma.
'''
    # print(w)
    # print(w - sigma*find_grad(A, b, w))
    return w - sigma*find_grad(A, b, w)


# from vec import Vec
# from mat import Mat
# from vecutil import list2vec
# from matutil import listlist2mat
# A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
# b1 = list2vec([1, 1, -1, -1, 1])
# A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})
# b2 = Vec(A2.D[0], {x:1 for x in A2.D[0]})


#print(gradient_descent_step(A1, b1, Vec(A1.D[1], {}), 2))
# Vec({0.000000, 1.000000, 2.000000, 3.000000, 4.000000}, {0.000000: -12.000000, 1.000000: -56.000000, 2.000000: 56.000000, 3.000000: 68.000000, 4.000000: 72.000000})

#print(gradient_descent_step(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}), 2))
# Vec({0.000000, 1.000000, 2.000000, 3.000000, 4.000000}, {0.000000: 8946.000000, 1.000000: 9134.000000, 2.000000: 11790.000000, 3.000000: 6866.000000, 4.000000: 10214.000000})

#print(gradient_descent_step(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}), 2))
# Vec({0.000000, 1.000000, 2.000000, 3.000000, 4.000000}, {0.000000: -1371.000000, 1.000000: -1165.000000, 2.000000: -2163.000000, 3.000000: -1101.000000, 4.000000: -1495.000000})

# print(gradient_descent_step(A2, b2, Vec(A2.D[1], {}), 3))
# Vec({65.000000, 66.000000, 67.000000, 68.000000, 69.000000, 70.000000, 71.000000, 72.000000, 73.000000, 74.000000, 75.000000, 76.000000, 77.000000, 78.000000, 79.000000, 80.000000, 81.000000, 82.000000, 83.000000, 84.000000, 85.000000, 86.000000, 87.000000, 88.000000, 89.000000, 90.000000}, {65.000000: 33306.000000, 66.000000: 4914.000000, 67.000000: -23478.000000, 68.000000: -51870.000000, 69.000000: 15624.000000, 70.000000: 10062.000000, 71.000000: -18330.000000, 72.000000: -46722.000000, 73.000000: -2058.000000, 74.000000: 15210.000000, 75.000000: -13182.000000, 76.000000: -41574.000000, 77.000000: -19740.000000, 78.000000: 20358.000000, 79.000000: -8034.000000, 80.000000: -36426.000000, 81.000000: -32856.000000, 82.000000: 25506.000000, 83.000000: -2886.000000, 84.000000: -31278.000000, 85.000000: -50538.000000, 86.000000: 30654.000000, 87.000000: 2262.000000, 88.000000: -26130.000000, 89.000000: -54522.000000, 90.000000: 22104.000000})

# print(gradient_descent_step(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}), 3))
# Vec({65.000000, 66.000000, 67.000000, 68.000000, 69.000000, 70.000000, 71.000000, 72.000000, 73.000000, 74.000000, 75.000000, 76.000000, 77.000000, 78.000000, 79.000000, 80.000000, 81.000000, 82.000000, 83.000000, 84.000000, 85.000000, 86.000000, 87.000000, 88.000000, 89.000000, 90.000000}, {65.000000: -118741604.000000, 66.000000: -16986860.000000, 67.000000: 84767884.000000, 68.000000: 186522628.000000, 69.000000: -49611194.000000, 70.000000: -35436896.000000, 71.000000: 66317848.000000, 72.000000: 168072592.000000, 73.000000: 5474200.000000, 74.000000: -53886932.000000, 75.000000: 47867812.000000, 76.000000: 149622556.000000, 77.000000: 67362934.000000, 78.000000: -72336968.000000, 79.000000: 29417776.000000, 80.000000: 131172520.000000, 81.000000: 115302538.000000, 82.000000: -90787004.000000, 83.000000: 10967740.000000, 84.000000: 112722484.000000, 85.000000: 182487832.000000, 86.000000: -109237040.000000, 87.000000: -7482296.000000, 88.000000: 94272448.000000, 89.000000: 196027192.000000, 90.000000: -71785538.000000})

# print(gradient_descent_step(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}), 3))
# Vec({65.000000, 66.000000, 67.000000, 68.000000, 69.000000, 70.000000, 71.000000, 72.000000, 73.000000, 74.000000, 75.000000, 76.000000, 77.000000, 78.000000, 79.000000, 80.000000, 81.000000, 82.000000, 83.000000, 84.000000, 85.000000, 86.000000, 87.000000, 88.000000, 89.000000, 90.000000}, {65.000000: 23477749.000000, 66.000000: 10847675.000000, 67.000000: -1782395.000000, 68.000000: -14412469.000000, 69.000000: -14056835.000000, 70.000000: 13137743.000000, 71.000000: 507673.000000, 72.000000: -12122401.000000, 73.000000: -44641967.000000, 74.000000: 15427811.000000, 75.000000: 2797741.000000, 76.000000: -9832333.000000, 77.000000: -57853469.000000, 78.000000: 17717879.000000, 79.000000: 5087809.000000, 80.000000: -7542265.000000, 81.000000: -54065753.000000, 82.000000: 20007947.000000, 83.000000: 7377877.000000, 84.000000: -5252197.000000, 85.000000: -32529995.000000, 86.000000: 22298015.000000, 87.000000: 9667945.000000, 88.000000: -2962129.000000, 89.000000: -15592199.000000, 90.000000: 4862963.000000})


def gradient_descent(A, b, w, sigma, T):
    for i in range(T):
        w = gradient_descent_step(A, b, w, sigma)
    return w



# A , b = read_training_data("train.data")
# T = 100
# print(A)
# print(b)
# w1 = Vec(A.D[1] , {})
# sigma1 = 2*1E-9
# result = gradient_descent(A, b, w1, sigma1, T)
# print(result)

