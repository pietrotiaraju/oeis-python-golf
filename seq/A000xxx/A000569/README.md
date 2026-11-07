# A000569

> Number of graphical partitions of 2n.
> — [OEIS A000569](https://oeis.org/A000569)

Offset 1: 1, 2, 5, 9, 17, 31, 54, 90, 151, 244, …

a(n) counts the partitions of 2n that are the degree sequence of a simple
graph (with no isolated vertices), that is, the degree sequences of graphs
with n edges.

### Python 3 — 166 bytes

```python
f=lambda s,m=1,p=():s<1and all(sum(p[:r])<=r*r-r+sum(min(x,r)for x in p[r:])for r in range(n))or sum(f(s-j,j,(j,)+p)for j in range(m,s+1))
n=2
while[print(f(n))]:n+=2
```

**How it works**

- **The test.** By the Erdős–Gallai theorem (1960), a sequence
  d_1 ≥ … ≥ d_L of positive integers with even sum is graphical if and only
  if Σ_{i≤r} d_i ≤ r(r − 1) + Σ_{i>r} min(d_i, r) for every r = 1, …, L.
  In the code `p[:r]` is d_1, …, d_r and `p[r:]` the rest.
- **The range of r.** The program checks r = 0, …, n − 1, where n = 2k is
  the sum, instead of 1, …, L. The case r = 0 is trivial. For r > L the
  condition reads n ≤ r(r − 1), which follows from the r = L case. The case
  r = L itself is skipped only when L = n, i.e. for 1 + 1 + … + 1, where it
  holds. So the test is exactly Erdős–Gallai, and it still sees r = 1 for
  the one-part partition (n) (which fails, as it should).
- **The partitions.** `f(s,m,p)` chooses parts j ≥ m in nondecreasing order
  and prepends each one, so `p` is nonincreasing, as the test needs. When
  nothing is left (`s<1`) it returns the test; otherwise it sums over the
  next part. If the test fails at a leaf, `or` falls through to an empty
  sum, which is 0.
- The loop runs over the even sums n = 2, 4, 6, …, and `f` reads that n as
  the bound for r.

**Notes**

- Other versions that print the same terms: Havel–Hakimi (remove the
  largest degree d, subtract 1 from the next d, re-sort) on a separate
  partition generator: 249 bytes.
- Exact integer arithmetic; correctness for every n rests on the
  Erdős–Gallai theorem.
- The program tries every partition of 2n (p(50) ≈ 2·10⁵): about 25 terms
  in 60 s here. The b-file has 860 terms (up to a(860)); the bar is 12
  terms in 60 s.
- a(n) is at most the partition number p(2n), which has under 50 digits
  even at n = 860, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 249 | first entry |
| 2026-11-07 | Python 3 | 166 | Erdős–Gallai test inside the partition recursion |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000569), CC BY-SA 4.0.
