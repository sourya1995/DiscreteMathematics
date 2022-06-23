def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) ==6
    dice1_wins, dice2_wins = 0, 0


    equal = 0
    for i in range(6):
        for j in range(6):
            if dice1[i] > dice2[j]:
                dice1_wins += 1
            if dice1[i] == dice2[j]:
                equal += 1

    dice2_wins = 36 - dice1_wins - equal
    return (dice1_wins, dice2_wins)


# print(count_wins([1,2,3,4,5,6], [1,2,3,4,5,6]))
# print(count_wins([1,1,6,6,8,8], [2,2,4,4,9,9])) 

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    for i in range(len(dices)):
        status = []
        for j in range(len(dices)):
            if i != j:
                dice1_wins, dice2_wins = count_wins(dices[i], dices[j])
                if dice1_wins > dice2_wins:
                    status.append(1)
        if status.count(1) == len(dices) - 1:
            return i
    return -1

# print(find_the_best_dice([[1,1,6,6,8,8], [2,2,4,4,9,9], [3,3,5,5,7,7]]))
# print(find_the_best_dice([[1,1,2,4,5,7], [1,2,2,3,4,7], [1,2,3,4,5,6])])
# print(find_the_best_dice([[3,3,3,3,3,3], [6,6,2,2,2,2], [4,4,4,4,0,0], [5,5,5,1,1,1])])

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i+1) % len(dices)

    res = find_the_best_dice(dices)
    if res != -1:
        strategy["first_dice"] = res
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if i != j:
                    dice1_wins, dice2_wins = count_wins(dices[i], dices[j])
                    if dice1_wins < dice2_wins:
                        break
            strategy[i] = j
    return strategy


print(compute_strategy([[1,1,4,6,7,8], [2,2,2,6,7,7], [3,3,3,5,5,8]]))
print(compute_strategy([[4,4,4,4,8,8], [7,7,3,3,3,3], [6,6,2,2,2,2], [5,5,5,1,1,1]]))

    