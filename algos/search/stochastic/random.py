# ------------------------- Random Search ---------------------------- #
# -------------------------------------------------------------------- #
import random


def objetive_function(vector: list) -> float:
    S = 0.0
    for i in range(0, len(vector)):
        S = S + vector[i] ** 2.0
    return S


def random_vector(minmax: list) -> list:
    rv = []
    for i in range(0, len(minmax)):
        rv.append(0)

    for i in range(0, len(minmax)):
        # UNIFORM RANDOM
        rv[i] = minmax[0] + ((minmax[1] - minmax[0]) * random.random())
    return rv


# TEST TO CHECK!!!!
def random_search(search_space: list, n: int):
    best = None
    for i in range(0, n):
        candidate = {'vector': random_vector(search_space)}
        candidate['cost'] = objetive_function(candidate['vector'])

        # TODO: CHECK THIS LOGIC
        if best is None or candidate['cost'] < best['cost']:
            print(candidate)
            best = candidate
            print('iteration = ', i + 1, 'best = ', best['cost'])

    return best
