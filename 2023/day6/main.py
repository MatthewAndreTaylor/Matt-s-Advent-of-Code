
# Part 1
# with open('input.txt', 'r') as f:
#     s = f.readline()
#
#     s = s.split(":")[1].split()
#
#     times = [int(time) for time in s]
#
#     s = f.readline()
#
#     s = s.split(":")[1].split()
#
#     distances = [int(dist) for dist in s]
#
#
#
# p = 1
# for time, distance in zip(times, distances):
#     amount = 0
#     for hold in range(time):
#         if (time - hold) * hold > distance:
#             amount += 1
#     p *= amount
#
# print(p)



# Part 2
with open('input.txt', 'r') as f:
    s = f.readline()

    s = ''.join(s.split(":")[1].split())

    times = [int(s)]

    s = f.readline()

    s = ''.join(s.split(":")[1].split())

    distances = [int(s)]



p = 1
for time, distance in zip(times, distances):
    amount = 0
    for hold in range(time):
        if (time - hold) * hold > distance:
            amount += 1
    p *= amount

print(p)
