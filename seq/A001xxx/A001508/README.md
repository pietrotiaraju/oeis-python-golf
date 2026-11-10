# A001508

> a(n) is the number of c-nets with n+1 vertices and 2n+2 edges, n >= 1.
> — [OEIS A001508](https://oeis.org/A001508)

Offset 1: 0, 0, 0, 0, 13, 252, 3740, 51300, 685419, 9095856, …

A c-net is a rooted 3-connected planar map. With n + 1 vertices and
2n + 2 edges, Euler's formula V − E + F = 2 gives n + 3 faces.

### Python 3 — 174 bytes

```python
from math import*
C=comb;m=3
while 1:R=range(m);print((m>3)*sum((-1)**(a+b)*C(2*m-2-a-b,m+~a)*C(m+~b,2)*C(2*m-4,a)*C(2*m,b)*((k:=m*m-2*m)-a*b)for a in R for b in R)//-k);m+=1
```

**The formula**

- Mullin and Schellenberg (*The enumeration of c-nets via
  quadrangulations*, J. Combin. Theory 4 (1968), 259–276) proved that
  the number of rooted c-nets with N + 1 faces and K + 1 vertices is,
  for N, K ≥ 3,

  T(N, K) = Σ_(i<K) Σ_(j<N) (−1)^(i+j+1) (i+j+2)!/(2·i!·j!) ·
  [C(2N, K−i−1)·C(2K, N−j−1) − 4·C(2N−1, K−i−2)·C(2K−1, N−j−2)]

  (OEIS A290326; this sequence is T(n + 2, n)). Their printed table has a
  few wrong entries (see A290326); the formula itself reproduces every
  term of the b-file.
- Put a = K − 1 − i and b = N − 1 − j. Since C(2N−1, a−1) = a/(2N)·C(2N, a)
  and C(2K−1, b−1) = b/(2K)·C(2K, b), the bracket is
  C(2N, a)·C(2K, b)·(NK − ab)/(NK), and
  (i+j+2)!/(2·i!·j!) = C(N+K−a−b, K−1−a)·C(N+1−b, 2). So

  NK·T(N, K) = Σ (−1)^(N+K+a+b+1) C(N+K−a−b, K−1−a)·C(N+1−b, 2)·C(2N, a)·C(2K, b)·(NK − ab).

**How it works**

- The formula is symmetric: swapping N ↔ K together with i ↔ j leaves
  it unchanged (as it must: the dual of a c-net is a c-net, with vertices
  and faces exchanged). The program counts with m = n + 2 and evaluates
  T(m − 2, m) = T(n + 2, n): N = m − 2, K = m.
- N + K = 2m − 2 is even, so the sign is (−1)^(a+b+1): the program sums
  with (−1)^(a+b) and divides by −NK = −(m² − 2m), which the walrus
  `(k:=m*m-2*m)` stores inside the first term (the sum is exactly that
  multiple of a(n)).
- a runs over 0 … K − 1 = m − 1 and b over 0 … N − 1 = m − 3; at b = m − 2
  and b = m − 1 the factor C(N + 1 − b, 2) is C(1, 2) or C(0, 2) = 0, so
  one `R=range(m)` serves both loops. `C=comb`; `m+~a` and `m+~b` are
  m − 1 − a and N + 1 − b. The range is set in the loop body: an
  assignment expression cannot be the iterable of a comprehension.
- The theorem covers N, K ≥ 3, i.e. n ≥ 3. At n = 2 the formula gives
  0 = a(2); at n = 1 it gives −1, so `(m>3)*` prints a(1) = 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n ≥ 1.
- The b-file has 204 terms (n = 1 to 204); the bar is the whole
  b-file in 90 s. The double sum costs O(n²) big-integer products per
  term; the last b-file term comes after about 35 s on this PC (about 20 reference seconds).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 174 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001508), CC BY-SA 4.0.
