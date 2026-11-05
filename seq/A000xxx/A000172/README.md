# A000172

> The Franel number a(n) = Sum_{k = 0..n} binomial(n,k)^3.
> — [OEIS A000172](https://oeis.org/A000172)

Offset 0: 1, 2, 10, 56, 346, 2252, 15184, 104960, 739162, 5280932, …

### Python 3 — 68 bytes

```python
a=n=0;b=1
while[print(b)]:a,b=b,((7*n*-~n+2)*b+8*n*n*a)//(n:=n+1)//n
```

**How it works**

- Franel's recurrence (1894):
  (n+1)²·a(n+1) = (7n²+7n+2)·a(n) + 8n²·a(n−1), valid for every n ≥ 1, and
  at n = 0 it gives a(1) = 2 whatever a(−1) is, because its coefficient
  8n² vanishes. So `a` starts at 0 and `b` at a(0) = 1.
- `7*n*-~n+2` is 7n(n+1)+2, two bytes under `7*n*n+7*n+2`.
- The walrus in the divisor bumps n after the numerator has used the old
  value: `X//(n:=n+1)//n` is ⌊⌊X/(n+1)⌋/(n+1)⌋ = X/(n+1)², which saves the
  separate `;n+=1`. The division is exact because the numerator is
  (n+1)²·a(n+1).
- The plain sum, `sum(comb(n,k)**3for k in range(n+1))` with
  `from math import*`, is 77 bytes.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (1001 terms) prints at once; the program stops after a(4765), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000172), CC BY-SA 4.0.
