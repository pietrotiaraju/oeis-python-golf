# A000183

> Number of discordant permutations of length n.
> — [OEIS A000183](https://oeis.org/A000183)

Offset 1: 0, 0, 0, 1, 2, 20, 144, 1265, 12072, 126565, 1445100, …

### Python 3 — 98 bytes

```python
f=lambda c:c<{0}or sum(f(c-{j})for j in c if(j+len(c))%n>2)
n=0
while n:=n+1:print(f({*range(n)}))
```

**How it works**

- a(n) counts the permutations p of Z_n with p(i) − i ∉ {0, 1, 2}
  (mod n): the permutations discordant with the identity, the n-cycle
  s and s². (The OEIS comment "none in or next to the original chair"
  forbids {−1, 0, 1} instead; shifting p by one turns one into the other.)
- `f` fills the rows one at a time and `c` is the set of columns still
  free. The row being filled is r = len(c), so the rows go n, n−1, …, 1
  with no counter to pass, and column j is allowed in row r when
  (j + r) mod n > 2. Writing i = −r mod n this reads (j − i) mod n > 2,
  and r ↦ −r is a bijection of Z_n, so the count is the same.
- `c<{0}` is true only for the empty set (a proper subset of {0}), one
  byte under `not c`: a full placement returns `True`, which `sum`
  counts as 1. The top call always gets a non-empty set, so it returns
  the int from `sum`, including the zeros for n = 1, 2, 3.
- `n` is the global read at call time, so the lambda carries only the
  set.

**Notes**

- Exhaustive search, correct for every n. It is about n times slower
  per term: on the machine that set the bar a(1)…a(11) come out in
  about 6 s and a(12) would take about 70 s more. The bar is 11 terms
  in 60 s.
- The fast route is inclusion–exclusion over the rook numbers of the
  3-band circulant board,
  a(n) = Σ_m (−1)^m·(n−m)!·[A061702](https://oeis.org/A061702)(n, m) for
  n ≥ 3. With x = −1/t the rook polynomial becomes P_n(t) + (−1)ⁿ, where
  P_n is the n-th power sum of the roots of μ³ − (t−2)μ² + tμ − 1, and
  then a(n) = Σ_k [t^k]P_n·k! + (−1)ⁿ. The auxiliary
  V(n) = Σ_k [t^k]h_n·k! (complete symmetric h_n of the same roots)
  satisfies the monic order-7 recurrence
  V(n) = n·V(n−1) + 5V(n−2) + (8−3n)V(n−3) + (n−6)V(n−4) + (2n−7)V(n−5)
  + (6−n)V(n−6) − V(n−7) (found from the terms, not proved here), but
  a program built on it is longer than the search.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000183), CC BY-SA 4.0.
