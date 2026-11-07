# A000567

> Octagonal numbers: n*(3*n-2). Also called star numbers.
> — [OEIS A000567](https://oeis.org/A000567)

Offset 0: 0, 1, 8, 21, 40, 65, 96, 133, 176, 225, …

### Python 3 — 29 bytes

```python
m=1
while[print(m*m//3)]:m-=3
```

**How it works**

- With m = 1 − 3n, m² = 9n² − 6n + 1 = 3·a(n) + 1, because
  3·a(n) = 3n(3n − 2) = 9n² − 6n. Since 0 ≤ 1 < 3, ⌊m²/3⌋ = a(n) exactly.
- `m-=3` walks m = 1, −2, −5, −8, …; m = 3n − 1 gives the same squares but
  needs the start value `m=-1`, one byte more. The same completed square
  serves the pentagonal [A000326](../A000326/), hexagonal
  [A000384](../A000384/) and heptagonal [A000566](../A000566/) numbers.
- `while[print(…)]:` never ends: `print` returns `None` and `[None]` is a
  non-empty list (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: the formula as given,
  `n=0` / `while[print(n*(3*n-2))]:n+=1`: 32 bytes; adding the first
  differences 6n − 5, `a=n=0` / `while[print(a)]:a+=n+1;n+=6`: 33 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) < 3n², so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |
| 2026-11-07 | Python 3 | 29 | completed square, `m*m//3` with m = 1 − 3n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000567), CC BY-SA 4.0.
