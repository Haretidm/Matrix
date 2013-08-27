from image_mat_util import *
from mat import Mat
from vec import Vec
from matutil import rowdict2mat
from solver import solve

## Task 1
def move2board(v):
    '''
Input:
- v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
Output:
- A {'y1','y2','y3'}-vector z, the coordinate representation
in whiteboard coordinates of the point p such that the line through the
origin and q intersects the whiteboard plane at p.
'''
    return Vec({'y1','y2','y3'}, {'y1': v['y1']/v['y3'] , 'y2': v['y2']/v['y3'] , 'y3': 1})


# v1 = Vec({'y1','y2','y3'}, {'y1':2, 'y2': 4, 'y3': 6})
# print(move2board(v1))

## Task 2
def make_equations(x1, x2, w1, w2):
    '''
Input:
- x1 & x2: photo coordinates of a point on the board
- y1 & y2: whiteboard coordinates of a point on the board
Output:
- List [u,v] where u*h = 0 and v*h = 0
'''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1,('y3','x2'):w1*x2,('y3','x3'):w1,('y1','x1'):-x1,('y1','x2'):-x2,('y1','x3'):-1})
    v = Vec(domain, {('y3','x1'):w2*x1,('y3','x2'):w2*x2,('y3','x3'):w2,('y2','x1'):-x1,('y2','x2'):-x2,('y2','x3'):-1})
    return [u, v]


domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
[u1, v1] = make_equations(358,36,0,0)
[u2, v2] = make_equations(329,597,0,1)
[u3, v3] = make_equations(592,157,1,0)
[u4, v4] = make_equations(580,483,1,1)
w = Vec(domain, {('y1','x1'):1})

L = rowdict2mat({0:u1,1:v1,2:u2,3:v2,4:u3,5:v3,6:u4,7:v4,8:w})
b = Vec({0,1,2,3,4,5,6,7,8},{8:1})
h = solve(L,b)

## Task 3
H = Mat(({'y1','y2','y3'},{'x1','x2','x3'}),{ k:h.f[k] for k in h.f })

# (X_pts, colors) = file2mat('board.png', ('x1','x2','x3'))
# Y_pts = H * X_pts

## Task 4
def mat_move2board(Y):
    '''
Input:
- Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector
giving the whiteboard coordinates of a point q.
Output:
- Mat instance, each column of which is the corresponding point in the
whiteboard plane (the point of intersection with the whiteboard plane
of the line through the origin and q).
'''

    returnMat = Mat(Y.D,{})
    for col in Y.D[1]:
        y3_val = Y[('y3',col)]
        for row in Y.D[0]:
            returnMat[(row,col)] = Y[(row,col)] / y3_val
    return returnMat
