# A000291

> Number of bipartite partitions of n white objects and 2 black ones.
> — [OEIS A000291](https://oeis.org/A000291)

Offset 0: 2, 4, 9, 16, 29, 47, 77, 118, 181, 267, 392, 560, 797, 1111, …

A partition of the multiset {wⁿ, b, b} is some blocks of white objects only
(a partition of what is left, g.f. P(x)) plus either one block holding both
b's and any number of w's (1/(1 − x)) or two blocks with one b each, which
carry an unordered pair of white counts (1/((1 − x)(1 − x²))). So the g.f. is
P(x)·(1/(1 − x) + 1/((1 − x)(1 − x²))), which is the entry's
a(n) = [A000070](../A000070/)(n) + [A000097](../A000097/)(n). With
c = A000097, whose g.f. is P(x)/((1 − x)(1 − x²)), it reads
a(n) = 2·c(n) − c(n − 2).

### Python 3 — 99 bytes

```python
*a,n=0,0,1,0
while[print(2*a[-1]-a[-3])]:n-=1;a+=sum(d*sum(a[d::d])<<(d>-3)for d in range(n,0))//n,
```

**How it works**

- The list grows exactly as in [A000097](../A000097/): c is the Euler
  transform with two kinds of parts 1 and 2, so
  **m·c(m) = Σₖ k·eₖ·Σⱼ c(m − jk)** with e₁ = e₂ = 2 and eₖ = 1 otherwise.
  n runs −1, −2, … and d = −k, so `a[d::d]` reads c(m − k), c(m − 2k), …
  back from the end, and `<<(d>-3)` doubles the k = 1, 2 terms. The sum
  and n are both negative, so `//n` is the exact quotient.
- Two zeros in front stand for c(−2) = c(−1) = 0, so `2*a[-1]-a[-3]` is
  right from a(0) on. The slices run into them, but they add nothing.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.1·√n digits, so the 4300-digit int-to-str limit is far beyond
  what the program reaches.
- The whole b-file (10 001 terms) prints in about 59 s here and 5000 terms
  in about 13 s; the bar is 5000 terms in 60 s, as for A000097.
- Keeping A000070 in the list instead (weight 2 for part 1 only,
  `<<(d>-2)`) drops the leading zeros, and A000097 is then every other
  A000070 term summed back from the end, `a[-1]+sum(a[::-2])`; that is
  100 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 99 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000291), CC BY-SA 4.0.
