# A000434

> Number of permutations of [n] in which the longest increasing run has length 4.
> — [OEIS A000434](https://oeis.org/A000434)

Offset 1: 0, 0, 0, 1, 8, 67, 602, 5811, 60875, 690729, …

A run is a maximal block of consecutive positions whose entries increase, so
for n = 5 the permutation 1 2 3 5 4 counts (runs 1235 and 4).

### Python 3 — 126 bytes

```python
L=[c:=1]*4;m=2
while[print(L[-1]-L[-2])]:
 m+=1
 for q in 4,5:L+=sum(1//(k%q*2-1)*(c:=c*(m-k)//k)*L[-2*k]for k in range(1,m)),
```

**How it works**

- Let B_r(n) count the permutations of [n] whose runs all have length at
  most r; then a(n) = B_4(n) − B_3(n). With q = r + 1 their e.g.f. is
  1/D_q(x), D_q(x) = Σ_{j≥0} (x^(qj)/(qj)! − x^(qj+1)/(qj+1)!) (David and
  Barton; Alekseyev, arXiv:1205.4581, linked from the entry). Comparing
  coefficients in D_q·B_r = 1 gives, for n ≥ 1,

  B_r(n) = Σ_{k=1}^{n} C(n, k)·f_q(k)·B_r(n − k),

  with f_q(k) = 1 for k ≡ 1, −1 for k ≡ 0 and 0 otherwise (mod q).
- `1//(k%q*2-1)` is f_q(k): with r = k mod q the divisor 2r − 1 is −1, 1,
  3, 5, 7, … and the floor of 1 over it is −1, 1, 0, 0, 0, … .
- Both sequences live in one list, interleaved: `L` = B_3(0), B_4(0),
  B_3(1), B_4(1), … . When B_3(n) is appended `L` has 2n entries, so
  `L[-2*k]` is B_3(n − k); right after, it has 2n + 1 entries and the same
  `L[-2*k]` is B_4(n − k). `L[-1]-L[-2]` is the newest pair's difference,
  a(n).
- `c` walks the binomials C(n, 1), …, C(n, n) with m = n + 1:
  C(n, k) = C(n, k − 1)·(n − k + 1)/k, and the `//` is exact because
  C(n, k − 1)·(n − k + 1) = k·C(n, k). The walk sits inside the product, so
  it advances even when f_q(k) = 0, and it ends at C(n, n) = 1, the start the
  next walk needs: `c` is set once (`L=[c:=1]*4`).
- The list starts with B_3(0), B_4(0), B_3(1), B_4(1) = 1, 1, 1, 1 and
  m = 2, so the header prints a(1) = 0 before the first pass computes n = 2.

**Notes**

- This is the [A000402](../A000402/) program (runs of length 3) with q = 4, 5
  and `1//(k%q*2-1)` in place of the tuple `(-1,1,0,0)[k%q]`; with the tuple
  `(-1,1,0,0,0)` it is 131 bytes. A separate list per q with `math.comb`, as
  in [A000456](../A000456/): 166.
- Exact integer arithmetic; correctness for every n rests on the e.g.f.
  above.
- The b-file has 450 terms (up to a(450)); the bar is the whole b-file in
  60 s, which takes about half a second here.
- a(n) grows like n!, and a(1560) is the first term with more than 4300
  digits: printing stops there, after about 18 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 167 | first entry |
| 2026-11-06 | Python 3 | 166 | import math for a single comb call |
| 2026-11-07 | Python 3 | 126 | interleaved list and binomial walk of A000402, f_q(k) as `1//(k%q*2-1)` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000434), CC BY-SA 4.0.
