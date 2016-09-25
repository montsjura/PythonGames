def golf(m):
    r = list(map(sum, m))
    c = list(map(sum, list(zip(*m))))
    return [r.index(min(r)), c.index(min(c))]