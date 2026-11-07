# A000911

> a(n) = (2n+3)! /( n! * (n+1)! ).
> — [OEIS A000911](https://oeis.org/A000911)

Offset 0: 6, 60, 420, 2520, 13860, 72072, 360360, 1750320, 8314020, 38798760, …

### Python 3 — 41 bytes

```python
a=6;n=0
while[print(a)]:n+=1;a=4*a+6*a//n
```

**How it works**

- a(n)/a(n−1) = (2n+3)(2n+2)/(n(n+1)) = 2(2n+3)/n (R. J. Mathar's
  n·a(n) = 2(2n+3)·a(n−1) on the OEIS page).
- Split as 2(2n+3)/n = 4 + 6/n: a(n) = 4a(n−1) + 6a(n−1)/n. The second
  part is a(n) − 4a(n−1), an integer, so `6*a//n` is exact, and
  `4*a+6*a//n` is 2 bytes under `a*(4*n+6)//n`.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. The program prints 7132 terms in about a second and then stops
  with a `ValueError` at the 4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000911), CC BY-SA 4.0.
