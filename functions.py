import numpy as np


# F_HIMMELBLAU is a Himmelblau function
# 	v = F_HIMMELBLAU(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value
def fH(X):
    x = X[0]
    y = X[1]
    v = (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
    return v


# F_ROSENBROCK is a Rosenbrock function
# 	v = F_ROSENBROCK(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value

def fR(X):
    x = X[0]
    y = X[1]
    v = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    return v


# f_Br is a Branin function
# 	v = f_Br(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value

def fBr(X):
    x1 = X[0]
    x2 = X[1]
    a = 1
    b = 5.1 / (4 * np.pi ** 2)
    c = 5 / np.pi
    r = 6
    s = 10
    t = 1 / (8 * np.pi)
    v = a * (x2 - b * x1 ** 2 + c * x1 - r) ** 2 + s * (1 - t) * np.cos(x1) + s
    return v

# f_Br is a Beale function
# 	v = f_Be(X)
#	INPUT ARGUMENTS:
#	X - is 2x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value

def fBe(X):
    x1 = X[0]
    x2 = X[1]

    v = (1.5 - x1 + x1*x2) ** 2 + (2.25 - x1 + x1*x2 ** 2) ** 2 + (2.625 - x1 + x1*x2 ** 3) ** 2
    return v

# f_Sph is a Beale function
# 	v = f_Sph(X)
#	INPUT ARGUMENTS:
#	X - is 3x1 vector of input variables
#	OUTPUT ARGUMENTS:
#	v is a function value

def fSph(X):
    v = np.sum(np.square(X))
    return v
