# A001892

> Number of permutations of (1,...,n) having n-2 inversions (n>=2).
> — [OEIS A001892](https://oeis.org/A001892)

Offset 2: 1, 2, 5, 15, 49, 169, 602, 2191, 8095, 30239, 113906, 431886, 1646177, …

### Python 3 — 84 bytes

```python
p=[1];z=[s:=0]
while 1:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)];print(p[len(z)-2])
```

**How it works**

- Counting the permutations of n letters by inversions gives the Mahonian
  polynomial [1]·[2]⋯[n], with [m] = 1 + x + ⋯ + x^(m−1), and a(n) is its
  coefficient of xⁿ⁻².
- The multiplication is the one of [A000707](../../A000xxx/A000707/):
  `z` holds m zeros, `zip(p+z,z+p)` pairs each coefficient with the one m
  places earlier, so `a-b` runs over p·(1 − x^m), and the running sum `s`
  divides by 1 − x. The coefficients of p·(1 − x^m) add up to 0, so `s` is
  back to 0 after every round (it is set once, in `z=[s:=0]`), and p picks
  up one trailing zero per round.
- A000707 prints before multiplying; here the first term is a(2), so the
  loop multiplies first: after `z+=0,` there are m zeros, p becomes
  [1]⋯[m], and `p[len(z)-2]` is a(m), starting at m = 2.

**Notes**

- Exact integer additions; the only fact used is the product formula for
  inversions, so the program is right for every n.
- p keeps the whole product, about m²/2 integers, so time and memory grow
  like m³: here about 500 terms in 15 s using 190 MB. The timeout is 15 s
  to keep a run under 300 MB.
- The pentagonal-number form a(n) = Σ_j (−1)^j·C(2n − 3 − j(3j−1)/2, n − 1)
  (Euler's pentagonal theorem, valid since n − 2 < n) is fast, but `comb`
  refuses negative arguments and the guard makes it longer (see A000707).
- The b-file has 999 terms (n = 2 to 1000); the bar is 400 terms in 15 s.
- [A001893](../A001893/) and [A001894](../A001894/) read the coefficients
  of xⁿ⁻³ and xⁿ⁻⁴ of the same product.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001892), CC BY-SA 4.0.
