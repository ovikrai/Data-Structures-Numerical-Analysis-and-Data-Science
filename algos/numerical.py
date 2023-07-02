#################################################################################
# --------------------SOLUTIONS FOR EQUATIONS OF ONE VARIABLE ------------------#
#################################################################################
from scipy.misc import derivative
from algos.utils import Matrix, MatrixNull


# ------------------- BISECTION METHOD ----------------- #
# To ﬁnd a solution to f(x) = 0 given
# the continuous function f on the interval [a, b],
# where f(a) and f(b) have opposite signs:
# ------------- INPUT --------------- #
# Continuous function: f
# Endpoints: a, b
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure.
def bisection(f, a: float, b: float, tol: float, n: int) -> float or None:
    print('########## START: BISECTION METHOD #########')
    # Step 1: Set variables
    i = 0
    fa = f(a)
    p: float

    # Step 2: Iterations begin
    while i <= n:
        # Step 3: Compute p and set fp
        p = float(a + (b - a) / 2)
        fp = f(p)

        # Step 4: If check pass, procedure is complete
        if fp == 0 or (b - a) / 2 < tol:
            print('########## OUTPUT:', p)
            print('########## END: BISECTION METHOD ######### \n')
            return p

        # Step 4.1: Printing variables per iteration information
        print('########## interation i =', i)
        print('########## a =', a)
        print('########## b =', b)
        print('########## p =', p)
        print('########## fp =', fp)

        # Step 5: Increment the iterator
        i = i + 1

        # Step 6: Compute a and b,  or keep fp unchanged
        fa_by_fp = fa * fp
        if fa_by_fp > 0:
            a = p
            fa = fp
        else:
            b = p

    # Step 7: The procedure was unsuccessful
    print('########## Method failed after', n, 'iterations')
    print('########## OUTPUT:', None)
    print('########## END: BISECTION METHOD ######### \n')
    return None


# ------------------- FIXED-POINT ITERATION METHOD ----------------- #
# To ﬁnd a solution to p = g(p) given an initial approximation p_init
# ------------- INPUT --------------- #
# Continuous function: g
# Initial Approximation: p_init
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure.
def fixed_point_iteration(f, p_init: float, tol: float, n: int) -> float or None:
    print('########## START: FIXED POINT ITERATION METHOD #########')
    # Step 1: Set variables
    i = 0
    p: float

    # Step 2: Start repetition structure
    while i <= n:
        # Step 3: Compute p
        p = f(p_init)

        # Step 4: Check for successful procedure and output
        if abs(p - p_init) < tol:
            print('########## OUTPUT:', p)
            print('########## END: FIXED POINT ITERATION METHOD ######### \n')
            return p

        # Step 4.1: Printing variables per iteration information
        print('########## interation i =', i)
        print('########## p =', p)
        print('########## p_init =', p_init)

        # Step 5: Increment the iterator
        i = i + 1

        # Step 6: update p_init
        p_init = p

    # Step 7: The procedure was unsuccessful
    print('########## Method failed after ', n, ' iterations')
    print('########## OUTPUT:', None)
    print('########## END: FIXED POINT ITERATION METHOD ######### \n')
    return None


# ------------------- NEWTON'S METHOD ----------------- #
# To ﬁnd a solution to f(x) = 0 given an initial approximation p_init
# ------------- INPUT --------------- #
# Continuous function: f
# Initial Approximation: p_init
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure
def newton(f, p_init: float, tol: float, n: int):
    print('########## START: NEWTON METHOD #########')
    # Step 1: Set Variables
    i = 0
    p: float
    d: float
    fp: float

    # Step 2: Iteration Begins
    while i <= n:
        # Step 3: Compute p
        df = derivative(f, p_init)
        fp = f(p_init)
        p = p_init - (fp / df)

        # Step 4: Check if procedure was successful
        if abs(p - p_init) < tol:
            print('########## OUTPUT:', p)
            print('########## END: NEWTON METHOD ######### \n')
            return p

        # Step 4.1: Print iteration info
        print('########## interation i =', i)
        print('########## p =', p)
        print('########## p_init =', p_init)

        # Step 5: Increment iterator
        i = i + 1

        # Step 6: Update p_init
        p_init = p

    # Step 7: The procedure was unsuccessful
    print('########## Method failed after ', n, ' iterations')
    print('########## OUTPUT:', None)
    print('########## END: NEWTON METHOD ######### \n')
    return None


