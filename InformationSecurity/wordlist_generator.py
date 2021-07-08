import itertools

string = input('type the string for permutation:ert')
result = itertools.permutations(string, 3)

for i in result:
    print(''.join(i))

