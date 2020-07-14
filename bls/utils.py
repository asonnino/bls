""" Utilities """
from hashlib import sha256
from petlib.bn import Bn


# ==================================================
# polynomial utilities
# ==================================================
def poly_eval(coeff, x):
    """ evaluate a polynomial defined by the list of coefficient coeff at point x """
    return sum([coeff[i] * (Bn(x) ** i) for i in range(len(coeff))])


def lagrange_basis(indexes, o, x=0):
    """ generates all lagrange basis polynomials """
    l = []
    for i in indexes:
        numerator, denominator = 1, 1
        for j in indexes:
            if j != i:
	            numerator = (numerator * (x - j)) % o
	            denominator = (denominator * (i - j)) % o
        l.append((numerator * denominator.mod_inverse(o)) % o)
    return l


# ==================================================
# other
# ==================================================
def ec_sum(list):
    """ sum EC points list """
    ret = list[0]
    for i in range(1, len(list)):
        ret = ret + list[i]
    return ret


def hash(elements):
    """ generates a Bn hash by hashing a number of EC points """
    Cstring = ",".join([str(x) for x in elements])
    return sha256(Cstring.encode()).digest()
