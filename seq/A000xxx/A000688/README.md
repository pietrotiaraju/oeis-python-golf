# A000688

> Number of Abelian groups of order n; number of factorizations of n into prime powers.
> — [OEIS A000688](https://oeis.org/A000688)

Offset 1: 1, 1, 1, 2, 1, 1, 1, 3, 2, 1, 1, 2, 1, 1, 1, 5, 1, 2, 1, 2, …

### Python 3 — 97 bytes

```python
f=lambda n,m=0:n<2or sum(f(n//d,d)for d in range(2,n+1)if n%d+m%d<1)
n=1
while[print(+f(n))]:n+=1
```

**How it works**

- By the structure theorem, a finite Abelian group of order n is
  C(d₁) × … × C(d_k) for a unique chain of invariant factors
  1 < d₁ | d₂ | … | d_k with d₁⋯d_k = n. So a(n) counts these chains, the
  empty chain being the trivial group of order 1.
- `f(n,m)` counts the chains with product n whose factors all divide m;
  m = 0 means no condition, because `0%d` is 0. Pick the largest factor d
  first: d > 1 divides both n and m, and the rest is a chain with product
  n/d whose factors all divide d. Hence f(n, m) = [n = 1] + Σ f(n/d, d).
- `n<2or` returns `True` for n = 1, which a sum counts as 1; at the top
  level `+f(n)` turns that `True` into `1`.
- Splitting the chain prime by prime gives the OEIS formula: a(n) is the
  product of the partition numbers p(e) over the prime powers pᵉ ∥ n.

**Notes**

- Exact integer counting, so the program is right for every n. The
  recursion depth is the length of a chain, at most log₂ n.
- Each call scans d up to n, so a term costs O(n) steps per partial chain.
  The whole b-file (10000 terms) prints in about 31 s on this PC; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000688), CC BY-SA 4.0.
