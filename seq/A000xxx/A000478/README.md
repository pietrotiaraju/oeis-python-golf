# A000478

> Number of ways of placing n labeled balls into 3 indistinguishable boxes with at least 2 balls in each box.
> — [OEIS A000478](https://oeis.org/A000478)

Offset 6: 15, 105, 490, 1918, 6825, 22935, 74316, 235092, 731731, 2252341, …

### Python 3 — 61 bytes

```python
n=6
while 1:print((6*(1+n+n*n)-3*(n+2)*2**n+2*3**n)//12);n+=1
```

**How it works**

Expand (exp(x)-1-x)³/3! and extract the n-th exponential
coefficient. It gives (1+n+n²)/2-(1/2+n/4)*2^n+3^n/6,
the OEIS formula. A common denominator of 12 keeps every
intermediate value integral. The first possible size is n=6.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 195 terms in 60 s; the official b-file contains 195 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000478), CC BY-SA 4.0.
