# A000459

> Number of multiset permutations of {1, 1, 2, 2, ..., n, n} with no fixed points.
> — [OEIS A000459](https://oeis.org/A000459)

Offset 0: 1, 0, 1, 10, 297, 13756, 925705, 85394646, 10351036465, 1596005408152, …

### Python 3 — 66 bytes

```python
a=b=1;n=0
while[print(b)]:n+=1;a,b=b,n*((2*n-1)*b+2*(n-1)*a)-2*n+1
```

**How it works**

Use the OEIS recurrence a(n)=n(2n-1)a(n-1)+2n(n-1)a(n-2)-(2n-1),
with a(0)=1 and a(1)=0. The state stores consecutive values.
The arbitrary preceding seed is multiplied by zero at n=1,
so a=b=1 generates the correct first update and then every term.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 101 terms in 60 s; the official b-file contains 101 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000459), CC BY-SA 4.0.
