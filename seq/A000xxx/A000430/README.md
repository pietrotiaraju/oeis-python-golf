# A000430

> Primes and squares of primes.
> — [OEIS A000430](https://oeis.org/A000430)

Offset 1: 2, 3, 4, 5, 7, 9, 11, 13, 17, 19, …

### Python 3 — 74 bytes

```python
s=set();n=p=1
while 1:
 p*=n*n;n+=1
 if p%n:s|={n,n*n}
 if n in s:print(n)
```

**How it works**

At the test for n, p=((n-1)!)². Wilson's theorem implies p mod n
is nonzero exactly for primes n>=2: every composite n>=4 divides
((n-1)!)² (including n=4). On discovering a prime, mark it and
its square. The increasing counter prints exactly those marked values.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1000 terms in 60 s; the official b-file contains 1000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000430), CC BY-SA 4.0.
