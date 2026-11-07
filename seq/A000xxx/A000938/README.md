# A000938

> Number of collinear point-triples in an n X n grid.
> — [OEIS A000938](https://oeis.org/A000938)

Offset 1: 0, 0, 8, 44, 152, 372, 824, 1544, 2712, 4448, 6992, 10332, 15072, 21012, 28688, 38520, 50880, 65480, 83640, 104676, …

### Python 3 — 109 bytes

```python
from math import*
n=1
while[print(2*sum(k%n*(k//n)*gcd(n-k%n,n-k//n)for k in range(n*n))-(n**4-n*n)//6)]:n+=1
```

**How it works**

- A collinear triple is fixed by its two outer points and one lattice
  point strictly between them; two points at offset (dx, dy) have
  gcd(|dx|, |dy|)−1 such points. Summing over pairs gives the OEIS formula
  (Larrosa Cañestro) a(n) = 2 Σ (n−i)(n−j) gcd(i, j) − n²(n²−1)/6, the sum
  over 1 ≤ i, j ≤ n−1: the factor 2 is the two signs of the slope, and
  the polynomial collects the −1 of every pair together with the
  horizontal and vertical pairs.
- Writing i → n−i, j → n−j makes the weights plain i·j, and then i = 0 or
  j = 0 adds nothing, so the sum can run over 0 ≤ i, j < n: one loop
  k < n² with i = k%n, j = k//n, 2 B under two `for` clauses.
- n²(n²−1) is a product of three consecutive integers times n, so the
  division by 6 is exact.

**Notes**

- Exact integer arithmetic; only the counting identity above.
- n² gcds per term: about 630–680 terms in 60 s here.
- The b-file has 1000 terms; the bar is 500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000938), CC BY-SA 4.0.
