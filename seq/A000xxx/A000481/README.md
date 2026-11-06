# A000481

> Stirling numbers of the second kind, S(n,5).
> — [OEIS A000481](https://oeis.org/A000481)

Offset 5: 1, 15, 140, 1050, 6951, 42525, 246730, 1379400, 7508501, 40075035, …

### Python 3 — 57 bytes

```python
a=b=c=d=1
while[print(a)]:d=2*d+1;c=3*c+d;b=4*b+c;a=5*a+b
```

**How it works**

The generating function after removing x⁵ is
1/((1-x)(1-2x)(1-3x)(1-4x)(1-5x)).
Successively adjoining the factors gives h_j(m)=j*h_j(m-1)+h_(j-1)(m).
All h_j(0) equal 1. Update from j=2 through 5 so that the
right-hand term already belongs to the new row; a is h_5(m)=S(m+5,5).

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 196 terms in 60 s; the official b-file contains 196 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000481), CC BY-SA 4.0.
