# A001997

> Number of different shapes formed by bending a piece of wire of length n in the plane.
> — [OEIS A001997](https://oeis.org/A001997)

Offset 0: 1, 1, 2, 4, 10, 24, 66, 176, 493, 1362, 3821, 10660, 29864, 83329, 232702, …

The wire has n unit segments and is bent by 0° or ±90° at each of the
n − 1 marks between them. It may cross itself but may not run along itself
(no segment of the lattice is used twice), and two wires are the same
shape when a rotation, a reflection or reading from the other end takes
one to the other. In the words of the OEIS comment, a(n) counts the
undirected trails of length n on the square lattice up to rotation and
reflection. A wire is its word of n − 1 turns over {left, straight,
right}; a plain search over these words with the trail test reproduces
every term in the OEIS data that it reaches, and the program below follows
the same definition.

### Python 3 — 178 bytes

```python
n=s=1
while[print(s)]:
 s=0
 for N in range(3**n//6+1):
  p=d=1;E={1};k=N;r=0
  for _ in[0]*~-n:t=k-(k:=(k+1)//3)*3;r=3*r+t;d*=1j**t;E|={2*p+d};p+=d
  s+=n-len(E)<1>r*r-N*N
 n+=1
```

**How it works**

- A word of n − 1 turns is a number N in balanced ternary: digit t = 1 is
  a left turn (multiply the direction by i), −1 a right turn, 0 straight
  on. The digits come out lowest first: `t=k-(k:=(k+1)//3)*3` is the
  balanced remainder and the walrus divides k in the same expression.
- The four ways to look at one wire act on N simply. The mirror image
  swaps left and right, so it is −N; reading the wire from the other end
  reverses the word and also swaps left and right, so it is −r, where r is
  N with its n − 1 digits in reverse order (`r=3*r+t`); both together give
  r. A shape is the orbit {N, −N, r, −r}, and the program counts it at its
  largest member: N ≥ |r|, written `r*r-N*N<1`. That needs N ≥ 0, so only
  N = 0…(3ⁿ⁻¹ − 1)/2 = `3**n//6` are tried.
- The walk starts with the edge from 0 to 1. An edge from p in direction d
  is stored as its doubled midpoint 2p + d, which names the unit segment
  whichever way it is crossed, so the wire is a trail exactly when its n
  midpoints are all different: `n-len(E)<1`. Mirror images and reversals
  of a trail are trails, so testing the counted member is enough.
- `n=s=1` prints a(0) = 1 first; n = 1 has no turns and gives 1.

**Notes**

- The search tries about 3ⁿ⁻¹/2 words, n steps each, so a term takes
  about three times as long as the one before: 15 terms (to
  a(14) = 232702) in about 22 s here, 16 in about 67 s. The bar is 15 terms
  in 60 s. Memory stays near 10 MB.
- Exact arithmetic: the walk uses complex numbers, whose parts are
  integers of size at most 2n + 1, far below 2⁵³.
- The same count with tuples from `itertools.product` and the orbit
  minimum `min(w,c,w[::-1],c[::-1])` is 211 bytes and twice as slow.
- Words with a reused segment are A001998's extra shapes: 3ⁿ⁻¹ words up
  to the same four maps give [A001998](../A001998/)(n − 1), which first
  differs from this sequence at n = 5 (25 against 24, the wire wound
  around a square and back over its first segment).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 178 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001997), CC BY-SA 4.0.
