from collections import Counter
from functools import cmp_to_key

# Part 1
# card_values = {"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, '2':0}
# def compare_cards(card0, card1):
#     for i in range(5):
#         if card0[i] != card1[i]:
#             if card_values[card0[i]] > card_values[card1[i]]:
#                 return 1
#             else:
#                 return -1
#     return 0
#
# hand_to_bid = {}
# with open('input.txt', 'r') as f:
#     while True:
#         s = f.readline()
#         if not s:
#             break
#
#         hand, bid = s.split()
#
#         hand_to_bid[hand] = int(bid)
#
#
# #print(hand_to_bid)
#
# five_kind = []
# four_kind = []
# full_house = []
# three_kind = []
# two_pair = []
# one_pair = []
# high_card = []
#
# for hand in hand_to_bid.keys():
#     c = Counter(hand)
#     if len(c) == 1:
#         five_kind.append(hand)
#     elif len(c) == 2:
#         is_four = False
#         for val in c.values():
#             if val > 3:
#                 is_four = True
#         if is_four:
#             four_kind.append(hand)
#         else:
#             full_house.append(hand)
#     elif len(c) == 3:
#         is_three = False
#         for val in c.values():
#             if val > 2:
#                 is_three = True
#         if is_three:
#             three_kind.append(hand)
#         else:
#             two_pair.append(hand)
#     elif len(c) == 4:
#         one_pair.append(hand)
#     else:
#         high_card.append(hand)
#
#
# four_kind.sort(key=cmp_to_key(compare_cards))
# full_house.sort(key=cmp_to_key(compare_cards))
# three_kind.sort(key=cmp_to_key(compare_cards))
# two_pair.sort(key=cmp_to_key(compare_cards))
# one_pair.sort(key=cmp_to_key(compare_cards))
# high_card.sort(key=cmp_to_key(compare_cards))
#
# res = 0
# lst = high_card + one_pair + two_pair + three_kind + full_house + four_kind + five_kind
# print(lst)
#
# for i, hand in enumerate(lst, start=1):
#     res += hand_to_bid[hand] * i
#
# print(res)


# Part 2
letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}


def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]


def classify(hand):
    return max(map(score, replacements(hand)))


def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])


plays = []

for line in open('input.txt', 'r'):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key=lambda play: strength(play[0]))
print(plays)

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)
