# A000067

> Number of positive integers <= 2^n of form x^2 + 2 y^2.
> — [OEIS A000067](https://oeis.org/A000067)

Offset 0: 1, 2, 4, 6, 10, 18, 33, 60, 111, 205, 385, 725, 1374, 2610, …

### Python 3 — 90 bytes

```python
n=0
while 1:r=range(2<<n//2);print(len({min(x*x+2*y*y,2**n)for x in r for y in r})-1);n+=1
```

**How it works**

- This is the [A000050](../A000050/) program with `2*` in front of `y*y`.
  Signs do not matter, so x, y ≥ 0, and any value up to 2ⁿ has
  x ≤ 2^(n/2) and y ≤ 2^((n−1)/2). `range(2<<n//2)` goes past both bounds
  for every n, so one range serves both variables.
- `min(x*x+2*y*y,2**n)` turns every value above 2ⁿ into 2ⁿ. That adds
  nothing new to the set, because 2ⁿ has the form itself: (2^k)² + 2·0²
  when n = 2k, and 0² + 2·(2^k)² when n = 2k+1. So the set holds exactly
  the values in [0, 2ⁿ], without an `if` filter.
- 0 = 0² + 2·0² is in the set and is not positive, so `-1` removes it.

**Notes**

- Term n costs (2<<n//2)² pairs, between 2ⁿ⁺¹ and 2ⁿ⁺² of them, and the
  set grows to a(n) elements. The program prints a(0)…a(23) in about 14 s
  and a(24) at about 37 s. The bar is 24 terms in 60 s; the b-file goes to
  n = 58, far beyond any enumeration.
- A number is of this form exactly when every prime ≡ 5 or 7 (mod 8)
  divides it to an even power, but testing that for every m ≤ 2ⁿ is both
  longer and no faster than the enumeration.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000067), CC BY-SA 4.0.
