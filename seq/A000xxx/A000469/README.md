# A000469

> 1 together with products of 2 or more distinct primes.
> — [OEIS A000469](https://oeis.org/A000469)

Offset 1: 1, 6, 10, 14, 15, 21, 22, 26, 30, 33, …

### Python 3 — 129 bytes

```python
from math import*
n=1
while 1:
 r=range(2,isqrt(n)+1)
 if all(n%(k*k)for k in r)and(n==1 or any(n%k<1 for k in r)):print(n)
 n+=1
```

**How it works**

A product of distinct primes is exactly a squarefree integer.
The first condition excludes every square divisor greater than 1.
The second accepts 1 and composite integers; a composite squarefree
integer has at least two prime factors. It suffices to test divisors
through the exact integer square root of n.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000469), CC BY-SA 4.0.
