# version code 988
# Please fill out this stencil and submit using the provided submission script.
from matutil import *
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
Input:
- A: a list of row lists
Output:
- True if A is in echelon form
- False otherwise
Examples:
>>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
True
>>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
False
'''
    loc_p = -1
    loc_c = -1
    for i in range(len(A[0])):
        if A[0][i] != 0:
            loc_p = i
            break
    for row in A[1:]:
        for i in range(len(row)):
            if row[i] != 0:
                loc_c = i
                break
        if (loc_c <= loc_p and loc_p != -1) or (loc_p == -1 and loc_c > loc_p):
            return False
        else:
            loc_p = loc_c
    return True
    



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
Input:
- rowlist: a list of Vecs
- label_list: a list of labels establishing an order on the domain of
Vecs in rowlist
- b: a vector (represented as a list)
Output:
- Vec x such that rowlist * x is b
>>> D = {'A','B','C','D','E'}
>>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
>>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
>>> echelon_solve(U_rows, cols, b_list)
Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
'''
    new_rowlist = []
    new_b = []
    rows_left = set(range(len(rowlist)))
    new_label_list = []
    for c in label_list:
        rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
        if rows_with_nonzero != []:
            pivot = rows_with_nonzero[0]
            rows_left.remove(pivot)
            new_rowlist.append(rowlist[pivot])
            new_b.append(b[pivot])
            new_label_list.append(c)
    from vecutil import zero_vec
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(new_b))):
        c = new_label_list[j]
        row = new_rowlist[j]
        x[c] = (new_b[j] - x*row)/row[c]
    return x



## Problem 6
rowlist = [Vec({'A', 'C', 'B', 'D'},{'A': one, 'C': 0, 'B': one, 'D': one}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': 0, 'B': one, 'D': 0}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': one, 'B': 0, 'D': 0}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': 0, 'B': 0, 'D': one})] # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one,one,0,0] # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6, 3.2]
closest_vector_2 = [0, 1, 0]
closest_vector_3 = [3, 2, 1, -4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-1/6,-1/3,1/6]
projection_orthogonal_2 = [7/6,4/3,23/6]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1
