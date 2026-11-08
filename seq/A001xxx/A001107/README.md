# A001107

> 10-gonal (or decagonal) numbers: a(n) = n*(4*n-3).
> — [OEIS A001107](https://oeis.org/A001107)

Offset 0: 0, 1, 10, 27, 52, 85, 126, 175, 232, 297, 370, 451, …

### Python 3 — 29 bytes

```python
m=3
while[print(m*m>>4)]:m-=8
```

**How it works**

- With m = 3 − 8n, m² = 64n² − 48n + 9 = 16·a(n) + 9, because
  16·a(n) = 16n(4n − 3) = 64n² − 48n. Since 0 ≤ 9 < 16, ⌊m²/16⌋ = a(n)
  exactly, and the division by 16 is the shift `>>4`, one byte under `//16`.
- For ⌊(αn + β)²/c⌋ = 4n² − 3n you need α² = 4c and β = −3α/8, so α = 8 is
  the smallest step. The same completed square serves the octagonal
  [A000567](../../A000xxx/A000567/) and 9-gonal [A001106](../A001106/)
  numbers (and the pentagonal, hexagonal and heptagonal pages linked
  there).
- `m-=8` walks m = 3, −5, −13, …; m = 8n − 3 gives the same squares but
  needs the start value `m=-3`, one byte more.

**Notes**

- Other versions that print the same terms: the formula as given,
  `n=0` / `while[print(n*(4*n-3))]:n+=1`: 32 bytes; adding the first
  differences 8n − 7, `a=d=0` / `while[print(a)]:a+=d+1;d+=8`: 33 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) < 4n², so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001107), CC BY-SA 4.0.
