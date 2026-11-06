# A000426

> Coefficients of ménage hit polynomials.
> — [OEIS A000426](https://oeis.org/A000426)

Offset 1: 0, 1, 1, 1, 8, 35, 211, 1459, 11584, 103605, …

### Python 3 — 81 bytes

```python
m=b=c=d=1;a=0
while[print(a)]:m+=1;a,b,c,d=b,c,d,m*(b+c+d)+(m*c+d-b)//2+a+(-1)**m
```

**How it works**

This is the proved recurrence for the normalized ménage hit
coefficient used by [A000033](../A000033/), with its final factor
m omitted. At counter m, the state stores b(m), …, b(m+3),
initially 0,1,1,1. See A000033 and its recurrence certificate for
the telescoping proof of the integer update. The unnormalized
sequence is m*b(m), whereas this sequence is b(m).

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 100 terms in 60 s; the official b-file contains 100 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000426), CC BY-SA 4.0.
