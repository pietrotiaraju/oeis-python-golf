# A001811

> Coefficients of Laguerre polynomials.
> — [OEIS A001811](https://oeis.org/A001811)

Offset 4: 1, 25, 450, 7350, 117600, 1905120, 31752000, 548856000, 9879408000, 185513328000, 3636061228800, 74373979680000, …

### Python 3 — 43 bytes

```python
a=1;n=4
while[print(a)]:n+=1;a=a*n*n//(n-4)
```

**How it works**

- **The Laguerre coefficient.** n!·L_n(x) = Σₖ (−1)ᵏ n!·C(n, k)/k!·xᵏ
  ([A021009](https://oeis.org/A021009)); this sequence is the absolute value
  of the x⁴ coefficient, a(n) = n!·C(n, 4)/4! = C(n, 4)²·(n − 4)!.
- **A ratio.** C(n, 4)² grows by (n/(n − 4))² and (n − 4)! by n − 4, so
  a(n) = a(n − 1)·n²/(n − 4), from a(4) = 1 (the OEIS formula
  a(n+1) = a(n)·(n + 1)²/(n − 3)).
- **The program.** `n` counts from 4; `a*n*n` is formed before `//(n-4)`, and
  the quotient is the integer a(n), so the division is exact.

**Notes**

- Checked against the exact Laguerre polynomials (three-term recurrence) for
  n < 90, and against the b-file.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1556.
- The b-file has 97 terms (n = 4 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001811), CC BY-SA 4.0.
