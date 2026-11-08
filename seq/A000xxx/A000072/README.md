# A000072

> Number of positive integers <= 2^n of form x^2 + 4 y^2.
> — [OEIS A000072](https://oeis.org/A000072)

Offset 0: 1, 1, 2, 4, 7, 12, 22, 41, 72, 137, 254, 476, 901, 1716, 3274, …

### Python 3 — 98 bytes

```python
n=0
while r:=range(1<<-~n//2|3):print(len({min(x*x+y*y,2**n+1)for x in r for y in r[::2]})-2);n+=1
```

**How it works**

- x² + 4y² is x² + Y² with Y = 2y even, so x runs over `r` and Y over the
  even numbers `r[::2]`. Signs do not matter, so x, Y ≥ 0.
- A value up to 2ⁿ has x, Y ≤ 2^(n/2) ≤ 2^c, where c = ⌈n/2⌉ is
  `-~n//2`. `range(1<<-~n//2|3)` holds 0 … 2^c: its length is 2^c + 3
  for c ≥ 2, and 3 for c ≤ 1, where `|3` makes up for 2^c being 1 or 2.
- `min(x*x+y*y,2**n+1)` turns every value above 2ⁿ into 2ⁿ + 1, and that
  value is always there: x = Y = 2 gives 8 > 2ⁿ + 1 for n ≤ 2, and
  x = Y = 2^c gives 2·4^c > 2ⁿ + 1 for n ≥ 1. So the set holds the values
  in [0, 2ⁿ] plus 2ⁿ + 1, and `-2` removes 0 = 0² + 0² and the 2ⁿ + 1.
- The range is never empty, so the `while` condition keeps the loop going
  while it names `r`.

**Speed**

- Term n costs |r|·|r[::2]| ≈ 2^(2c−1) pairs: about 2ⁿ⁻¹ for even n and
  2ⁿ for odd n. The 91-byte version used `range(2<<n//2)` for both x and y
  with `4*y*y`, which is 2ⁿ⁺² pairs for even n and 2ⁿ⁺¹ for odd n.
- The bar is 25 terms in 60 s, and it must come within half the timeout on
  the CI runner. The 91-byte version needed 46 s there. On the same local
  machine this version reaches a(24) in about 16 s against 68 s for the
  91-byte one; the b-file goes to n = 60, far beyond any enumeration.

**Notes**

- m is x² + 4y² exactly when m is a sum of two squares and m ≢ 2 (mod 4):
  an odd sum of two squares has one even square, and a multiple of 4 that
  is a² + b² has a and b both even. Hence the OEIS formula
  a(n) = A000050(n) − A000050(n−1) + A000050(n−2).
- Keeping `range(2<<n//2)` and only switching to even Y,
  `{min(x*x+y*y,2**n)for x in r for y in r[::2]}` with `-1`, is 92 bytes
  and twice as fast as the 91-byte version, but at about 24 s on the CI
  runner it sits too close to the 30 s limit. (It needs no `+1`: with that
  range, n = 1 never reaches the value 2.)
- Capping at 2ⁿ − 1 (`~-2**n`) with `-1` fixes n = 1, since 2ⁿ − 1 ≡ 3
  (mod 4) is never of the form, but gives a(0) = 0. Capping at 2ⁿ with
  `-1` and the tight range counts 2 at n = 1, which is not of the form.
- Enumerating only the ellipse x² + 4y² ≤ 2ⁿ with `math.isqrt` bounds is
  about three times faster again, but 130 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 92 | first entry |
| 2026-11-05 | Python 3 | 91 | value named in the while condition |
| 2026-11-08 | Python 3 | 98 | fix: tight ranges and even Y, so the bar comes within half the timeout |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000072), CC BY-SA 4.0.
