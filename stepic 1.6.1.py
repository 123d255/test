def pti(pr, ch):
    return ch == pr or any(map(lambda pl: isP(pr, pl), p[ch]))
p = {}
for j in range(2):
    for c in [input().split() for i in range(int(input()))]:
        if j: print(['No', 'Yes'][pti(*c)])
        else: p[c[0]] = c[2:]