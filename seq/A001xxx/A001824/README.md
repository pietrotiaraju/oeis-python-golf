# A001824

> Central factorial numbers: 1st subdiagonal of A008956.
> — [OEIS A001824](https://oeis.org/A001824)

Offset 0: 1, 10, 259, 12916, 1057221, 128816766, 21878089479, 4940831601000, …

### Python 3 — 45 bytes

```python
a=f=k=1
while[print(a)]:f*=k*k;k+=2;a=a*k*k+f
```

**How it works**

- **The triangle.** Row m of [A008956](https://oeis.org/A008956) holds the
  elementary symmetric functions of the odd squares 1², 3², …, (2m − 1)².
  This sequence is its first subdiagonal, a(n) = eₙ(1², 3², …, (2n + 1)²),
  the sum of the n + 1 products that leave out one odd square:
  a(n) = ((2n + 1)!!)²·Σₖ₌₀..ₙ 1/(2k + 1)². By Joe Keane's formula on the
  OEIS page it is also (2n + 3)!/3! times the coefficient of x²ⁿ⁺³ in
  (arcsin x)³.
- **The recurrence.** Multiplying in the factor x + (2n + 1)² gives
  a(n) = (2n + 1)²·a(n − 1) + ((2n − 1)!!)².
- **The program.** `f` = ((2n − 1)!!)² and `k` = 2n + 1 when a(n) is
  printed; a pass multiplies f by k², steps k to 2n + 3 and makes
  a(n + 1) = k²·a(n) + f. Everything starts at 1, since (−1)!! = 1.
  [A001819](../A001819/) is the same recurrence over all squares.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 779.
- The b-file has 225 terms (n = 0 to 224); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001824), CC BY-SA 4.0.
