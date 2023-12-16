
# Part 1
res = 0
# with open('input.txt', 'r') as f:
#     while True:
#         s = f.readline()
#         if not s:
#             break
#         s = [c for c in s if c.isdigit()]
#         res += int(s[0] + s[-1])

#print(res)

# Part 2
nums = {"one":"1","two":"2","three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
with open('input.txt', 'r') as f:
    while True:
        s = f.readline()
        if not s:
            break

        last = None
        first = None
        firstnum = None
        lastNum = None

        for key in nums.keys():
            for i in range(len(s)):
                if s.startswith(key, i):
                    if first is None or i < first:
                        first = i
                        firstnum = nums[key]

                    if last is None or i > last:
                        last = i
                        lastNum = nums[key]


        for i, c in enumerate(s):
            if c.isdigit():
                if first is None or i < first:
                    first = i
                    firstnum = c

                if last is None or i > last:
                    last = i
                    lastNum = c

        res += int(firstnum + lastNum)

print(res)
