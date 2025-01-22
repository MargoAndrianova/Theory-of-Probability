from itertools import product

def per():
    chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    per_all = list(product(chars, repeat=6))
    correct_perm = []

    for perm in per_all:
        check = True
        if perm[0] == 0:
            continue
        for i in range(1, 6):
            if perm[i-1] == perm[i]:
                check = False
                break
        if check:
            correct_perm.append(perm)
    print(correct_perm)
    print(len(correct_perm))

if __name__ == "__main__":
    per()