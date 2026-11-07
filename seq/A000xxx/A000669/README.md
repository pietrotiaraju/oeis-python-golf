# A000669

> Number of series-reduced planted trees with n leaves. Also the number of essentially series series-parallel networks with n edges; also the number of essentially parallel series-parallel networks with n edges.
> — [OEIS A000669](https://oeis.org/A000669)

Offset 1: 1, 1, 2, 5, 12, 33, 90, 261, 766, 2312, 7068, 21965, 68954, 218751, …

### Python 3 — 96 bytes

```python
A=[1,n:=1]
while[print(-~A[n]//2)]:n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- A series-reduced planted tree is a leaf or a multiset of at least two such
  trees, so with b(n) = a(n) the OEIS formula holds:
  Π_k (1 − x^k)^(−b(k)) = 1 + x + 2·Σ_{k>1} b(k)·x^k.
  The right-hand side is 1 + Σ s(n)·xⁿ with s = [A000084](../A000084/)
  (series-parallel networks): s(1) = 1 and s(n) = 2·b(n) for n > 1.
- The list `A` is exactly the [A000084](../A000084/) record: it holds
  s(0) = 1, s(1), …, and appends s(n) from the Euler transform recurrence
  n·s(n) = Σ_{d<n} 2d·b(d)·Σ_{j≥1} s(n − jd), where 2d·b(d) is d·s(d)
  for d ≥ 2 and 2 for d = 1 (so `d` runs over 1, 1, 2, …, n − 1). See that
  page for the slice `A[-d::-d]`.
- The print turns s back into b: `-~A[n]//2` is (s(n) + 1)//2, which is 1
  for n = 1 and s(n)/2 for n > 1 because s(n) is even there.

**Notes**

- Exact integer arithmetic: the sum is n·s(n), so `//n` is exact and the
  program is right for every n.
- About 2800 terms print in 60 s; the bar is the whole b-file (1001 terms)
  in 60 s, which takes well under a second.
- a(n) grows like 3.56…ⁿ, so near n = 7800 the decimal form passes Python's
  4300-digit int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000669), CC BY-SA 4.0.
