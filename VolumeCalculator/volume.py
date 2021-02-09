import math  # access math module to get pi constant


def volcube(a):
    v = a * a * a  # takes an argument, and applies it to the formula for cube
    return v


def volpyramid(b, h):
    v = (1/3) * (b * b) * h  # takes 2 arguments, and applies it to the formula for pyramid
    return v


def volellipsoid(r1, r2, r3):
    v = (4.0/3.0) * math.pi * r1 * r2 * r3  # takes 3 arguments, and applies it to the formula for ellipsoid
    return v
