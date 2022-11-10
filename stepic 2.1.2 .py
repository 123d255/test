errs = {}
tr_errs = []


def foumdpat(err2, start, end, pt=[]):
    pt = pt + [start]
    if start == end:
        return pt
    if start not in err2:
        return []
    for node in err2[start]:
        if node not in pt:
            newpt = foumdpat(err2, node, end, pt)
            if newpt: return newpt
    return []


for i in range(int(input())):
    inpt = input().split()
    child = inpt[0]
    parents = inpt[2:]
    errs[child] = parents

for i in range(int(input())):
    thrin = input()
    for tr_err in tr_errs:
        if len(foumdpat(errs, thrin, tr_err)) > 1:
            print(thrin)
            break
    tr_errs.append(thrin)