# ------------------- SECANT METHOD ----------------- #
# To ﬁnd a solution to f(x) = 0 given an initial approximations p_0 and p_1
# ------------- INPUT --------------- #
# Continuous function: f
# Initial Approximations: p_0, p_1
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure
def secant(f, p_0: float, p_1: float, tol: float, n: int):
    print('########## START: SECANT METHOD #########')
    # Step 1: set  variable
    i = 2
    q_0 = f(p_0)
    q_1 = f(p_1)

    # Step 2: start iteration
    while i <= n:
        # Step 3: Compute p
        p = p_1 - ((q_1 * (p_1 - p_0)) / (q_1 - q_0))

        # Step 4: Check for successful procedure
        if abs(p - p_1) < tol:
            print('########## OUTPUT:', p)
            print('########## END: SECANT METHOD ######### \n')
            return p

        # Step 4.1: Print iteration info
        print('########## interation i =', i)
        print('########## p =', p)
        print('########## p_0 =', p_0)
        print('########## p_1 =', p_1)
        print('########## q_0 =', q_0)
        print('########## q_1 =', q_1)

        # Step 5: increment iterator
        i = i + 1

        # Step 6: Update p_0, q_0, p_1, p_1
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f(p)

    # Step 7: Procedure unsuccessful
    print('########## Method failed after ', n, ' iterations')
    print('########## OUTPUT:', None)
    print('########## END: NEWTON METHOD ######### \n')
    return None


# ------------------- FALSE POSITION METHOD ----------------- #
# To ﬁnd a solution to f(x) = 0
# given the continuous function f on the interval [p_0 , p_1]
# where f(p_0) and f(p_1) have opposite signs:
# ------------- INPUT --------------- #
# Continuous function: f
# Initial Approximations: p_0, p_1
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure
def false_position(f, p_0: float, p_1: float, tol: float, n: int):
    print('########## START: FALSE POSITION METHOD ######### \n')
    # Step 1: Set variables
    i = 2
    q_0 = f(p_0)
    q_1 = f(p_1)
    q: float

    # Step 2: Iteration Start
    while i <= n:
        # Step 3: Compute p
        p = p_1 - ((q_1 * (p_1 - p_0)) / (q_1 - q_0))

        # Step 4: Check if procedure was successful
        if abs(p - p_1) < tol:
            print('########## OUTPUT:', p)
            print('########## END: FALSE POSITION METHOD ######### \n')
            return p

        # Step 4.1: Print iteration info
        print('########## interation i =', i)
        print('########## p =', p)
        print('########## p_0 =', p_0)
        print('########## p_1 =', p_1)
        print('########## q_0 =', q_0)
        print('########## q_1 =', q_1)

        # Step 5: Increment iterator
        i = i + 1
        q = f(p)

        # Step 6: Check for update of p_0, q_0
        if q * q_1 < 0:
            p_0 = p_1
            q_0 = q_1

        # Step 7: Update p_1, q_1
        p_1 = p
        q_1 = q

    # Step 8: Output for unsuccessful procedure
    print('########## Method failed after ', n, ' iterations')
    print('########## OUTPUT:', None)
    print('########## END: FALSE POSITION METHOD ######### \n')
    return None


# ------------------- STEFFENSEN METHOD ----------------- #
# To ﬁnd a solution to p = f(p) given initial approximation p_0
# ------------- INPUT --------------- #
# Continuous function: f
# Initial Approximation: p_0
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure
def steffensen(f, p_0: float, tol: float, n: int):
    print('########## START: STEFFENSEN METHOD #########')
    # Step 1: Set variables
    i = 1

    # Step 2: Iteration Start
    while i <= n:
        # Step 3: Compute p
        p_1 = f(p_0)
        p_2 = f(p_1)
        p = p_0 - (((p_1 - p_0) ** 2) / (p_2 - (2 * p_1) + p_0))

        # Step 4: Check if procedure was successful
        if abs(p - p_0) < tol:
            print('########## OUTPUT:', p)
            print('########## END: STEFFENSEN METHOD ######### \n')
            return p

        # Step 4.1: Print iteration info
        print('########## interation i =', i)
        print('########## p =', p)
        print('########## p_0 =', p_0)
        print('########## p_1 =', p_1)

        # Step 5: Increment iterator
        i = i + 1

        # Step 6: Check for update of p_0
        p_0 = p

    # Step 7: Output for unsuccessful procedure
    print('########## Method failed after ', n, ' iterations')
    print('########## OUTPUT:', None)
    print('########## END: FALSE POSITION METHOD ######### \n')
    return None


