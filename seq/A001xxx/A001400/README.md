# A001400

> Number of partitions of n into at most 4 parts.
> — [OEIS A001400](https://oeis.org/A001400)

Offset 0: 1, 1, 2, 3, 5, 6, 9, 11, 15, 18, 23, 27, 34, 39, 47, 54, 64, 72, 84, 94, 108, …

### Python 3 — 49 bytes

```python
m=5
while[print((m*(m*m-12+m%2*9)+99)//144)]:m+=1
```

**How it works**

- With m = n + 5, Michael Somos's formula in the entry reads
  a(n) = round((2m³ − 15m − 9m(−1)ᵐ)/288). For even m the fraction is
  (m³ − 12m)/144, for odd m it is (m³ − 3m)/144, so it is Q(m)/144 with
  Q(m) = m(m² − 12 + 9·(m mod 2)): that is `m*(m*m-12+m%2*9)`.
- **Why it holds for every n.** The generating function
  1/((1−x)(1−x²)(1−x³)(1−x⁴)) has a pole of order 4 at 1, of order 2 at −1
  and simple poles at the other cube and fourth roots of unity, so a(n) is
  a cubic in n plus a linear polynomial times (−1)ⁿ plus terms of period 3
  and 4. Comtet's exact formula (also in the entry, there for partitions
  into exactly 4 parts, i.e. shifted by 4) shows that the first two parts
  together are Q(m)/144, so E(n) = 144·a(n) − Q(m) has period 12. Over one
  period it takes the values 34, 0, −34, 16, 18, −16, −2, 0, 2, 16, −18, −16,
  all in [−34, 34]. Hence 0 ≤ 99 − E(n) < 144, which is exactly
  ⌊(Q(m) + 99)/144⌋ = a(n). Any constant from 34 to 109 works; 99 is a
  two-digit one.
- Exact integer arithmetic throughout, so the program is right for every n.

**Notes**

- The coin-change template of [A001401](../A001401/) (coins 2, 3, 4 after
  the pennies) is 59 bytes here.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001400), CC BY-SA 4.0.
