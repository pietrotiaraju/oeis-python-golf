# A000748

> Expansion of bracket function.
> — [OEIS A000748](https://oeis.org/A000748)

Offset 0: 1, -3, 6, -9, 9, 0, -27, 81, -162, 243, -243, 0, 729, -2187, 4374, -6561, …

### Python 3 — 35 bytes

```python
x=y=1
while[print(x)]:y=x-3*y;x=y-x
```

**How it works**

- The g.f. is 1/((1 + x)³ − x³) = 1/(1 + 3x + 3x²), so
  a(n+1) = −3a(n) − 3a(n−1). Instead of the pair (a(n), a(n−1)) the
  program keeps x = a(n) and y = a(n) + a(n−1), the coefficients of A and
  (1 + x)A. Both are 1 at n = 0, so the start is `x=y=1`.
- In the new pair, y′ = a(n+1) + a(n) = −3(a(n) + a(n−1)) + a(n) = x − 3y,
  and then a(n+1) = y′ − x. Two plain assignments in that order,
  `y=x-3*y;x=y-x`, need no tuple and no temporary.
- That is 2 bytes under the usual `a,b=1,0` / `a,b=-3*(a+b),a`. A search
  over all two-variable update chains with small coefficients found
  nothing shorter.

**Notes**

- Exact integer arithmetic. |a(n)| ≤ 2·3^(n/2) (the roots of 1 + 3t + 3t²
  have modulus 1/√3), so terms have about 0.24n digits and the
  4300-digit int-to-str limit is reached only near n = 18 000, after the
  b-file.
- The whole b-file (1001 terms) prints in well under a second; the bar is
  the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000748), CC BY-SA 4.0.
