def tower_tall(i, towers):
    import copy
    towers_copy = copy.deepcopy(towers)
    t = towers_copy[i]
    towers_copy[i] = 1
    if len(towers) != sum(towers):
        return 1
    return int(t%3)


def towerBreakers(n, m):
    # Write your code here
    if n%2 == 0:
        n = 2
    else:
        n = 1
    towers = [m]*n
    player1 = True
    while len(towers) != sum(towers):
        for i,t in enumerate(towers):
            if t > 1:
                towers[i] = tower_tall(i, towers)
                player1 = not player1
                break
    if  player1:
        return 2
    return 1

print(towerBreakers(183446, 617621)) #1
print(towerBreakers(2, 6)) #1
print(towerBreakers(1, 4)) #1
 
