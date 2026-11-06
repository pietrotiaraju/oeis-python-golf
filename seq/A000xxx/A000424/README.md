# A000424

> Differences of reciprocals of unity.
> — [OEIS A000424](https://oeis.org/A000424)

Offset 1: 7, 85, 1660, 48076, 1942416, 104587344, 7245893376, 628308907776, 66687811660800, 8506654697548800, …

### Python 3 — 86 bytes

```python
a=0;b=1;c=7;n=1
while[print(c)]:n+=1;a,b,c=b,c,(3*n*n+3*n+1)*c-3*n**4*b+((n-1)*n)**3*a
```

**How it works**

Use the third-order integer recurrence stated by the OEIS:
a(n)=(3n²+3n+1)a(n-1)-3n⁴a(n-2)+(n-1)³n³a(n-3).
The seeds a(-1)=0, a(0)=1, a(1)=7 reproduce a(2)=85
and a(3)=1660, after which the recurrence determines the sequence.
The tuple update preserves the previous three values.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 16 terms in 60 s; the official b-file contains 16 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000424), CC BY-SA 4.0.