# ------------------- HORNER METHOD ----------------- #
# To evaluate the polynomial P(x) and its derivative at x_0
# ------------- INPUT --------------- #
# Degree of the polynomial: n
# List of Coefficients: [a_0 ... a_n]
# Point of Derivation: x_0
# ------------- OUTPUT --------------- #
# Polynomial and derivative pair (y, z) at point x_0
def horner(n: int, a: tuple, x_0: float) -> tuple:
    print('########## START: HORNER METHOD #########')
    # Step 1: compute variables
    y = a[n]
    z = a[n]

    # Step 2: Iterate
    for i in range(n - 1, 0, -1):
        # Step 2.1: Print iteration info
        print('########## interation i =', i)
        print('########## y =', y)
        print('########## z =', z)
        print('########## a_i =', a[i])

        y = (x_0 * y) + a[i]
        z = (x_0 * z) + y

    # Step 3: Update
    y = (x_0 * y) + a[0]

    # Step 4: Output
    print('########## OUTPUT:', 'P(x) =', y, ', P`(x) =', z)
    print('########## END: HORNER METHOD ######### \n')
    return y, z


# ------------------- MULLER METHOD ----------------- #
# To ﬁnd a solution to f(x) = 0
# given three approximation, p_0, p_1, p_2
# ------------- INPUT --------------- #
# Continuous function: f
# Initial Approximations: p_0, p_1, p2
# Tolerance: tol
# Maximum number of iterations: n
# ------------- OUTPUT --------------- #
# Approximate solution p or message of failure
def muller(f, p_0: float, p_1: float, p_2: float, tol: float, n: int):
    print('########## START: MULLER METHOD #########')
    # Step 1: Set variables
    h_1 = p_1 - p_0
    h_2 = p_2 - p_1
    del_1 = (f(p_1) - f(p_0)) / h_1
    del_2 = (f(p_2) - f(p_1)) / h_2
    d = (del_2 - del_1) / (h_2 + h_1)
    i = 3

    # Step 2: Iteration Start
    while i <= n:
        # Step 3: Compute b and D
        # Note: May require complex arithmetic.
        b = del_2 + (h_2 * d)
        D = ((b ** 2) - (4 * f(p_2) * d)) ** (1 / 2)

        # Step 4: Set E value
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        # Step 5: set h and p value
        h = (-2 * f(p_2)) / E
        p = p_2 + h

        # Step 6: Check if procedure was successful
        if abs(h) < tol:
            print('########## OUTPUT:', p)
            print('########## END: MULLER METHOD ######### \n')
            return p

        # Step 6.1: Print iteration info
        print('########## interation i =', i)
        print('########## p =', p)
        print('########## p_0 =', p_0)
        print('########## p_1 =', p_1)
        print('########## p_2 =', p_2)
        print('########## h_1 =', h_1)
        print('########## h_2 =', h_2)
        print('########## del_1 =', del_1)
        print('########## del_2 =', del_2)
        print('########## d =', d)

        # Step 7: Update Variables
        p_0 = p_1
        p_1 = p_2
        p_2 = p
        h_1 = p_1 - p_0
        h_2 = p_2 - p_1
        del_1 = (f(p_1) - f(p_0)) / h_1
        del_2 = (f(p_2) - f(p_1)) / h_2
        d = (del_2 - del_1) / (h_2 + h_1)
        i = i + 1

    # Step 7: Output for unsuccessful procedure
    print('########## Method failed after ', n, ' iterations')
    print('########## OUTPUT:', None)
    print('########## END: MULLER METHOD ######### \n')
    return None


