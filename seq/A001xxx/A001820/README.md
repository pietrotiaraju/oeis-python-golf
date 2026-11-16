# A001820

> Central factorial numbers: 2nd subdiagonal of A008955.
> — [OEIS A001820](https://oeis.org/A001820)

Offset 0: 1, 14, 273, 7645, 296296, 15291640, 1017067024, 84865562640, 8689315795776, …

### Python 3 — 59 bytes

```python
b=c=f=1;k=2
while[print(c)]:b=b*k*k+f;f*=k*k;k+=1;c=c*k*k+b
```

**How it works**

- **The triangle.** Let T(m, j) = eⱼ(1², 2², …, m²), the coefficient of
  xʲ in (1 + 1²x)(1 + 2²x)⋯(1 + m²x); row m of
  [A008955](https://oeis.org/A008955) is T(m, 0), …, T(m, m). This sequence
  is its second subdiagonal, a(n) = T(n + 2, n): 1, 1 + 4 + 9 = 14,
  e₂(1, 4, 9, 16) = 273, …
- **Diagonal recurrence.** Multiplying in the factor 1 + m²x gives
  T(m, j) = T(m − 1, j) + m²·T(m − 1, j − 1). For the diagonals
  dᵢ(n) = T(n + i, n) that reads dᵢ(n) = dᵢ₋₁(n) + (n + i)²·dᵢ(n − 1), with
  d₀(n) = T(n, n) = (n!)². So d₁ ([A001819](../A001819/) shifted) feeds
  d₂ = a.
- **The program.** At step n, `b` = d₁(n), `c` = d₂(n), `f` = ((n + 1)!)²
  and `k` = n + 2, all starting at 1 except k = 2. One pass does
  `b=b*k*k+f` (d₁(n + 1) = d₀(n + 1) + (n + 2)²d₁(n)), `f*=k*k`,
  `k+=1` and `c=c*k*k+b` (d₂(n + 1) = d₁(n + 1) + (n + 3)²d₂(n)). Updating
  f between b and c lets one counter serve all three squares.
  [A001825](../A001825/) is the same program over odd squares.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 858.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001820), CC BY-SA 4.0.
