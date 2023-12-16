
def to_map(lst):
    def foo(value):
        for i in range(len(lst)):
            dst, src, l = map(int, lst[i].split())

            if src <= value < src + l:
                return dst + (value - src)

        return value

    return foo

with open('input.txt', 'r') as f:
    s = f.read()
    s = s.split('\n\n')

    seeds = s[0][s[0].find(':') + 2:]
    seeds = [int(seed) for seed in seeds.split()]
    #print(seeds)

    s = s[1:]
    for i in range(len(s)):
        s[i] = s[i][s[i].find(':')+2:]
        s[i] = s[i].split('\n')

    for lst in s:
        foo = to_map(lst)
        seeds = list(map(foo, seeds))

    print(min(seeds))
