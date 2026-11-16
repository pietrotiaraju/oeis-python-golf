# A001832

> Number of labeled connected bipartite graphs on n nodes.
> — [OEIS A001832](https://oeis.org/A001832)

Offset 1: 1, 1, 3, 19, 195, 3031, 67263, 2086099, 89224635, 5254054111, 426609529863, …

### Python 3 — 165 bytes

```python
from math import*
A=lambda n:sum(comb(n,j)<<j*(n-j)for j in range(n+1))
L=[0]
while[print(a:=A(n:=len(L))//2-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
```

**How it works**

- **Two-coloured graphs.** Colour each of n labeled vertices black or white
  and draw any edges between the colours: there are
  A(n) = Σⱼ C(n, j)·2^(j(n−j)) such pictures
  ([A047863](https://oeis.org/A047863)). Each one splits into its connected
  components, each a connected bipartite graph with one of its colourings,
  and a connected bipartite graph has exactly two colourings (a single
  vertex too). So with B(x) the e.g.f. of this sequence,
  Σ A(n)xⁿ/n! = exp(2B(x)): the formula log(A(x))/2 on the OEIS page.
- **Taking the log.** Differentiating, A′ = 2B′·A, which reads
  A(n) = 2·Σₖ₌₁..ₙ C(n − 1, k − 1)·a(k)·A(n − k), so
  a(n) = A(n)/2 − Σₖ₌₁..ₙ₋₁ C(n − 1, k − 1)·a(k)·A(n − k).
- **The program.** `L` holds a(1), …, a(n − 1) after a dummy 0 in L[0], so
  `n:=len(L)` is the next index. C(n − 1, k − 1) is written k·C(n, k)/n
  (`comb(n,k)*k*L[k]//n`, exact because n divides k·C(n, k)), which makes
  the k = 0 term vanish and lets the sum run over `range(n)`, as in
  [A001187](../A001187/). `A` is A047863. A(n) is even for n ≥ 1 (swap the
  colours), so `A(n)//2` is exact.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 238.
- The b-file has 50 terms (n = 1 to 50); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 165 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001832), CC BY-SA 4.0.
