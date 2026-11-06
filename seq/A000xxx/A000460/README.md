# A000460

> Eulerian numbers (Euler's triangle: column k=3 of A008292, column k=2 of A173018).
> — [OEIS A000460](https://oeis.org/A000460)

Offset 3: 1, 11, 66, 302, 1191, 4293, 14608, 47840, 152637, 478271, …

### Python 3 — 50 bytes

```python
n=3
while 1:print(3**n-(n+1)*2**n+n*(n+1)//2);n+=1
```

**How it works**

The Eulerian inclusion-exclusion formula for exactly two descents
is 3^n - C(n+1,1)*2^n + C(n+1,2).
The loop evaluates this integer expression starting at n=3.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 998 terms in 60 s; the official b-file contains 998 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000460), CC BY-SA 4.0.
