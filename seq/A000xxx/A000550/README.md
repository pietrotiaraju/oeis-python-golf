# A000550

> Number of trees of diameter 7.
> — [OEIS A000550](https://oeis.org/A000550)

Offset 8: 1, 3, 14, 42, 128, 334, 850, 2010, 4625, 10201, …

### Python 3 — 177 bytes

```python
*L,n=1,1,0;Z=0,
while[n>-16or print((sum(map(int.__mul__,Z,Z[::-1]))+Z[-n//2])//2)]:
 n-=2;Z+=0,L[-2]-L[-1]
 for h in 1,0:L+=sum(d*L[~d*h]*sum(L[d::d])for d in range(n,0,2))//n,
```

**How it works**

- **The decomposition.** A tree of diameter 7 has a unique central edge, the
  middle edge of every longest path. Cutting it leaves two trees rooted at
  its ends, each of height exactly 3, and every unordered pair of such rooted
  trees gives back a tree of diameter 7. With R(x) = Σ R_N x^N counting rooted
  trees of height exactly 3 by nodes, the unordered pairs give
  a(N) = [x^N] (R(x)² + R(x²))/2 (the formula on the OEIS page).
- **Rooted trees of height 3.** A rooted tree of height at most 2 on m + 1
  nodes is a root with stars below it, so there are p(m) of them (partitions
  of m). A rooted tree of height at most 3 on m + 1 nodes is a root with a
  multiset of those below it, counted by c(m) = [x^m] Π_k (1 − x^k)^(−p(k−1)).
  So R_N = c(N − 1) − p(N − 1).
- **Both Euler transforms in one list** (the [A000235](../A000235/) trick).
  For b = Π_k (1 − x^k)^(−w(k)), m·b(m) = Σ_{k≤m} k·w(k)·Σ_{j≥1} b(m − jk).
  `L` is c(0), p(0), c(1), p(1), …, and step m (with n = −2m) appends c(m)
  and then p(m). In the sum d = −2k, and `L[d::d]` reads every 2k-th entry
  from the end: b(m − k), b(m − 2k), …, with b = c in the first pass (L then
  ends with p(m − 1)) and b = p in the second. The weight `L[~d*h]` is
  L[2k − 1] = p(k − 1) when h = 1 and L[0] = c(0) = 1 when h = 0, and
  d/n = k/m. The division is exact because m·b(m) is that integer sum.
- **The convolution.** `Z` is R_0, 0, R_1, 0, …, 0, R_m: each step first
  appends 0 and R_m = c(m − 1) − p(m − 1) = `L[-2]-L[-1]`. In
  Σ_j Z_j·Z_{2m−j} the odd j give 0, so the dot product of `Z` with its
  reverse is Σ_i R_i·R_{m−i} = [x^m] R(x)². The middle entry `Z[-n//2]` = Z_m
  is R_{m/2} for even m and 0 for odd m, which is [x^m] R(x²). So the header
  prints a(m), once m ≥ 8 (`n>-16or`: there are no such trees below 8 nodes).
- `*L,n=1,1,0` starts with L = [c(0), p(0)] = [1, 1] and n = 0, and `Z=0,`
  is R_0 = 0.

**Notes**

- Other versions: updating `Z` after the two passes (so `Z=0,0,0`, `Z[1-n//2]`
  and one more line) is 182 bytes; a plain list of R with the middle term as
  `n//2%2*R[-n//4+1]` was 187.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints in under 0.1 s, and about 4000 terms in 60 s here
  (a(4068) has 534 digits). The b-file has 50 terms (up to a(57)); the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 315 | first entry |
| 2026-11-06 | Python 3 | 187 | interleaved Euler transforms and central-edge convolution |
| 2026-11-07 | Python 3 | 177 | zero-interleaved R, so the middle term is Z[m] |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000550), CC BY-SA 4.0.
