# A001812

> Coefficients of Laguerre polynomials.
> — [OEIS A001812](https://oeis.org/A001812)

Offset 5: 1, 36, 882, 18816, 381024, 7620480, 153679680, 3161410560, 66784798080, 1454424491520, 32724551059200, 761589551923200, …

### Python 3 — 43 bytes

```python
a=1;n=5
while[print(a)]:n+=1;a=a*n*n//(n-5)
```

**How it works**

- **The Laguerre coefficient.** n!·L_n(x) = Σₖ (−1)ᵏ n!·C(n, k)/k!·xᵏ
  ([A021009](https://oeis.org/A021009)); this sequence is the absolute value
  of the x⁵ coefficient, a(n) = n!·C(n, 5)/5! = (n!/5!)²/(n − 5)!
  = C(n, 5)²·(n − 5)!.
- **A ratio.** C(n, 5)² grows by (n/(n − 5))² and (n − 5)! by n − 5, so
  a(n) = a(n − 1)·n²/(n − 5), from a(5) = 1.
- **The program.** `n` counts from 5; `a*n*n` is formed before `//(n-5)`, and
  the quotient is the integer a(n), so the division is exact.

**Notes**

- Checked against the exact Laguerre polynomials (three-term recurrence) for
  n < 90, and against the b-file.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1555.
- The b-file has 96 terms (n = 5 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001812), CC BY-SA 4.0.
