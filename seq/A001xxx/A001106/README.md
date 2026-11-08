# A001106

> 9-gonal (or enneagonal or nonagonal) numbers: a(n) = n*(7*n-5)/2.
> — [OEIS A001106](https://oeis.org/A001106)

Offset 0: 0, 1, 9, 24, 46, 75, 111, 154, 204, 261, 325, 396, …

### Python 3 — 31 bytes

```python
m=5
while[print(m*m//56)]:m-=14
```

**How it works**

- With m = 5 − 14n, m² = 196n² − 140n + 25 = 56·a(n) + 25, because
  56·a(n) = 28n(7n − 5) = 196n² − 140n. Since 0 ≤ 25 < 56,
  ⌊m²/56⌋ = a(n) exactly, so `m*m//56` is the n-th 9-gonal number with no
  product of two factors and no halving.
- The step is forced: for ⌊(αn + β)²/c⌋ to give 3.5n² − 2.5n you need
  α²/c = 7/2 and 2αβ/c = −5/2, so β = −5α/14 and α must be a multiple of 14.
- `m-=14` walks m = 5, −9, −23, …; m = 14n − 5 gives the same squares but
  needs the start value `m=-5`, one byte more. The same completed square
  serves the pentagonal [A000326](../../A000xxx/A000326/), hexagonal
  [A000384](../../A000xxx/A000384/), heptagonal
  [A000566](../../A000xxx/A000566/), octagonal
  [A000567](../../A000xxx/A000567/) and 10-gonal [A001107](../A001107/)
  numbers.
- `while[print(…)]:` never ends: `print` returns `None` and `[None]` is a
  non-empty list (the [A000007](../../A000xxx/A000007/) loop).

**Notes**

- Other versions that print the same terms: the formula as given,
  `n=0` / `while[print(n*(7*n-5)//2)]:n+=1`: 35 bytes; adding the first
  differences 7n − 6, `a=d=0` / `while[print(a)]:a+=d+1;d+=7`: 33 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10001 terms (up to a(10000)); the bar is the whole b-file in
  60 s, and the program prints it in well under a second here.
- a(n) < 4n², so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001106), CC BY-SA 4.0.
