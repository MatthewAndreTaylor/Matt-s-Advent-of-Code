# Part 1

res = 0
# with open('input.txt', 'r') as f:
#     while True:
#         s = f.readline()
#         if not s:
#             break
#
#         s = s[s.find(':') + 2:]
#         left, right = s.split('|')
#
#         winners = set(left.split())
#         your_nums = right.split()
#
#         r = 0
#
#         for num in your_nums:
#             if num in winners:
#                 if r == 0:
#                     r = 1
#                 else:
#                     r *= 2
#
#         res+= r
#
# print(res)


# Part 2
winners = []
your_nums = []
num_cards = 0

with open('input.txt', 'r') as f:
    while True:
        s = f.readline()
        if not s:
            break

        s = s[s.find(':') + 2:]
        left, right = s.split('|')

        winners.append(set(left.split()))
        your_nums.append(set(right.split()))
        num_cards+=1


cards_won = [1] * num_cards
for i in range(num_cards):
    l = 0
    for num in your_nums[i]:
        if num in winners[i]:
            l+=1

    for j in range(l):
        cards_won[i + j + 1] += cards_won[i]


print(sum(cards_won))

