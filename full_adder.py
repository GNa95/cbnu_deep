import numpy as np

# AND function
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def AND_1(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# AND_1(0,0)
# AND_1(1,0)
# AND_1(0,1)
# AND_1(1,1)


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


def half_adder(x1, x2):
    s = XOR(x1, x2)
    c = AND(x1, x2)
    return s, c


def full_adder(x1, x2, c_in):
    s1 = XOR(x1, x2)
    s = XOR(s1, c_in)
    
    s2 = AND(x1, x2)
    s3 = AND(s1, c_in)
    c = OR(s2, s3)
    return c, s
    
    