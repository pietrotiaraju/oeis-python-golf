# A000477

> a(n) = Sum_{k=1..n-1} k^2*sigma(k)*sigma(n-k).
> — [OEIS A000477](https://oeis.org/A000477)

Offset 1: 0, 1, 15, 76, 275, 720, 1666, 3440, 6129, 11250, …

### Python 3 — 82 bytes

```python
n=1
while 1:print(n**2*sum(k*(3*k*k+1-4*n)for k in range(1,n+1)if n%k<1)//24);n+=1
```

**How it works**

The divisor-sum identity listed by the OEIS is
a(n)=n^2*((1-4n)*sigma_1(n)+3*sigma_3(n))/24.
Combine the two divisor sums into one sum over k dividing n,
then perform the exact division by 24. The loop starts at n=1.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000477), CC BY-SA 4.0.
