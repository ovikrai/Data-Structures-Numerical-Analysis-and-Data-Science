from algos.utils import Matrix, MatrixNull
import numpy
import math
import collections
import scipy

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
# TODO: CHECK LOGIC
def adaptive_quadrature(f, a, b, n, tol, m=20):
    # STEP 1: SET VARIABLES
    APP = 0.0

    TOL = []
    A   = []
    H   = []
    FA  = []
    FC  = []
    FB  = []
    S   = []
    L   = []

    i = 0
    TOL.append(0)
    A.append(0)
    H.append(0)
    FA.append(0)
    FC.append(0)
    FB.append(0)
    S.append(0)
    L.append(0)

    # ADD INIT VALUES i = 0
    i = i + 1
    TOL.append(10.0 * tol)
    A.append(a)
    H.append((b - a) / 2)
    FA.append(f(a))
    FC.append(f(a + H[i]))
    FB.append(f(b))
    S.append(H[i] * (FA[i] + (4.0 * FC[i]) + FB[i]) / 3.0)
    L.append(1.0)

    # STEP 2
    while i > 0:
        print('ENTERING WHILE LOOP. i = ', i)
        # STEP 3
        FD = f(A[i] + (H[i] / 2))
        FE = f(A[i] + (3 * (H[i] / 2)))

        # Approximations from Simpson's method for halves of sub-intervals
        S1 = H[i] * (FA[i] + (4 * FD) + FC[i]) / 6.0
        S2 = H[i] * (FC[i] + (4 * FE) + FB[i]) / 6.0

        # SAVE DATA AT THIS LEVEL
        v1 = A[i]
        v2 = FA[i]
        v3 = FC[i]
        v4 = FB[i]
        v5 = H[i]
        v6 = TOL[i]
        v7 = S[i]
        v8 = L[i]

        print('variables: ',i,v1,v2,v3,v4,v5,v6,v7,v8)
        print('APP, STEP 3:', APP)


        # STEP 4: DELETE THE LEVEL
        i = i - 1
        print('EXITING WHILE LOOP. i = ', i)

        # STEP 5
        if math.fabs((S1 + S2) - v7) < v6:
            APP = APP + (S1 + S2)
            print('ENTERING IF. APP, STEP 5:', APP)
        else:
            if v8 >= n:
                # PROCEDURE FAILS
                print('LEVEL EXCEEDED')
                break
            else:
                # DATA FOR RIGHT HALF SUB-INTERVAL
                # ADD ONE LEVEL
                i = i + 1
                A.append(v1 + v5)
                FA.append(v3)
                FC.append(FE)
                FB.append(v4)
                H.append(v5 / 2)
                TOL.append(v6 / 2)
                S.append(S2)
                L.append(v8 + 1)


                # DATA FOR LEFT HALF SUB-INTERVAL
                # ADD ONE LEVEL
                i = i + 1
                A.append(v1)
                FA.append(v2)
                FC.append(FD)
                FB.append(v3)
                H.append(H[i - 1])
                TOL.append(TOL[i -1])
                S.append(S1)
                L.append(L[i - 1])



    # APP APPROXIMATES INTEGRAL TO WITHIN TOL
    return APP


# ADAPTIVE QUADRATURE WITH SIMPSONS RULES RECURSIVE VERSION
# TODO: study the recursive version
def _quad_simpsons_mem(f, a, fa, b, fb):
    """Evaluates the Simpson's Rule, also returning m and f(m) to reuse"""
    m = (a + b) / 2
    fm = f(m)
    return (m, fm, abs(b - a) / 6 * (fa + 4 * fm + fb))

def _quad_asr(f, a, fa, b, fb, eps, whole, m, fm):
    """
    Efficient recursive implementation of adaptive Simpson's rule.
    Function values at the start, middle, end of the intervals are retained.
    """
    lm, flm, left  = _quad_simpsons_mem(f, a, fa, m, fm)
    rm, frm, right = _quad_simpsons_mem(f, m, fm, b, fb)
    delta = left + right - whole
    if abs(delta) <= 15 * eps:
        return left + right + delta / 15
    return _quad_asr(f, a, fa, m, fm, eps/2, left , lm, flm) +\
           _quad_asr(f, m, fm, b, fb, eps/2, right, rm, frm)

def quad_asr(f, a, b, eps):
    """Integrate f from a to b using Adaptive Simpson's Rule with max error of eps."""
    fa, fb = f(a), f(b)
    m, fm, whole = _quad_simpsons_mem(f, a, fa, b, fb)
    return _quad_asr(f, a, fa, b, fb, eps, whole, m, fm)
