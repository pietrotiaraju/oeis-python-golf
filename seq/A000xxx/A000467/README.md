# A000467

> Number of permutations of [n] in which the longest increasing run has length 6.
> — [OEIS A000467](https://oeis.org/A000467)

Offset 1: 0, 0, 0, 0, 0, 1, 12, 137, 1602, 19710, …

### Python 3 — 167 bytes

```python
from math import*
L=[[1],[1]];n=0
while 1:
 n+=1
 for q,a in enumerate(L,6):a+=[sum(comb(n,k)*((k%q==1)-(k%q<1))*a[-k]for k in range(1,n+1))]
 print(L[1][-1]-L[0][-1])
```

**How it works**

For a maximum increasing-run length r, the e.g.f. is the reciprocal
of sum(x^((r+1)j)/((r+1)j)! - x^((r+1)j+1)/((r+1)j+1)!), j >= 0.
This is the bounded-run cluster formula; see the Alekseyev reference
linked by the OEIS. Equating coefficients gives the binomial recurrence
used in the comprehension: add the terms with k congruent to 1 modulo
r+1 and subtract those with k congruent to 0. The lists track maximum
run lengths 5 and 6. Their difference counts maximum length exactly 6.
Both start with the empty-permutation count 1; printing starts at n=1.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 450 terms in 60 s; the official b-file contains 450 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 167 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000467), CC BY-SA 4.0.
