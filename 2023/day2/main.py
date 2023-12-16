
# Part 1
# game_num = 0
# res = 0
#
# d = {"red":12, "green":13, "blue":14}
#
# with open('input.txt', 'r') as f:
#     while True:
#         s = f.readline()
#         if not s:
#             break
#         game_num += 1
#         flag = True
#
#         s = s[s.find(':')+2:]
#         ss = s.split(';')
#         for game in ss:
#             groups = game.split(',')
#             for group in groups:
#                 g = group.split()
#                 if int(g[0]) > d[g[1]]:
#                     flag = False
#         if flag:
#             res+= game_num
#
# print(res)


# Part 2
game_num = 0
res = 0

with open('input.txt', 'r') as f:
    while True:
        s = f.readline()
        if not s:
            break
        game_num += 1

        d = {"red": 0, "green": 0, "blue": 0}
        s = s[s.find(':')+2:]
        ss = s.split(';')
        for game in ss:
            groups = game.split(',')
            for group in groups:
                g = group.split()
                if int(g[0]) > d[g[1]]:
                    d[g[1]] = int(g[0])

        r = 1
        for val in d.values():
            r*= val
        res+= r

print(res)


