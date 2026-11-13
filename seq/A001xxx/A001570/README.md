# A001570

> Numbers k such that k^2 is centered hexagonal.
> — [OEIS A001570](https://oeis.org/A001570)

Offset 1: 1, 13, 181, 2521, 35113, 489061, 6811741, 94875313, 1321442641, …

### Python 3 — 34 bytes

```python
a=b=1
while[print(a)]:a,b=14*a-b,a
```

**How it works**

- The centered hexagonal numbers are 3m(m + 1) + 1, m ≥ 0. Multiplying
  k² = 3m(m + 1) + 1 by 4 gives **(2k)² − 3(2m + 1)² = 1**, so (x, y) =
  (2k, 2m + 1) is a solution of the Pell equation x² − 3y² = 1 with x even
  and y odd, and every such solution gives a term.
- All positive solutions are x + y√3 = (2 + √3)ʲ, j ≥ 0 (2 + √3 is the
  fundamental solution). From x′ = 2x + 3y, y′ = x + 2y the parities of x
  and y swap at each step, so x is even (and then y is odd, as
  3y² = x² − 1) exactly for odd j: x = 2, 26, 362, …, k = 1, 13, 181, ….
- Two steps multiply by (2 + √3)² = 7 + 4√3, whose trace is 14, so the
  x of every other solution satisfies x″ = 14x′ − x, and so does k = x/2:
  **a(n + 1) = 14·a(n) − a(n − 1)**. Running it back once gives
  14·1 − 13 = 1, so `a=b=1` (term and the one before it) starts the loop.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.14·n digits; the 4300-digit int-to-str limit is reached near
  n = 3700.
- The bar is the whole b-file (870 terms), which prints in well under a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001570), CC BY-SA 4.0.
