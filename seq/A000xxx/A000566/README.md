# A000566

> Heptagonal numbers (or 7-gonal numbers): n*(5*n-3)/2.
> — [OEIS A000566](https://oeis.org/A000566)

Offset 0: 0, 1, 7, 18, 34, 55, 81, 112, 148, 189, …

### Python 3 — 31 bytes

```python
m=3
while[print(m*m//40)]:m-=10
```

**How it works**

- With m = 3 − 10n, m² = 100n² − 60n + 9 = 40·a(n) + 9, because
  40·a(n) = 20n(5n − 3) = 100n² − 60n. Since 0 ≤ 9 < 40, ⌊m²/40⌋ = a(n)
  exactly, so `m*m//40` is the n-th heptagonal number with no product of
  two factors and no halving.
- `m-=10` walks m = 3, −7, −17, …; m = 10n − 3 gives the same squares, but
  its start value `m=-3` costs one more byte. The pentagonal
  [A000326](../A000326/) and hexagonal [A000384](../A000384/) pages use the
  same completed square.
- `while[print(…)]:` never ends: `print` returns `None` and `[None]` is a
  non-empty list (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: the formula as given,
  `n=0` / `while[print(n*(5*n-3)//2)]:n+=1`: 35 bytes; adding the first
  differences 5n − 4, `a=n=0` / `while[print(a)]:a+=n+1;n+=5`: 33 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10001 terms (up to a(10000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.2 s here.
- a(n) < 3n², so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |
| 2026-11-07 | Python 3 | 31 | completed square, `m*m//40` with m = 3 − 10n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000566), CC BY-SA 4.0.
