from itertools import permutations

def per(lst):
    per_all = set(permutations(lst))
    correct_perm = []

    for perm in per_all:
        check = True
        for i in range(3):
            if perm[i] >= perm[i+1]:
                check = False
                break
        for j in range(4, 8):
            if perm[j-1] <= perm[j]:
                check = False
                break
        if check:
            correct_perm.append(perm)
    print(correct_perm)
    print(len(correct_perm))

if __name__ == "__main__":
    set_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    set_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    per(set_1)
    per(set_2)
