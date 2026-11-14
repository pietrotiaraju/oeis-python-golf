# A001701

> Generalized Stirling numbers, [n+2,n]_2.
> — [OEIS A001701](https://oeis.org/A001701)

Offset 1: 1, 6, 26, 71, 155, 295, 511, 826, 1266, 1860, 2640, 3641, 4901, 6461, 8365, 10660, 13396, 16626, …

### Python 3 — 47 bytes

```python
a=0;s=c=2
while[print(a or 1)]:c+=1;a+=c*s;s+=c
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). With N = n + 2 and K = n that is the coefficient of xⁿ⁻² in the n
  factors (x+2)(x+3)⋯(x+n+1), i.e. the second elementary symmetric function
  e₂(2, 3, …, n+1): the sum of i·j over all pairs 2 ≤ i < j ≤ n + 1. (This is
  the entry's closed form n(n−1)(3n²+17n+26)/24 for n > 1.)
- Adding a number c to a set raises e₂ by c times the old e₁. The program keeps
  a = e₂ and s = e₁ of the set {2, …, c}: it starts from {2} (a = 0,
  s = c = 2), prints, and each pass adds c + 1, so the k-th print belongs to
  {2, …, k+1}.
- For n = 1 the definition gives an empty sum, but the entry lists a(1) = 1
  (its generating functions include that term, and its closed form is stated
  for n > 1). The program follows the data: the first print, for the set {2},
  has a = 0, and `a or 1` turns exactly that one into 1, since every later a
  is positive.

**Notes**

- Exact integer arithmetic, correct for every n (the values are polynomial in
  n, far from the 4300-digit limit). The whole b-file (1000 terms) prints at
  once; the bar is the whole b-file in 60 s.
- The closed form with the same patch,
  `n=1` / `while[print(n*~-n*(3*n*n+17*n+26)//24or 1)]:n+=1`, is 52 bytes.
- [A001702](../A001702/) is the next one, e₃.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001701), CC BY-SA 4.0.
