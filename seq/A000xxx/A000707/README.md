# A000707

> Number of permutations of [1,2,...,n] with n-1 inversions.
> — [OEIS A000707](https://oeis.org/A000707)

Offset 1: 1, 1, 2, 6, 20, 71, 259, 961, 3606, 13640, 51909, 198497, 762007, 2934764, …

### Python 3 — 83 bytes

```python
p=[1];z=[s:=0]
while[print(p[len(z)-1])]:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)]
```

**How it works**

- Counting permutations of n letters by inversions gives the Mahonian
  polynomial [1]·[2]⋯[n], with [m] = 1 + x + ⋯ + x^(m−1), and a(n) is its
  coefficient of xⁿ⁻¹.
- The multiplication is the one of [A000140](../A000140/): `z` holds m
  zeros, `zip(p+z,z+p)` pairs each coefficient with the one m places
  earlier, so `a-b` runs over p·(1 − x^m), and the running sum `s` divides
  by 1 − x. The coefficients of p·(1 − x^m) add up to 0, so `s` is back to
  0 at the end of every round (it is set once, in `z=[s:=0]`), and p picks
  up one trailing zero per round.
- At the print, `z` has m zeros and p = [1]⋯[m], so `p[len(z)-1]` is a(m);
  then `z` grows and p is multiplied by [m+1]. The first factor used is
  [2], since p = [1] already stands for [1].

**Notes**

- Exact integer additions; the only fact used is the product formula for
  inversions.
- p keeps the whole product, about m²/2 integers, the middle ones about
  log₂ m! bits long, so memory grows like m³·log m: 542 terms in 15 s
  here, using about 230 MB, and about 740 terms (530 MB) in 60 s. The
  timeout is 15 s to keep a run under 300 MB.
- The pentagonal-number form a(n+1) = Σₘ (−1)ᵐ C(2n − m(3m−1)/2, n) is fast
  and needs no memory, but `comb` refuses negative arguments, and the
  guard made it about 115 bytes; reading the digit n−1 of
  ∏ (Bⁱ−1)/(B−1) with B = 4ⁿ was 96.
- The b-file has 1665 terms; the bar is 420 terms in 15 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000707), CC BY-SA 4.0.
