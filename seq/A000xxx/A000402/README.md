# A000402

> Number of permutations of [n] in which the longest increasing run has length 3.
> — [OEIS A000402](https://oeis.org/A000402)

Offset 1: 0, 0, 1, 6, 41, 293, 2309, 19975, 189524, 1960041, …

A run is a maximal block of consecutive positions whose entries increase.

### Python 3 — 126 bytes

```python
L=[c:=1]*4;m=2
while[print(L[-1]-L[-2])]:
 m+=1
 for q in 3,4:L+=sum(1//(k%q*2-1)*(c:=c*(m-k)//k)*L[-2*k]for k in range(1,m)),
```

**How it works**

- Let B_r(n) count the permutations of [n] whose runs all have length at
  most r; then a(n) = B_3(n) − B_2(n). With q = r + 1 their e.g.f. is
  1/D_q(x), D_q(x) = Σ_{j≥0} (x^(qj)/(qj)! − x^(qj+1)/(qj+1)!) (David and
  Barton; Alekseyev, arXiv:1205.4581, linked from the entry). Comparing
  coefficients in D_q·B_r = 1 gives, for n ≥ 1,

  B_r(n) = Σ_{k=1}^{n} C(n, k)·f_q(k)·B_r(n − k),

  with f_q(k) = 1 for k ≡ 1, −1 for k ≡ 0 and 0 otherwise (mod q).
- Both sequences live in one list, interleaved:
  `L` = B_2(0), B_3(0), B_2(1), B_3(1), … . When B_2(n) is appended `L`
  has 2n entries, so `L[-2*k]` is B_2(n − k); right after, it has 2n + 1
  entries and the same `L[-2*k]` is B_3(n − k). One expression serves
  both passes of `for q in 3,4`, and the newest pair gives
  `L[-1]-L[-2]` = a(n).
- `1//(k%q*2-1)` is f_q(k): x = 2·(k mod q) − 1 is −1, 1, 3 or 5, and
  ⌊1/x⌋ is then −1, 1, 0, 0. It stands first in the product, because
  `(c:=…)*1//(…)` would floor-divide the binomial instead.
- `c` walks the binomials C(n, 1), …, C(n, n) with m = n + 1:
  C(n, k) = C(n, k − 1)·(n − k + 1)/k, and the `//` is exact because
  C(n, k − 1)·(n − k + 1) = k·C(n, k). Each walk ends at C(n, n) = 1,
  which is exactly the start value the next walk needs, so `c` is set
  only once (`L=[c:=1]*4`).
- The list starts with B_2(0), B_3(0), B_2(1), B_3(1) = 1, 1, 1, 1 and
  m = 2, so the header prints a(1) = 0 before the first pass computes n = 2.

**Notes**

- `math.comb(n,k)` with a separate list per q (the [A000434](../A000434/)
  layout) is 166 bytes; with the interleaved list it is 139, and the
  self-resetting binomial walk brings it to 129. The sign tuple
  `(-1,1,0,0)[k%q]` in place of `1//(k%q*2-1)` is 3 bytes longer.
- Exact integer arithmetic; correctness for every n rests on the e.g.f.
  above. A brute-force count over all permutations agrees for n ≤ 8.
- The b-file has 452 terms (up to a(452)); the bar is the whole b-file in
  60 s, which takes under half a second here.
- a(n) grows like n!, and a(1567) is the first term with more than 4300
  digits: printing stops there, after about 18 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 167 | first entry |
| 2026-11-06 | Python 3 | 166 | import math for a single comb call |
| 2026-11-07 | Python 3 | 129 | interleaved list, self-resetting binomial walk |
| 2026-11-07 | Python 3 | 126 | f_q(k) as 1//(2(k mod q) − 1) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000402), CC BY-SA 4.0.
