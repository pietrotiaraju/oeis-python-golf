# A000441

> a(n) = Sum_{k=1..n-1} k*sigma(k)*sigma(n-k).
> — [OEIS A000441](https://oeis.org/A000441)

Offset 1: 0, 1, 9, 34, 95, 210, 406, 740, 1161, 1920, …

### Python 3 — 82 bytes

```python
n=1
while 1:print(n**1*sum(k*(5*k*k+1-6*n)for k in range(1,n+1)if n%k<1)//24);n+=1
```

**How it works**

The divisor-sum identity listed by the OEIS is
a(n)=n^1*((1-6n)*sigma_1(n)+5*sigma_3(n))/24.
Combine the two divisor sums into one sum over k dividing n,
then perform the exact division by 24. The loop starts at n=1.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1000 terms in 60 s; the official b-file contains 1000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000441), CC BY-SA 4.0.
