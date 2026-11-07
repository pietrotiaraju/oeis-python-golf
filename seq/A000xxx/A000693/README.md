# A000693

> Related to population of numbers of form x^2 + y^2.
> — [OEIS A000693](https://oeis.org/A000693)

Offset 1: 1, 2, 3, 6, 10, 19, 35, 62, 118, 219, 414, 783, 1497, …

### Python 3 — 93 bytes

```python
n=p=1
while r:=range(2<<n//2):print(p:=len({min(x*x+y*y,2**n)for x in r for y in r})+~p);n+=1
```

**How it works**

- The OEIS definition is a(1) = 1, a(2) = 2 and a(n) = A000074(n) + a(n−2),
  where [A000074](../A000074/)(j) counts the odd sums of two squares up to
  2ʲ. Unrolled, a(n) = [n even] + Σ A000074(j) over j ≤ n with j ≡ n (mod 2).
- Each odd sum of two squares v ≤ 2ʲ with j = n − 2i is the number 4ⁱv ≤ 2ⁿ,
  and the extra 1 for even n is 2ⁿ = 4^(n/2)·1. So a(n) counts the sums of
  two squares w ≤ 2ⁿ whose 2-adic valuation is even (w = 4ⁱ·odd).
- Halving maps the sums of two squares with odd valuation up to 2ⁿ onto those
  with even valuation up to 2ⁿ⁻¹ (w is a sum of two squares exactly when
  2w is). Hence a(n) = [A000050](../A000050/)(n) − a(n−1) with a(0) = 1,
  where A000050(n) counts all sums of two squares in 1 … 2ⁿ.
- The set is A000050's: `min(x*x+y*y,2**n)` sends every value above 2ⁿ to
  2ⁿ, which is itself a sum of two squares, and 0 is removed by the −1.
  `+~p` is −1 − p, so `p:=len(…)+~p` turns the count into a(n).
- `range(2<<n//2)` reaches past √(2ⁿ), and `while r:=range(…)` is always
  true.

**Notes**

- Exact integer counting, so the program is right for every n; the
  recurrence agrees with the OEIS data through a(34).
- Term n costs (2<<n//2)² pairs, about 2ⁿ⁺¹. a(1) … a(21) print in about
  11 s, a(22) at 30 s and a(23) at 54 s. The bar is 21 terms in 60 s.
- Adding A000074's odd count to a(n−2), `p,q=q,p+len(…)-1`, is 104 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000693), CC BY-SA 4.0.
