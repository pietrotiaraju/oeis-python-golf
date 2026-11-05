# A000063

> Symmetrical dissections of an n-gon.
> — [OEIS A000063](https://oeis.org/A000063)

Offset 5: 1, 1, 2, 4, 5, 14, 14, 39, 42, 132, 132, 424, 429, 1428, 1430, …

### Python 3 — 91 bytes

```python
d={1:1};n=5
while k:=n//2:d[k]=d[k-1]*(4*k-6)//k;print(d[k]-d.get(n/4,0)-d.get(n/6,0));n+=1
```

**How it works**

- Guy's formula (1958), quoted on the OEIS page:
  a(n) = C(⌊n/2⌋ − 1) − C(n/4 − 1) − C(n/6 − 1), where C is the Catalan
  number and C(x) = 0 when x is not an integer. So odd n gives
  a(2m + 1) = C(m − 1), and an even n loses a term for each of 4 and 6 that
  divides it: a(12) = C(5) − C(2) − C(1) = 42 − 2 − 1 = 39.
- The dict `d` holds d[k] = C(k − 1) for k = 1 … ⌊n/2⌋, built with
  C(k − 1) = C(k − 2)·(4k − 6)/k. With k = ⌊n/2⌋ the update writes the new
  key on even n and rewrites the same value on odd n, so no parity test is
  needed. Each division is exact, because the product is the next Catalan
  number times k.
- `d.get(n/4,0)` does the "0 when not an integer" part for free: n/4 is a
  float, and a float equal to an integer has the same hash and compares
  equal, so 3.0 finds the key 3, while 2.25 finds nothing and gives 0. n/4 and
  n/6 never pass ⌊n/2⌋, so every integer key they ask for is already there.
- `while k:=n//2:` sets k in the loop condition, and k ≥ 2 is always true.

**Notes**

- The formula is the one from R. K. Guy's paper, with exact integer
  arithmetic throughout, so the program is right for every n. a(n) is about
  2ⁿ: the program prints up to a(14307), which has 4300 digits, and then
  stops on Python's int-to-str limit (a `ValueError` on stderr). n/4 and n/6
  are exact floats for every n it gets that far.
- The whole b-file (996 terms, n = 5 … 1000) prints in under 0.1 s. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000063), CC BY-SA 4.0.
