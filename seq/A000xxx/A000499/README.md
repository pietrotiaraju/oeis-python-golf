# A000499

> a(n) = Sum_{k=1..n-1} k^3*sigma(k)*sigma(n-k).
> — [OEIS A000499](https://oeis.org/A000499)

Offset 1: 0, 1, 27, 184, 875, 2700, 7546, 17600, 35721, 72750, …

### Python 3 — 82 bytes

```python
n=1
while 1:print(n**3*sum(k*(2*k*k+1-3*n)for k in range(1,n+1)if n%k<1)//24);n+=1
```

**How it works**

The OEIS divisor-sum identity is
a(n)=n³*((1-3n)*sigma_1(n)+2*sigma_3(n))/24.
Combine the divisor sums into one pass over divisors k of n.
The polynomial numerator is divisible by 24 for every positive n.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000499), CC BY-SA 4.0.
