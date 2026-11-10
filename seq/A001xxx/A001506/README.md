# A001506

> a(n) is the number of c-nets with n+1 vertices and 2n edges, n >= 1.
> — [OEIS A001506](https://oeis.org/A001506)

Offset 1: 0, 0, 1, 4, 24, 188, 1705, 16980, 180670, 2020120, …

A c-net is a rooted 3-connected planar map. With n + 1 vertices and
2n edges, Euler's formula V − E + F = 2 gives n + 1 faces.

### Python 3 — 165 bytes

```python
from math import*
C=comb;n=1
while 1:R=range(n);print((n>1)*sum((-1)**(a+b)*C(2*n-a-b,n+~a)*C(n-b+1,2)*C(2*n,a)*C(2*n,b)*(n*n-a*b)for a in R for b in R)//-n//n);n+=1
```

**The formula**

- Mullin and Schellenberg (*The enumeration of c-nets via
  quadrangulations*, J. Combin. Theory 4 (1968), 259–276) proved that
  the number of rooted c-nets with N + 1 faces and K + 1 vertices is,
  for N, K ≥ 3,

  T(N, K) = Σ_(i<K) Σ_(j<N) (−1)^(i+j+1) (i+j+2)!/(2·i!·j!) ·
  [C(2N, K−i−1)·C(2K, N−j−1) − 4·C(2N−1, K−i−2)·C(2K−1, N−j−2)]

  (OEIS A290326; this sequence is T(n, n)). Their printed table has a
  few wrong entries (see A290326); the formula itself reproduces every
  term of the b-file.
- Put a = K − 1 − i and b = N − 1 − j. Since C(2N−1, a−1) = a/(2N)·C(2N, a)
  and C(2K−1, b−1) = b/(2K)·C(2K, b), the bracket is
  C(2N, a)·C(2K, b)·(NK − ab)/(NK), and
  (i+j+2)!/(2·i!·j!) = C(N+K−a−b, K−1−a)·C(N+1−b, 2). So

  NK·T(N, K) = Σ (−1)^(N+K+a+b+1) C(N+K−a−b, K−1−a)·C(N+1−b, 2)·C(2N, a)·C(2K, b)·(NK − ab).

**How it works**

- Here N = K = n. N + K is even, so the sign is (−1)^(a+b+1): the
  program sums with (−1)^(a+b) and divides by −n² (`//-n//n`), exactly,
  since the sum is that multiple of a(n).
- Both a and b run over 0 … n − 1 (`R=range(n)`). `C=comb`, and `n+~a`
  is n − 1 − a.
- The range is set in the loop body: an assignment expression cannot be
  the iterable of a comprehension.
- The theorem covers n ≥ 3. At n = 2 the formula gives 0 = a(2) (no
  c-net has three vertices); at n = 1 it gives −1, so `(n>1)*` prints
  a(1) = 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n ≥ 1.
- The b-file has 200 terms (n = 1 to 200); the bar is the whole
  b-file in 90 s. The double sum costs O(n²) big-integer products per
  term; the last b-file term comes after about 35 s on this PC (about 20 reference seconds).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 165 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001506), CC BY-SA 4.0.
