"""Check the packing construction behind A300001's rule for n = 82..200000.

For each n, s is the smallest side with s*s >= n and s*s - n outside {1,2,4,5,7,10,13}.
Write s*s - n = 3a + 8b with b in {0,1,2}: a triangles of side 2 go in the two bottom
strips of height 2, at most two triangles of side 3 go in the top triangle of side s-4,
and unit triangles fill the rest, giving exactly n pieces.
"""
bad = {1, 2, 4, 5, 7, 10, 13}


def rule(n):
    s = 1
    while s * s < n or s * s - n in bad:
        s += 1
    return s


def strip(L):
    # side-2 triangles in a strip of height 2 whose base has length L
    return L - 1 if L % 2 == 0 else L - 2


for n in range(82, 200001):
    s = rule(n)
    d = s * s - n
    b = next(b for b in (0, 1, 2) if d >= 8 * b and (d - 8 * b) % 3 == 0)
    a = (d - 8 * b) // 3
    assert s >= 10 and a <= strip(s) + strip(s - 2) and s - 4 >= 3 * b, n
print("construction works for n = 82..200000")
