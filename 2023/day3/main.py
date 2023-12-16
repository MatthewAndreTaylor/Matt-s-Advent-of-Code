SYMBOL = 2
EMPTY = 0
DIGIT = 1
PARTNUM = 3
from collections import defaultdict

# Part 1
# with open('input.txt', 'r') as f:
#     lst = []
#     while True:
#         s = f.readline()
#         if not s:
#             break
#
#         lst.append(s[:-1])
#
#     grid = []
#     char_grid = []
#     for s in lst:
#         row = []
#         char_row = []
#         for c in s:
#             char_row.append(c)
#             if c.isdigit():
#                 row.append(DIGIT)
#             elif c == '.':
#                 row.append(EMPTY)
#             else:
#                 row.append(SYMBOL)
#         grid.append(row)
#         char_grid.append(char_row)
#
#
#     directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
#
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == DIGIT:
#                 for x, y in directions:
#                     dx, dy = i + x, j + y
#                     if 0 < i + x < len(row) and 0 < j + y < len(row):
#                         if grid[dx][dy] == SYMBOL:
#                             grid[i][j] = PARTNUM
#
#
    # for i in range(20):
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if j + 1 < len(row):
    #                 if grid[i][j] == DIGIT and grid[i][j + 1] == PARTNUM:
    #                     grid[i][j] = PARTNUM
    #             if j - 1 >= 0:
    #                 if grid[i][j] == DIGIT and grid[i][j - 1] == PARTNUM:
    #                     grid[i][j] = PARTNUM
#
#
#     res = 0
#     acc = ''
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == PARTNUM:
#                 acc+= char_grid[i][j]
#             else:
#                 if acc:
#                     res += int(acc)
#                     acc = ''
#
#     print(res)


# Part 2

with open('input.txt', 'r') as f:
    lst = []
    while True:
        s = f.readline()
        if not s:
            break

        lst.append(s[:-1])

    grid = []
    char_grid = []
    for s in lst:
        row = []
        char_row = []
        for c in s:
            char_row.append(c)
            if c.isdigit():
                row.append(DIGIT)
            elif c == '*':
                row.append(SYMBOL)
            else:
                row.append(EMPTY)
        grid.append(row)
        char_grid.append(char_row)


    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    d = defaultdict(set)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == DIGIT:
                for x, y in directions:
                    dx, dy = i + x, j + y
                    if 0 < i + x < len(row) and 0 < j + y < len(row):
                        if grid[dx][dy] == SYMBOL:
                            grid[i][j] = PARTNUM
                            d[(dx,dy)].add((i, j))


    for i in range(10):
        copy = defaultdict(set)
        for k, v in d.items():
            for x, y in v:
                if y + 1 < len(row):
                    if grid[x][y + 1] == DIGIT:
                        copy[k].add((x, y + 1))
                if y - 1 >= 0:
                    if grid[x][y - 1] == DIGIT:
                        copy[k].add((x, y - 1))

        for k, v in d.items():
            copy[k].update(v)
        d = copy


    def split_adjacent_lists(points):
        sorted_points = sorted(points)

        result = []
        current_sublist = [sorted_points[0]]

        for i in range(1, len(sorted_points)):
            if sorted_points[i][0] == current_sublist[-1][0] and sorted_points[i][1] == current_sublist[-1][1] + 1:
                current_sublist.append(sorted_points[i])
            else:
                result.append(current_sublist)
                current_sublist = [sorted_points[i]]

        result.append(current_sublist)
        return result

    res = 0

    for k, v in d.items():
        i = 0
        r = 1
        for lst in split_adjacent_lists(v):
            i+= 1
            acc =''
            for x,y in lst:
                acc += char_grid[x][y]
            r *= int(acc)

        if i == 2:
            res+=r

    print(res)
