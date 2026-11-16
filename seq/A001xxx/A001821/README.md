# A001821

> Central factorial numbers: 3rd subdiagonal of A008955.
> — [OEIS A001821](https://oeis.org/A001821)

Offset 0: 1, 30, 1023, 44473, 2475473, 173721912, 15088541896, 1593719752240, …

### Python 3 — 73 bytes

```python
L=[p:=1]*4;m=3
while[print(p)]:p=0;m-=3;L=[p:=p+(m:=m+1)**2*x for x in L]
```

**How it works**

- **The triangle.** With T(m, j) = eⱼ(1², 2², …, m²), the coefficients of
  (1 + 1²x)⋯(1 + m²x) (rows of [A008955](https://oeis.org/A008955)), this
  sequence is the third subdiagonal a(n) = T(n + 3, n) = eₙ(1², …, (n + 3)²).
- **Diagonal recurrence.** From T(m, j) = T(m − 1, j) + m²·T(m − 1, j − 1),
  the diagonals dᵢ(n) = T(n + i, n) satisfy
  dᵢ(n + 1) = dᵢ₋₁(n + 1) + (n + 1 + i)²·dᵢ(n), with d₀(n) = (n!)²
  (d₋₁ = 0). So one step computes d₀(n + 1), d₁(n + 1), d₂(n + 1), d₃(n + 1)
  in this order, each from the one just made.
- **The program.** `L` = [d₀(n), …, d₃(n)], all 1 at n = 0. In
  `L=[p:=p+(m:=m+1)**2*x for x in L]` the walrus `p` carries the new value
  of the previous diagonal (it starts at 0 for d₀) and `m` runs over
  n + 1, …, n + 4; `m-=3` then moves the start up by one for the next
  step. After the pass p = d₃(n + 1), which the header prints. Four named
  variables (as in [A001820](../A001820/)) take 76 bytes.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 857.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001821), CC BY-SA 4.0.
