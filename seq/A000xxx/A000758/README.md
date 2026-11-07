# A000758

> Sum over rooted plane trees with n edges of (height - 1); height = measured edges.
> — [OEIS A000758](https://oeis.org/A000758)

Offset 1: 0, 1, 5, 20, 76, 285, 1066, 3991, 14976, 56353, 212667, 804860, 3054328, …

### Python 3 — 114 bytes

```python
from math import*
f=0;n=4
while[print(-4*f+(f:=sum(comb(n,n//2+j)for m in range(3,n)for j in range(m,n,m))))]:n+=2
```

**How it works**

- Below, N is the number of edges and the trees are Dyck paths of
  length 2N. The height sum is Σ_{t≥1} #(height ≥ t), and the −1 drops
  t = 1: a(N) = Σ_{h≥1} (C_N − H_h(N)), where C_N is the Catalan number
  and H_h(N) counts the paths that stay in 0…h.
- Reflection in the strip (walls at −1 and h+1, so period 2(h+2)) gives
  H_h(N) = Σ_{k∈ℤ} [C(2N, N+km) − C(2N, N−1+km)] with m = h+2. The k = 0
  term is C_N, and pairing k with −k gives
  C_N − H_h(N) = Σ_{k≥1} Δ(km), Δ(j) = C(2N,N+j−1) − 2C(2N,N+j) + C(2N,N+j+1).
- Δ(j) is the coefficient of x^(N+1+j) in
  (1−x)²(1+x)^(2N) = (1+x)^(2N+2) − 4x(1+x)^(2N). Summing over m ≥ 3 and
  k ≥ 1: a(N) = f(N+1) − 4f(N), with f(N) = Σ_{m≥3} Σ_{k≥1} C(2N, N+km).
- The program keeps n = 2N, so the binomial is `comb(n,n//2+j)` with j = km,
  and prints −4·f(N−1) + f(N) = a(N−1): `-4*f` is read before the walrus
  stores the new f. It starts at n = 4 with f = f(1) = 0, so the first line
  is a(1).
- Both ranges overshoot (m and j run up to 2N), which costs nothing:
  `comb` returns 0 once the lower index passes 2N, and j ≥ 3 keeps every
  argument non-negative.

**Notes**

- Exact integer arithmetic; about 2N·ln N binomials per term: 776 terms
  in 60 s here.
- Looping k instead of j, `comb(n,n//2+k*m)` with `range(1,n)`, is the same
  length but O(N²) binomials per term (474 terms in 60 s). With N itself as
  the loop variable the program is 115 (k loop) or 117 (j loop) bytes.
- The OEIS entry notes that the definition was reconstructed in 2026 and
  reproduces the original terms; this program follows that definition and
  matches the whole b-file.
- The b-file has 1000 terms; the bar is 600 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000758), CC BY-SA 4.0.
