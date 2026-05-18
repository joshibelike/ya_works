class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def add(r, v):
    if not r:
        return Node(v)
    if v < r.v:
        r.l = add(r.l, v)
    elif v > r.v:
        r.r = add(r.r, v)
    return r

def find(r, v):
    if not r or r.v == v:
        return r
    return find(r.l, v) if v < r.v else find(r.r, v)

def get_all(r):
    s = set()
    def go(x):
        if x:
            s.add(x.v)
            go(x.l)
            go(x.r)
    go(r)
    return s

vals = list(map(int, input().split()))
x, y = map(int, input().split())


root = None
for n in vals:
    root = add(root, n)

a = get_all(find(root, x))
b = get_all(find(root, y))

res = sorted(a & b)

print(' '.join(map(str, res)) if res else 0)