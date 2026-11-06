# A000458

> a(0) = a(1) = 1; thereafter a(n) = sigma(a(n-1)) + sigma(a(n-2)).
> — [OEIS A000458](https://oeis.org/A000458)

Offset 0: 1, 1, 2, 4, 10, 25, 49, 88, 237, 500, …

### Python 3 — 146 bytes

```python
def s(n):
 p=2;t=1
 while p*p<=n:
  a=1
  while n%p<1:n//=p;a=a*p+1
  t*=a;p+=1
 return t*(n+1)if n>1 else t
a=b=1
while[print(a)]:a,b=b,s(a)+s(b)
```

**How it works**

Trial division factors n. For each prime power p^e, the nested
update a=a*p+1 builds 1+p+...+p^e; multiplying these factors
gives sigma(n). If a prime factor remains after p²>n, its
contribution is n+1. Start with a(0)=a(1)=1 and simultaneously
advance the two states using the defining sigma recurrence.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 40 terms in 10 s; the official b-file contains 101 terms.
- Exact trial division prints the first 40 terms quickly; later large terms need substantially more time. The bar is 40 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 146 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000458), CC BY-SA 4.0.
