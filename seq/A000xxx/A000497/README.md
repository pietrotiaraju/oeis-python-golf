# A000497

> S2(j,2j+2) where S2(n,k) is a 2-associated Stirling number of the second kind.
> — [OEIS A000497](https://oeis.org/A000497)

Offset 1: 1, 25, 490, 9450, 190575, 4099095, 94594500, 2343240900, 62199262125, 1764494857125, …

### Python 3 — 64 bytes

```python
a=n=1
while[print(a)]:n+=1;a=a*(n+1)*(2*n+1)**2//((2*n-1)*(n-1))
```

**How it works**

Use the OEIS first-order recurrence
(2n-1)(n-1)a(n)=(n+1)(2n+1)²a(n-1), starting at a(1)=1.
The counter is increased before the update, so n is at least 2
and the denominator is nonzero. The recurrence guarantees exact division.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 100 terms in 60 s; the official b-file contains 100 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000497), CC BY-SA 4.0.
