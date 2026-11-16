# A001825

> Central factorial numbers: 2nd subdiagonal of A008956.
> — [OEIS A001825](https://oeis.org/A001825)

Offset 0: 1, 35, 1974, 172810, 21967231, 3841278805, 886165820604, 261042753755556, …

### Python 3 — 59 bytes

```python
b=c=f=1;k=3
while[print(c)]:b=b*k*k+f;f*=k*k;k+=2;c=c*k*k+b
```

**How it works**

- **The triangle.** With T(m, j) = eⱼ(1², 3², …, (2m − 1)²), the rows of
  [A008956](https://oeis.org/A008956), this sequence is the second
  subdiagonal a(n) = T(n + 2, n) = eₙ(1², 3², …, (2n + 3)²): 1,
  1 + 9 + 25 = 35, 1974, … By Joe Keane's formula on the OEIS page it is
  also (2n + 5)!/5! times the coefficient of x²ⁿ⁺⁵ in (arcsin x)⁵.
- **Diagonal recurrence.** T(m, j) = T(m − 1, j) + (2m − 1)²·T(m − 1, j − 1),
  so the diagonals dᵢ(n) = T(n + i, n) satisfy
  dᵢ(n) = dᵢ₋₁(n) + (2n + 2i − 1)²·dᵢ(n − 1), with d₀(n) = ((2n − 1)!!)².
  d₁ is [A001824](../A001824/), and it feeds d₂ = a.
- **The program.** At step n, `b` = d₁(n), `c` = d₂(n),
  `f` = ((2n + 1)!!)² and `k` = 2n + 3. A pass does `b=b*k*k+f`,
  `f*=k*k`, `k+=2` and `c=c*k*k+b`: one counter serves the three odd
  squares because f is updated between b and c. It is
  [A001820](../A001820/)'s program with odd squares (k = 3, step 2).

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 778.
- The b-file has 51 terms (n = 0 to 50); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001825), CC BY-SA 4.0.
