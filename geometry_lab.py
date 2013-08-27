from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
In case you have never seen this notation for a parameter before,
the way it works is that identity() now defaults to having labels
equal to {'x','y','u'}. So you should write your procedure as if
it were defined 'def identity(labels):'. However, if you want the labels of
your identity matrix to be {'x','y','u'}, you can just call
identity(). Additionally, if you want {'r','g','b'}, or another set, to be the
labels of your matrix, you can call identity({'r','g','b'}).
'''
    output = Mat((labels,labels),{})
    for i in labels:
     output[i,i] = 1
    return output

## Task 2
def translation(x,y):
    '''
Input: An x and y value by which to translate an image.
Output: Corresponding 3x3 translation matrix.
'''
    output = identity()
    output['x','u'] = x
    output['y','u'] = y
    return output


## Task 3
def scale(a, b):
    '''
Input: Scaling parameters for the x and y direction.
Output: Corresponding 3x3 scaling matrix.
'''
    output = identity()
    output['x','x'] = a
    output['y','y'] = b
    return output

## Task 4
def rotation(angle):
    '''
Input: An angle in radians to rotate an image.
Output: Corresponding 3x3 rotation matrix.
Note that the math module is imported.
'''
    output = identity()
    output['x','x'] = math.cos(angle)
    output['x','y'] =-math.sin(angle)
    output['y','x'] = math.sin(angle)
    output['y','y'] = math.cos(angle)
    return output

## Task 5
def rotate_about(x,y,angle):
    '''
Input: An x and y coordinate to rotate about, and an angle
in radians to rotate about.
Output: Corresponding 3x3 rotation matrix.
It might be helpful to use procedures you already wrote.
'''
    output = translation(-x,-y)
    output = rotation(angle) * output
    output = translation(x,y) * output
    return output

## Task 6
def reflect_y():
    '''
Input: None.
Output: 3x3 Y-reflection matrix.
'''
    output = identity()
    output['x','x'] = -1
    return output

## Task 7
def reflect_x():
    '''
Inpute: None.
Output: 3x3 X-reflection matrix.
'''
    output = identity()
    output['y','y'] = -1
    return output
    
## Task 8
def scale_color(scale_r,scale_g,scale_b):
    '''
Input: 3 scaling parameters for the colors of the image.
Output: Corresponding 3x3 color scaling matrix.
'''
    output = identity(labels = {'r','g','b'})
    output['r','r'] = scale_r
    output['g','g'] = scale_g
    output['b','b'] = scale_b
    return output

## Task 9
def grayscale():
    '''
Input: None
Output: 3x3 greyscale matrix.
'''
    a = 77.0/256.0
    b = 151.0/256.0
    c = 28.0/256.0
    output = Mat(({'r','g','b'},{'r','g','b'}),
        {('r','r'):a,('r','g'):b,('r','b'):c,
        ('g','r'):a,('g','g'):b,('g','b'):c,
        ('b','r'):a,('b','g'):b,('b','b'):c})
    return output

## Task 10
def reflect_about(p1,p2):
    '''
Input: 2 points that define a line to reflect about.
Output: Corresponding 3x3 reflect about matrix.
'''
    pass

