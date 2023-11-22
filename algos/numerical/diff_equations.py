from typing import Callable


#--------------- EULER INITIAL-VALUE PROBLEM ----------#

def euler(f: Callable[[float, float],float],
          a: float, b: float,
          n: int, alpha: float) -> tuple[list, list]:
    t = [float] * n
    w = [float] * n

    h = (b - a) / n
    t[0] = a
    w[0] = alpha


    for i in range(1, n):
        w[i] = w[i - 1] + h * f(t, w[i -1])
        t[i] = a + i * h

    return t, w



