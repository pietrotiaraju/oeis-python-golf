# A000424

> Differences of reciprocals of unity.
> — [OEIS A000424](https://oeis.org/A000424)

Offset 1: 7, 85, 1660, 48076, 1942416, 104587344, 7245893376, 628308907776, 66687811660800, 8506654697548800, …

a(n) is column 2 of the David–Kendall–Barton table A008969: with m = n + 1,
a(n) = m!²·Σ_{1≤i≤j≤m} 1/(i·j), m!² times the complete homogeneous symmetric
function h₂(1, 1/2, …, 1/m).

### Python 3 — 56 bytes

```python
a=s=f=m=1
while 1:m+=1;s=m*s+f;a=m*m*a+f*s;f*=m;print(a)
```

**How it works**

- The OEIS formula (Alcover, after Heinz in A008969) is a(n) = T(n+1, 2) =
  m!²·F(m) with F(m) = Σ_{j=1}^{m} (−1)^(j+1)·C(m, j)/j². Pascal's rule
  C(m, j) − C(m−1, j) = C(m−1, j−1) = (j/m)·C(m, j) gives
  F(m) − F(m−1) = H_m/m, where H_m = Σ_j (−1)^(j+1)·C(m, j)/j is the harmonic
  number (the same step one level down, from Σ_{j≥1} (−1)^(j+1)·C(m, j) = 1).
  So F(m) = Σ_{k≤m} H_k/k = Σ_{i≤k≤m} 1/(i·k) = h₂(1, …, 1/m).
- Put A_m = m!²·F(m) and S_m = m!·H_m ([A000254](https://oeis.org/A000254)).
  Multiplying F(m) = F(m−1) + H_m/m by m!² gives
  A_m = m²·A_{m−1} + (m−1)!·S_m, and S_m = m·S_{m−1} + (m−1)!.
- The loop holds a = A_{m−1}, s = S_{m−1} and f = (m−1)! after `m+=1`:
  `s=m*s+f` makes S_m, `a=m*m*a+f*s` makes A_m from the new s, `f*=m`
  makes m!, and `print(a)` prints A_m = a(m−1). The start
  `a=s=f=m=1` is A_1 = S_1 = 1! = 1, so the first print is
  A_2 = 4·1 + 1·3 = 7.

**Notes**

- Kotesovec's order-3 recurrence a(n) = (3n² + 3n + 1)a(n−1) − 3n⁴a(n−2) +
  (n−1)³n³a(n−3): 86 bytes. Printing through walruses,
  `while[print(a:=f*(s:=(m:=m+1)*s+f)+m*m*a)]:f*=m`: 57. Starting from
  `a=7;s=3;f=m=2` with `while[print(a)]:`: 59. The Stirling form
  a(n) = c(m+1, 2)² − m!·c(m+1, 3) (unsigned Stirling numbers of the first
  kind, h₂ = e₁² − e₂): 60.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 16 terms (up to a(16)); the bar is the whole b-file in 60 s.
- a(859) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there (858 terms, in a fraction of a
  second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 86 | first entry |
| 2026-11-07 | Python 3 | 56 | m!²·h₂(1, …, 1/m) with the harmonic numerators m!·H_m |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000424), CC BY-SA 4.0.
