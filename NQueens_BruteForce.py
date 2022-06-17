import itertools as it

def is_solution(perm): #checks all combinations of a given permutation
    for(i1, i2) in it.combinations(range(len(perm)), 2):
        if(abs(i1 - i2)) == abs(perm[i1] - perm[i2]):
            return False
    return True

for perm in it.permutations(range(8)): #checks all permutations
    if is_solution(perm):
        print(perm)
        exit()