# ------------------- NEVILLE ITERATED INTERPOLATION METHOD ----------------- #
# To evaluate the interpolating polynomial P
# On the n + 1 distinct numbers x_0 ... x_n
# At the the number x for the function f
# ------------- INPUT --------------- #
# Function Value list: f
# Numbers list: a
# interpolation at value: x
# ------------- OUTPUT --------------- #
# Matrix Q
def neville(f: list, a: list, x: float):
    print('########## START: NEVILLE INTERPOLATION METHOD #########')

    n = len(a)
    Q: Matrix = []

    # Matrix initialization with Zeros
    for i in range(0, n, 1):
        Q.append([f[i]])
        for j in range(0, n - 1, 1):
            Q[i].append(0)

    # Step 1: Iterations
    for i in range(1, n, 1):
        for j in range(1, i + 1, 1):
            # Step 1.1: Print iteration info
            print('########## x =', x)
            print('########## interation i =', i)
            print('########## interation j =', j)
            print('########## a[i] =', a[i])
            print('########## a[i - j] =', a[i - j])
            print('########## Q[i][j-1] =', Q[i][j - 1])
            print('########## Q[i-1][j-1] =', Q[i - 1][j - 1])

            # Step 1.2: Calculate Quotient
            N = ((x - a[i - j]) * Q[i][j - 1]) - ((x - a[i]) * Q[i - 1][j - 1])
            D = (a[i] - a[i - j])
            Q[i][j] = N / D

            # Step 1.3: Print iteration result for debugging
            print('########## N =', N)
            print('########## D =', D)
            print('########## Q[i][j] = N / D =', Q[i][j])

    # Step 2: Output
    print('########## OUTPUT:')
    for i in range(0, n):
        print(Q[i])
    print('########## END: NEWTON DIVIDED DIFFERENCE METHOD ######### \n')
    return Q


# ------------------- NEWTON'S DIVIDED-DIFFERENCE FORMULA METHOD ----------------- #
# To obtain the divided-difference coefficients of the interpolatory polynomial P
# On the n + 1 distinct numbers x_0 ... x_n
# At the number x for the function f
# ------------- INPUT --------------- #
# Function Value list: f
# Numbers list: a
# ------------- OUTPUT --------------- #
# List A
def newton_divided_difference(f: list, a: list):
    print('########## START: NEWTON DIVIDED DIFFERENCE METHOD #########')
    n = len(a)
    F: Matrix = []

    # Matrix initialization
    for i in range(0, n, 1):
        # Initialize with function provided values
        F.append([f[i]])
        for j in range(0, n - 1, 1):
            # Matrix initialization with Zeros
            F[i].append(0)

    # Step 1: Iterations
    for i in range(1, n, 1):
        for j in range(1, i + 1, 1):
            # Step 1.1: Print iteration info
            print('########## interation i =', i)
            print('########## interation j =', j)
            print('########## a[i] =', a[i])
            print('########## a[i - j] =', a[i - j])
            print('########## F[i][j-1] =', F[i][j - 1])
            print('########## F[i-1][j-1] =', F[i - 1][j - 1])

            # Step 1.2: Calculate Quotient
            N = F[i][j - 1] - F[i - 1][j - 1]
            D = a[i] - a[i - j]

            F[i][j] = N / D

            # Step 1.3: Print quotient result for debugging
            print('########## N =', N)
            print('########## D =', D)
            print('########## F[i][j] = N / D =', F[i][j])

    # Step 2: Output
    print('########## OUTPUT:')
    for i in range(0, n):
        print(F[i])
    print('########## END: NEWTON DIVIDED DIFFERENCE METHOD ######### \n')
    return F


