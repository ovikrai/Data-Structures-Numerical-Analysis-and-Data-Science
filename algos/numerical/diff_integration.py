from algos.utils import Matrix, MatrixNull
import numpy


# ------------------- COMPOSITE SIMPSONS RULE METHOD ----------------- #
# To Approximate the integral I of function f
# ------------- INPUT --------------- #
# endpoints: a, b
# even positive integer: n
# ------------- OUTPUT --------------- #
# approximation X*I to I
def composite_simpsons_rule(f, a: float, b: float, n: int):
    print('########## START: COMPOSITE SIMPSON\'S RULE METHOD #########')
    # Step 1: sting variables
    h = (b - a) / n
    XI_0 = f(a) + f(b)
    XI_1 = 0
    XI_2 = 0

    for i in range(1, n, 1):
        X = a + (i * h)
        if i % 2 == 0:
            XI_2 = XI_2 + f(X)
        else:
            XI_1 = XI_1 + f(X)

    D = XI_0 + (2 * XI_2) + (4 * XI_1)
    XI = (h / 3) * D

    print('########## OUTPUT:')
    print(XI)
    print('########## END: COMPOSITE SIMPSON\'S RULE METHOD ######### \n')
    return XI


# ------------------- ROMBERG METHOD ----------------- #
# To Approximate the integral I of function f
# ------------- INPUT --------------- #
# endpoints: a, b
# even positive integer: n
# ------------- OUTPUT --------------- #
# Matrix r
def romberg(f, a: float, b: float, n: int):
    r: Matrix = []

    # Matrix initialization
    for i in range(0, n + 1, 1):
        # Initialize with function provided values
        r.append([])
        for j in range(0, n + 1, 1):
            # Matrix initialization with Zeros
            r[i].append(0.0)

    h = b - a
    r[0][0] = 0.5 * h * (f(a) + f(b))

    power_of_2 = 1
    for i in range(1, n + 1):
        # Compute the halved stepsize and use this to sum the function at
        # all the new points (in between the points already computed)
        h = 0.5 * h
        s = 0.0
        power_of_2 = 2 * power_of_2
        for k in range(1, power_of_2, 2):
            s = s + f(a + k * h)

        # Compute the composite trapezoid rule for the next level of
        # subdivision.  Use Richardson extrapolation to refine these values
        # into a more accurate form.
        r[i][0] = 0.5 * r[i - 1][0] + s * h

        power_of_4 = 1
        for j in range(1, i + 1):
            power_of_4 = 4 * power_of_4
            r[i][j] = r[i][j - 1] + (r[i][j - 1] - r[i - 1][j - 1]) / (power_of_4 - 1)
    return r


# ------------------- ADAPTIVE QUADRATURE ----------------- #
# TODO: NUMERIAL ALGOS
def adaptive_quadrature(f, a, b, n, tol):
    # STEP 1: SET VARIABLES
    APP = 0
    i = 1
    TOL = []
    A = []
    H = []
    FA = []
    FC = []
    FB = []
    S = []
    L = []

    # INIT LISTS
    for k in range(1, n):
        TOL.append(0)
        A.append(0)
        H.append(0)
        FA.append(0)
        FC.append(0)
        FB.append(0)
        S.append(0)
        L.append(0)

    # ADD INIT VALUES
    TOL[i] = 10.0 * tol
    A[i] = a
    H[i] = ((b - a) / 2)
    FA[i] = f(a)
    FC[i] = f(a + H[i])
    FB[i] = f(b)
    S[i] = (H[i] * (FA[i] + 4.0 * FC[i] + FB[i]) / 3.0)
    L[i] = 1.0

    # TODO: COMPLETE THE ALGO...
    while i > 0:
        print('A:', A[i])
        print('H:', H[i])
        FD = f((A[i] + H[i]) / 2)
        FE = f(A[i] + 3 * H[i] / 2)

        # Approximations from Simpson's method for halves of sub-intervals
        S1 = H[i] * (FA[i] + 4 * FD + FC[i]) / 6
        S2 = H[i] * (FC[i] + 4 * FE + FB[i]) / 6

        # SAVE DATA AT THIS LEVEL
        v1 = A[i]
        v2 = FA[i]
        v3 = FC[i]
        v4 = FB[i]
        v5 = H[i]
        v6 = TOL[i]
        v7 = S[i]
        v8 = L[i]

        # STEP 4: DELETE THE LEVEL
        i = i - 1

        if abs(S1 + S2 + v7) < v6:
            APP = APP + (S1 + S2)

        else:
            if v8 >= n:
                # PROCEDURE FAILS
                print('LEVEL EXCEEDED')
            else:
                # ADD ONE LEVEL
                i = i + 1
                # DATA FOR RIGHT HALF SUB-INTERVAL
                A[i] = (v1 + v5)
                FA[i] = v3
                FC[i] = FE
                FB[i] = v4
                H[i] = v5 / 2
                TOL[i] = v6 / 2
                S[i] = S2
                L[i] = v8 + 1

                # ADD ONE LEVEL
                i = i + 1
                # DATA FOR LEFT HALF SUB-INTERVAL
                A[i] = v1
                FA[i] = v2
                FC[i] = FD
                FB[i] = v3
                H[i] = H
                TOL[i] = v8 + 1
                S[i] = S1
                L[i] = L[i - 1]

    # APP APPROXIMATES INTEGRAL TO WITHIN TOL
    return APP
