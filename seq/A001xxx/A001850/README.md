# A001850

> Central Delannoy numbers: a(n) = Sum_{k=0..n} C(n,k)*C(n+k,k).
> — [OEIS A001850](https://oeis.org/A001850)

Offset 0: 1, 3, 13, 63, 321, 1683, 8989, 48639, 265729, 1462563, …

### Python 3 — 53 bytes

```python
a=n=0;b=1
while[print(b)]:n+=1;a,b=b,6*b-a-(3*b-a)//n
```

**How it works**

- The generating function of Σₖ C(n, k)·C(n + k, k) is
  A = (1 − 6x + x²)^(−1/2) (on the OEIS page). Then
  (1 − 6x + x²)·A′ = (3 − x)·A, and the coefficient of xⁿ⁻¹ gives
  n·a(n) = 3(2n − 1)·a(n−1) − (n − 1)·a(n−2) for n ≥ 1, with a(−1) = 0
  (the recurrence in T. D. Noe's article, cited on the OEIS page).
- Splitting off n(6a(n−1) − a(n−2)) leaves
  a(n) = 6a(n−1) − a(n−2) − (3a(n−1) − a(n−2))/n, and that quotient is an
  integer because everything else is: `//n` is exact.
- `a`, `b` hold a(n−2), a(n−1), starting from a(−1) = 0, a(0) = 1.

**Notes**

- The sum Σₖ C(n, k)²·2ᵏ with `math.comb`, or the coefficient of xⁿ in
  (1 + 3x + 2x²)ⁿ read off a big base, are both longer.
- Exact integer arithmetic, so the program is right for every n; a(n) has
  about 0.77n digits, so Python's 4300-digit int-to-str limit stops the
  output near n = 5600.
- The b-file has 1309 terms (n = 0 to 1308); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001850), CC BY-SA 4.0.
