# A000449

> Rencontres numbers: number of permutations of [n] with exactly 3 fixed points.
> — [OEIS A000449](https://oeis.org/A000449)

Offset 3: 1, 0, 10, 40, 315, 2464, 22260, 222480, 2447445, 29369120, …

### Python 3 — 59 bytes

```python
a=1;n=3
while[print(a)]:n+=1;a=n*a-(-1)**n*n*(n-1)*(n-2)//6
```

**How it works**

Rencontres numbers with exactly three fixed points are
C(n,3)*D(n-3), where D is the derangement number.
Using D(m)=m*D(m-1)+(-1)^m gives
a(n)=n*a(n-1)-(-1)^n*C(n,3), with a(3)=1.
The product divided by 6 is exactly C(n,3).

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 98 terms in 60 s; the official b-file contains 98 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000449), CC BY-SA 4.0.
