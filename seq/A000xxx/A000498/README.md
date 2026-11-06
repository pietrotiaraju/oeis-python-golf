# A000498

> Eulerian numbers (Euler's triangle: column k=4 of A008292, column k=3 of A173018).
> — [OEIS A000498](https://oeis.org/A000498)

Offset 4: 1, 26, 302, 2416, 15619, 88234, 455192, 2203488, 10187685, 45533450, …

### Python 3 — 73 bytes

```python
n=4
while 1:print(4**n-(n+1)*3**n+n*(n+1)*2**(n-1)-(n-1)*n*(n+1)//6);n+=1
```

**How it works**

Eulerian inclusion-exclusion for exactly three descents gives
4^n-C(n+1,1)*3^n+C(n+1,2)*2^n-C(n+1,3).
Expand the binomial coefficients and evaluate in integers,
starting at the minimum size n=4.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 197 terms in 60 s; the official b-file contains 197 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000498), CC BY-SA 4.0.
