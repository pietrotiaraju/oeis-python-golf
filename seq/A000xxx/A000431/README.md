# A000431

> Expansion of 2*x^3/((1-2*x)^2*(1-4*x)).
> — [OEIS A000431](https://oeis.org/A000431)

Offset 0: 0, 0, 0, 2, 16, 88, 416, 1824, 7680, 31616, …

### Python 3 — 42 bytes

```python
n=0
while 1:print(2**n*(2**n-2*n)//8);n+=1
```

**How it works**

The OEIS gives a(n) = (4^n - n*2^(n+1))/8 for n >= 1.
Factoring out 2^n gives the printed expression. At n=0 its integer
quotient is 0, supplying the separately specified initial coefficient.
For every n >= 1 the division is exact.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 201 terms in 60 s; the official b-file contains 201 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000431), CC BY-SA 4.0.
