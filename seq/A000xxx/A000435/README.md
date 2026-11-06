# A000435

> Normalized total height of all nodes in all rooted trees with n labeled nodes.
> — [OEIS A000435](https://oeis.org/A000435)

Offset 1: 0, 1, 8, 78, 944, 13800, 237432, 4708144, 105822432, 2660215680, …

### Python 3 — 75 bytes

```python
n=1
while 1:
 a=0;f=1
 for k in range(n-1,0,-1):f*=k;a=a*n+f
 print(a);n+=1
```

**How it works**

The OEIS gives a(n)=(n-1)!*sum(n^k/k!,k=0..n-2).
Evaluate it by Horner's rule, as in Luschny's integer algorithm
on that page: while k descends from n-1 to 1, f becomes
(n-1)!/(k-1)! and a becomes n*a+f. For n=1 the sum is empty
and the program prints 0. No rational intermediate values are needed.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1000 terms in 60 s; the official b-file contains 1000 terms.
- The downloaded OEIS b-file omits leading digits at indices 841, 846, 857, 858, 859, 929, 936, 938, 939, 940, 941. This new reference restores those digits. Each affected term was independently checked against the factorial sum as well as the integer Horner algorithm. All other source values are unchanged.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000435), CC BY-SA 4.0.
