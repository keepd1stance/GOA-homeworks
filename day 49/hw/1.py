def print_positions(rows, cols):
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            print("row:", row, "col:", col)

print_positions(2, 2)

def gamravlebis_tabula():
    table = []
    for i in range(1, 11):
        row = [i * j for j in range(1, 11)]
        table.append(row)
    return table

print(gamravlebis_tabula())


def wyvilebi(n):
    pairs = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > i:
                pairs.append((i, j))
    print(pairs)

wyvilebi(3)