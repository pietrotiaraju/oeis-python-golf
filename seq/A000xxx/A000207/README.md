# A000207

> Number of inequivalent ways of dissecting a regular (n+2)-gon into n triangles by n-1 non-intersecting diagonals under rotations and reflections; also the number of (unlabeled) maximal outerplanar graphs on n+2 vertices.
> — [OEIS A000207](https://oeis.org/A000207)

Offset 1: 1, 1, 1, 3, 4, 12, 27, 82, 228, 733, 2282, 7528, 24834, …

### Python 3 — 94 bytes

```python
m=2;L=[c:=1]
while 1:L+=0,0,c;c=4*c-6*c//m;m+=1;print((6*c//m+(9-m%2*3)*L[m//2*3]+4*L[m])//12)
```

**How it works**

With Catalan numbers C_k, the count of triangulations of an
(n+2)-gon up to the dihedral group is the classical closed form in the
OEIS entry (Moon and Moser, 1963):

  a(n) = C_n/(2n+4) + C_⌊n/2⌋/2 + [n even]·C_{n/2}/4 + [n ≡ 1 mod 3]·C_{(n−1)/3}/3.

Robert A. Russell's generating function
(4G − G² + 9G(z²) + 6zG(z²) + 4zG(z³))/12, with G = 1 + zG², gives the
same coefficients and the form the program uses:

  **12a(n) = 6C_n/(n+2) + (9 if n even, else 6)·C_⌊n/2⌋ + 4·[n ≡ 1 mod 3]·C_{(n−1)/3}.**

- The loop runs over m = n + 2, the number of vertices of the polygon, so
  the divisor is just `m`, the parity of n is the parity of m, and
  [n ≡ 1 mod 3] is [3 | m].
- `c` holds C_n. 6C_n/(n+2) = 4C_n − C_{n+1} is an integer, so `6*c//m`
  is exact, and the same identity is the update:
  C_{n+1} = 4C_n − 6C_n/(n+2) (2 bytes under `c*(4*m-6)//m`).
- The list `L` keeps the Catalan numbers three apart with zeros between
  them: L[3k+3] = C_k. Then `L[m]` is C_{m/3−1} = C_{(n−1)/3} when 3 | m
  and 0 otherwise, so the third term needs no test; and `L[m//2*3]` is
  C_{⌊m/2⌋−1} = C_⌊n/2⌋.
- The first pass is a phantom n = 0 step: it appends C_0 at index 3 and
  turns c into C_1 before anything is printed. That lets `L` start as
  `[1]` (L[0] is never read) and m start at 2.

**Golf tricks**

- The spaced list replaces `n%3%2*4*L[n//3]` with `4*L[m]` (−7 bytes)
  for a cost of `0,0,` in the append.
- Starting one step early saves `*4` and costs one byte in the loop
  (`while 1:…;print(…)` instead of `while[print(…)]:…`).

**Notes**

- Exact integer arithmetic throughout, so it is correct for every n; the
  only input is the formula above (Moon and Moser 1963; R. K. Guy 1958 and
  W. G. Brown 1964 counted the same dissections).
- About 7,160 terms come out in under a minute; the program then stops at
  Python's 4300-digit limit for converting an int to a string (a(7160)
  has 4301 digits). The bar is the whole b-file (200 terms) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000207), CC BY-SA 4.0.
