from itertools import permutations

set_1 = [1, 2, 3]
set_2 = [1, 2, 3, 4]
set_3 = [1, 3, 5, 7]
set_4 = [1, 2, 2, 1]


def per(lst):
    per_all = set(permutations(lst))
    correct_perm = []

    for perm in per_all:
        check = True
        for i in range(len(perm)):
            if lst[i] == perm[i]:
                check = False
                break
        if check:
            correct_perm.append(perm)
    print(correct_perm)
    print(len(correct_perm))


per(set_1)
per(set_2)
per(set_3)
per(set_4)
