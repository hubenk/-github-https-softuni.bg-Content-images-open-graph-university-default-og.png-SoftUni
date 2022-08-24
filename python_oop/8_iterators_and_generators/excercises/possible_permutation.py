from itertools import permutations

def possible_permutations(test_permutation):
    result = permutations(test_permutation)

    for combination in result:
        yield list(combination)


[print(n) for n in possible_permutations([1, 2, 3])]

