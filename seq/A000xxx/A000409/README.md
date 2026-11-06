# A000409

> Singular n X n (0,1)-matrices: the number of n X n (0,1)-matrices having distinct, nonzero ordered rows, but having at least two equal columns or at least one zero column.
> — [OEIS A000409](https://oeis.org/A000409)

Offset 2: 0, 6, 350, 43260, 14591171, 14657461469, 46173502811223, 474928141312623525, 16489412944755088235117, 1985178211854071817861662307, …

### Python 3 — 147 bytes

```python
from math import*
s=[0,2,-3,1];n=2
while[print(-sum(s[k+1]*comb(2**k-1,n)for k in range(n)))]:
 n+=1;s=[0]+[s[k-1]-n*s[k]for k in range(1,n+1)]+[1]
```

**How it works**

The OEIS gives a(n) = -sum(s(n+1,k+1)*C(2^k-1,n), k=0..n-1),
where s is the signed Stirling number of the first kind. The state
`s` stores coefficients of x(x-1)...(x-n), initially x(x-1)(x-2).
Multiplying by x-(n+1) after each output updates those coefficients.
All binomial arguments are nonnegative; math.comb returns zero when
there are fewer than n available rows. This counts the column
degeneracies in the sequence definition, rather than all singular matrices.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 14 terms in 60 s; the official b-file contains 14 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000409), CC BY-SA 4.0.