# ------------------- HERMITE INTERPOLATION FORMULA METHOD ----------------- #
# To obtain the coefficients of the Hermite interpolating polynomial H
# On the n + 1 distinct numbers x_0 ... x_n
# At the number x for the function f
# ------------- INPUT --------------- #
# Function Value list: f
# Derivative Function Value list: df
# Numbers list: a
# ------------- OUTPUT --------------- #
# Matrix Q
def hermite_interpolation(f: list, df: list, a: list):
    print('########## START: HERMITE INTERPOLATION METHOD #########')

    n = len(a)
    Q: Matrix = []

    # Matrix and list initialization with Zeros
    for i in range(0, 2 * n, 1):
        Q.append([])
        for j in range(0, 2 * n, 1):
            Q[i].append(0)
            # Initialize with function f provided value
            Q[i][0] = f[i // 2]

    # First Divided Difference
    for i in range(1, 2 * n, 1):
        if i % 2 == 0:
            N = f[i // 2] - f[i // 2 - 1]
            D = a[i // 2] - a[i // 2 - 1]
            Q[i][1] = N / D

        if i % 2 != 0:
            Q[i][1] = df[i // 2]  # derivative of function f values

    print(Q)

    # Iteration on Divided Difference
    for i in range(2, 2 * n, 1):
        for j in range(2, i + 1, 1):
            # Step 1.1: Print iteration info

            # Step 1.2: Calculate Quotient
            N = Q[i][j - 1] - Q[i - 1][j - 1]
            D = a[i // 2] - a[(i - j) // 2]

            Q[i][j] = N / D

            # Step 1.3: Print quotient result for debugging
            print('########## N =', N)
            print('########## D =', D)
            print('########## Q[i][j] = N / D =', Q[i][j])

    # Step 3: Output
    print('########## OUTPUT:')
    for i in range(0, 2 * n):
        print(Q[i])
    print('########## END: HERMITE INTERPOLATION METHOD ######### \n')
    return Q


# ------------------- NATURAL CUBIC SPLINE METHOD ----------------- #
# To construct the cubic spline interpolant S for the function f
# On the n + 1 distinct numbers x_0 ... x_n
# At the number x for the function f
# ------------- INPUT --------------- #
# n-distinct real number list: x
# Function Value list: a
# ------------- OUTPUT --------------- #
# Matrix S
# TODO: ADD DEBUG INFO FOR PRINTING
def natural_cubic_spline(a: list, x: list):
    print('########## START: NATURAL CUBIC SPLINE METHOD #########')
    n = len(a)

    S: Matrix = []
    h: list = []
    el: list = []
    mu: list = []
    z: list = []
    alpha: list = []
    b: list = []
    c: list = []
    d: list = []

    # List initialization with Zeros
    for i in range(0, n, 1):
        h.append(0)
        z.append(0)
        el.append(0)
        mu.append(0)
        alpha.append(0)
        b.append(0)
        c.append(0)
        d.append(0)

    # Step 1: Initialization of h
    for i in range(0, n, 1):
        if i == 0:
            h[i] = x[i + 1] - x[i]
        else:
            h[i] = x[i] - x[i - 1]

    # Step 2: Alpha initialization
    for i in range(1, n - 1, 1):
        D_1 = (3 / h[i]) * (a[i + 1] - a[i])
        D_0 = (3 / h[i - 1]) * (a[i] - a[i - 1])

        alpha[i] = D_1 - D_0

    # Step 3: initialization of el
    # Solve a tridiagonal linear system
    el[0] = 1

    # Step 4: Iteration of el, mu, z
    for i in range(1, n - 1, 1):
        el[i] = (2 * (x[i + 1] - x[i - 1])) - (h[i - 1] * mu[i - 1])
        mu[i] = h[i] / el[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / el[i]

    # Step 5: End of iteration
    el[n - 1] = 1
    z[n - 1] = 0
    c[n - 1] = 0

    # Step 6: Populate b, c, d
    for j in range(n - 1, 0, -1):
        c[j - 1] = z[j - 1] - (mu[j - 1] * c[j])
        b[j - 1] = ((a[j] - a[j - 1]) / h[j - 1]) - ((h[j - 1] * (c[j] + (2 * c[j - 1]))) / 3)
        d[j - 1] = (c[j] - c[j - 1]) / (3 * h[j - 1])

        if j == 0:
            c[j] = z[j] - (mu[j] * c[j + 1])
            b[j] = ((a[j + 1] - a[j]) / h[j]) - ((h[j] * (c[j + 1] + (2 * c[j]))) / 3)
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Step 6.1: End of iteration
    a[n - 1] = 0

    # Step 6.2: Append a, b, c, d to Matrix S
    S.append(a)
    S.append(b)
    S.append(c)
    S.append(d)

    # Step 7: Output
    print('########## OUTPUT:')
    for i in range(0, n):
        print(S[i])
    print('########## END: NATURAL CUBIC SPLINE METHOD ######### \n')
    return S


# ------------------- CLAMPED CUBIC SPLINE METHOD ----------------- #
# To construct the cubic spline interpolant S for the function f
# On the n + 1 distinct numbers x_0 ... x_n
# At the number x for the function f
# And derivatives f'(x_0) and f'(x_n)
# ------------- INPUT --------------- #
# n-distinct real number list: x
# Function Value list: a
# ------------- OUTPUT --------------- #
# Matrix S
def clamped_cubic_spline(a: list, x: list, df_0: float, df_n: float):
    print('########## START: CLAMPED CUBIC SPLINE METHOD #########')
    n = len(a)

    S: Matrix = []
    h: list = []
    el: list = []
    mu: list = []
    z: list = []
    alpha: list = []
    b: list = []
    c: list = []
    d: list = []

    # List initialization with Zeros
    for i in range(0, n, 1):
        h.append(0)
        z.append(0)
        el.append(0)
        mu.append(0)
        alpha.append(0)
        b.append(0)
        c.append(0)
        d.append(0)

    # Step 1: Initialization of h
    for i in range(0, n, 1):
        if i == 0:
            h[i] = x[i + 1] - x[i]
        else:
            h[i] = x[i] - x[i - 1]

    # Step 2: Alpha initialization
    alpha[0] = ((3 / h[0]) * (a[1] - a[0])) - (3 * df_0)
    alpha[n - 1] = (3 * df_n) - ((3 / h[n - 2]) * (a[n - 1] - a[n - 2]))

    # Step 3: Alpha Iteration
    for i in range(1, n - 1, 1):
        D_1 = (3 / h[i]) * (a[i + 1] - a[i])
        D_0 = (3 / h[i - 1]) * (a[i] - a[i - 1])
        alpha[i] = D_1 - D_0

    # Step 4: initialization of el
    # Solve a tridiagonal linear system
    el[0] = 2 * h[0]
    mu[0] = 1 / 2
    z[0] = alpha[0] / el[0]

    # Step 5: Iteration of el, mu, z
    for i in range(1, n - 1, 1):
        el[i] = (2 * (x[i + 1] - x[i - 1])) - (h[i - 1] * mu[i - 1])
        mu[i] = h[i] / el[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / el[i]

    # Step 6: End of iteration
    el[n - 1] = h[n - 2] * (2 - mu[n - 2])
    z[n - 1] = (alpha[n - 1] - (h[n - 2] * z[n - 2])) / el[n - 1]
    c[n - 1] = z[n - 1]

    # Step 7: Populate b, c, d
    for j in range(n - 1, 0, -1):
        c[j - 1] = z[j - 1] - (mu[j - 1] * c[j])
        b[j - 1] = ((a[j] - a[j - 1]) / h[j - 1]) - ((h[j - 1] * (c[j] + (2 * c[j - 1]))) / 3)
        d[j - 1] = (c[j] - c[j - 1]) / (3 * h[j - 1])

        # TODO: CHECK THIS LOGIC
        if j == 0:
            c[j] = z[j] - (mu[j] * c[j + 1])
            b[j] = ((a[j + 1] - a[j]) / h[j]) - ((h[j] * (c[j + 1] + (2 * c[j]))) / 3)
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Step 7.1: End of iteration
    a[n - 1] = 0
    b[n - 1] = 0
    c[n - 1] = 0
    d[n - 1] = 0

    # Step 7.2: Append a, b, c, d to Matrix S
    S.append(a)
    S.append(b)
    S.append(c)
    S.append(d)

    # Step 8: Output
    print('########## OUTPUT:')
    for i in range(0, n):
        print(S[i])
    print('########## END: CLAMPED CUBIC SPLINE METHOD ######### \n')
    return S


# ------------------- BEZIER CURVE FOR 2-POINTS METHOD ----------------- #
# To construct the cubic Bezier with 2 guide point
# ------------- INPUT --------------- #
# 2-distinct <x, y> points: z
# right guide point: right_minus
# left guide point: left_plus
# ------------- OUTPUT --------------- #
# list coeff
def bezier(p_0: tuple, p_1: tuple, left_plus: tuple, right_minus: tuple):
    print('########## START: 2-POINTS BEZIER CURVE METHOD #########')

    a_0 = p_0[0]  # x
    b_0 = p_0[1]  # y

    a_1 = 3 * (left_plus[0] - p_0[0])
    b_1 = 3 * (left_plus[1] - p_0[1])

    a_2 = 3 * (p_0[0] + right_minus[0] - (2 * left_plus[0]))
    b_2 = 3 * (p_0[1] + right_minus[1] - (2 * left_plus[1]))

    a_3 = p_1[0] - p_0[0] + (3 * left_plus[0]) - (3 * right_minus[0])
    b_3 = p_1[1] - p_0[1] + (3 * left_plus[1]) - (3 * right_minus[1])

    coeff = [a_0, a_1, a_2, a_3, b_0, b_1, b_2, b_3]

    print('########## OUTPUT:')
    print(coeff)
    print('########## END: 2-POINTS BEZIER CURVE METHOD ######### \n')
    return coeff


# ------------------- BEZIER CURVE FOR N-POINTS METHOD ----------------- #
# To construct the cubic Bezier with 2 guide point
# ------------- INPUT --------------- #
# N-distinct <x, y> points: p
# right guide points: g_R
# left guide points: g_L
# first guide point: g_0
# last guide point: g_n
# ------------- OUTPUT --------------- #
# Matrix R
def bezier_curve(p: list, g_R: list, g_L: list, g_0: tuple, g_n: tuple):
    print('########## START: N-POINTS BEZIER CURVE METHOD #########')
    n = len(p)
    R: Matrix = []
    R_0: list
    R_i: list
    R_n: list

    # Step 1: Iteration
    for i in range(0, n - 1, 1):
        print('########## ITERATION: i =', i)
        if i == 0:
            R_0 = bezier(p[0], p[1], g_0, g_L[0])
            R.append(R_0)
        elif i == n - 2:
            R_n = bezier(p[i], p[i + 1], g_R[i - 1], g_n)
            R.append(R_n)
        else:
            R_i = bezier(p[i], p[i + 1], g_R[i - 1], g_L[i - 2])
            R.append(R_i)

    print('########## OUTPUT:')
    print(R)
    print('########## END: N-POINTS BEZIER CURVE METHOD ######### \n')
    return R


# ------------------- DE CASTELJAU METHOD ----------------- #
# Evaluate polynomials in Bernstein form (aka Bezier curves)
# ------------- INPUT --------------- #
# variable: t
# list of coefficients: coeff
# ------------- OUTPUT --------------- #
# Float, first element of beta
def casteljau(t: float, coeff: list):
    print('########## START: CASTELJAU METHOD #########')
    # values in this list are overridden
    beta = [c for c in coeff]

    n = len(beta)

    for i in range(1, n):
        for j in range(0, n - i, 1):
            beta[j] = beta[j] * (1 - t) + beta[j + 1] * t

    print('########## OUTPUT:')
    print(beta[0])
    print('########## END: CASTELJAU METHOD ######### \n')
    return beta[0]


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
# Matrix R
# TODO: TEST METHOD WITH A EXAMPLE
def romberg(f, a: float, b: float, n: int):
    R: Matrix = []
    S = 0

    # Matrix initialization with Zeros
    for i in range(0, n, 1):
        R.append([])
        for j in range(0, n - 1, 1):
            R[i].append(0)

    # Step 1: Set Variables
    h = b - a
    R[1][1] = (h / 2) * (f(a) + f(b))

    # Step 2: Print OUTPUT
    print(R[1][1])

    # Step 3: Iteration
    for i in range(2, n, 1):

        # Step 4: Approximation from Trapezoidal Method
        for k in range(1, int(2 ** (i - 2)), 1):
            S = S + f(a + (k - (1 / 2)) * h)

        R[2][1] = (1 / 2) * (R[1][1] + (h * S))

        # Step 5: Extrapolation
        for j in range(2, i, 1):
            D = R[2][j - 1] - R[1][j - 1]
            N = (4 ** (j - 1)) - 1
            R[2][j] = R[2][j - 1] + (D / N)

        # Step 6: Print OUTPUT
        for j in range(1, i, 1):
            print(R[2][j])

        # Step 7: Update variables
        h = h / 2

        # Step 8: Update Row
        for j in range(1, i, 1):
            R[1][j] = R[2][j]

    print(R)
