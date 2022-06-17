def change(amount):
    if amount % 5 == 0:
        return int(amount/5) * [5]
    if amount % 7 == 0:
        return int(amount/7) * [7]

    res = change(amount - 5)
    res.append(5)
    return res


print(change(47))