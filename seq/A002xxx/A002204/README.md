# A002204

> An ill-conditioned determinant.
> — [OEIS A002204](https://oeis.org/A002204)

Offset 1: 1, 6, 720, 1512000, 53343360000, 31052236723200000, …

### Python 3 — 75 bytes

```python
from math import*
a=n=1
while[print(a)]:a*=comb(2*n,n)*comb(2*n+1,n)*n;n+=1
```

**How it works**

- **Definition used.** The entry's PARI program:
  a(n) = (−1)^(n+1)/det M_n, where the n×n matrix M_n has a first row of
  ones and entries 1/(i + j − 1) in rows i = 2…n (a Hilbert matrix with
  its first row replaced). It reproduces all 41 terms of the b-file.
- **Cauchy's determinant.** For rows i ≥ 2, 1/(i + j − 1) = 1/(x_i + y_j)
  with x_i = i and y_j = j − 1, and
  det[1/(x_i + y_j)] = ∏_(i<k) (x_k − x_i)(y_k − y_i) / ∏_(i,j) (x_i + y_j).
  Multiply the first row by x₁ and let x₁ → ∞: its entries
  x₁/(x₁ + y_j) tend to 1, and the factors containing x₁,
  x₁·∏_(k≥2) (x_k − x₁) / ∏_j (x₁ + y_j), tend to (−1)^(n−1). So
  det M_n = (−1)^(n−1)·∏_(2≤i<k≤n) (k − i)·∏_(1≤j<k≤n) (k − j) /
  ∏_(i=2..n, j=1..n) (i + j − 1), and
  a(n) = ∏_(i=1..n−1) (n+i)!/i! / (sf(n−2)·sf(n−1)), with
  sf(m) = 1!·2!⋯m!, a positive integer-valued closed form.
- **Ratio.** Dividing the closed form for n + 1 by the one for n gives
  a(n+1)/a(n) = (2n)!·(2n+1)!/((n−1)!·n!²·(n+1)!) = n·C(2n, n)·C(2n+1, n),
  which is the entry's recurrence a(n) = C(2n−2, n−2)·C(2n−2, n−1)·(2n−1)·a(n−1)
  written with one binomial fewer (C(2n, n−1)·(2n+1) = n·C(2n+1, n)).
  Exact integers, so every term is right.
- **Golf.** `while[print(a)]:` prints before each update; the three
  factors read the old n, and `n+=1` comes last.

**Notes**

- a(n) has about 0.6·n² digits: a(85) still prints, a(86) would pass
  Python's 4300-digit int-to-str limit, so the program stops there with a
  ValueError (an interpreter limit, not a wrong term).
- The b-file has 41 terms (n = 1 to 41); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002204), CC BY-SA 4.0.
