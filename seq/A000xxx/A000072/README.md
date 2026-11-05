# A000072

> Number of positive integers <= 2^n of form x^2 + 4 y^2.
> — [OEIS A000072](https://oeis.org/A000072)

Offset 0: 1, 1, 2, 4, 7, 12, 22, 41, 72, 137, 254, 476, 901, 1716, 3274, …

### Python 3 — 92 bytes

```python
n=0
while 1:r=range(2<<n//2);print(len({min(x*x+4*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

- This is the [A000050](../A000050/) program with `4*` in front of `y*y`
  and a different cap. Signs do not matter, so x, y ≥ 0, and any value up
  to 2ⁿ has x ≤ 2^(n/2) and y ≤ 2^(n/2)/2. `range(2<<n//2)` goes past both
  bounds for every n, so one range serves both variables.
- `min(x*x+4*y*y,2**n+1)` turns every value above 2ⁿ into 2ⁿ + 1. The
  largest pair, x = y = 2^(n//2+1) − 1, always goes past 2ⁿ + 1, so the set
  holds the values in [0, 2ⁿ] plus 2ⁿ + 1. `-2` removes 0 = 0² + 4·0² and
  the 2ⁿ + 1.
- A000050 caps at 2ⁿ itself and subtracts 1, which works because 2ⁿ is
  always a sum of two squares. Here it is not always of the form: 2 = 2¹ is
  not x² + 4y², so that version prints 2 for a(1) = 1. Every other 2ⁿ is
  of the form, (2^k)² + 4·0² when n = 2k and (2^k)² + 4·(2^(k−1))² when
  n = 2k+1 ≥ 3, so n = 1 is the only term the `+1` is there for.

**Notes**

- m is x² + 4y² exactly when m is a sum of two squares and m ≢ 2 (mod 4):
  an odd sum of two squares has one even square, and a multiple of 4 that
  is a² + b² has a and b both even. Hence the OEIS formula
  a(n) = A000050(n) − A000050(n−1) + A000050(n−2).
- That gives a 93-byte version, A000050 with y running over even numbers
  only: `{min(x*x+y*y,2**n)for x in r for y in r[::2]}` with `-1`. It
  needs no `+1` because at n = 1 every value is at most 1, but `[::2]`
  costs 5 bytes where `4*` and `+1` cost 4.
- Capping at 2ⁿ − 1 (`~-2**n`, same length as `2**n+1`) also fixes n = 1,
  since 2ⁿ − 1 ≡ 3 (mod 4) is never of the form, but then a(0) comes out 0.
- Term n costs (2<<n//2)² pairs, between 2ⁿ⁺¹ and 2ⁿ⁺² of them, and the
  set grows to a(n) elements. The program prints a(0)…a(24) in about 33 s
  and a(25) at about 54 s. The bar is 25 terms in 60 s, the same as
  A000050; the b-file goes to n = 60, far beyond any enumeration.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000072), CC BY-SA 4.0.
