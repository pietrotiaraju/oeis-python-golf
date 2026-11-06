# A000406

> Coefficients of iterated exponentials.
> — [OEIS A000406](https://oeis.org/A000406)

Offset 1: 1, 6, 57, 741, 12244, 245755, 5809875, 158198200, 4877852505, 168055077875, …

### Python 3 — 85 bytes

```python
Q=[[t:=1]]*6
while Q:=[[t]+[t:=t+i*x for i,x in enumerate(L)]for L in Q]:print(t);t=0
```

**How it works**

This is the exact Stirling-transform antidiagonal algorithm of
[A000310](../A000310/), with two additional transform levels.
Apply the first-kind Stirling transform six times to the series x.
Each level obeys T(i+1,k) = i*T(i,k) + T(i,k+1).
The carried value `t` starts at 1 and is 0 after the first pass,
providing the coefficients of x to the innermost level.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 100 terms in 60 s; the official b-file contains 100 terms.
- Python 3.11+ eventually reaches its default 4300-digit integer-to-string limit; this interpreter limit is not counted as a correctness failure.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000406), CC BY-SA 4.0.
