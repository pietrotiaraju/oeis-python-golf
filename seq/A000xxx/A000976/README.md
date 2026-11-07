# A000976

> Period of 1/n! in base 10.
> — [OEIS A000976](https://oeis.org/A000976)

Offset 1: 0, 0, 1, 1, 1, 1, 6, 6, 18, 18, 18, 54, 54, 378, 1134, 1134, 9072, 81648, 81648, 81648, …

### Python 3 — 78 bytes

```python
f=a=n=1
while[print(a*(f>2))]:
 n+=1;f*=n;b=a
 while~-pow(10,a,f)*10**n%f:a+=b
```

**How it works**

- 1/N has a purely periodic part whose period is the multiplicative order
  of 10 modulo N′, N with all factors 2 and 5 removed (and the period is 0
  when N′ = 1). For N = n! = `f`, both v₂(n!) and v₅(n!) are less than n,
  so 10ᵃ ≡ 1 (mod N′) exactly when f divides 10ⁿ·(10ᵃ − 1); the loop
  condition `~-pow(10,a,f)*10**n%f` tests that without ever computing N′
  (`~-x` is x − 1).
- N′ for n! is N′ for (n−1)! times the 2-and-5-free part of n, so the
  order for n is a multiple of the order `b` for n−1: the search steps
  through multiples, `a+=b`, and needs as many steps as the ratio of the
  two orders.
- For n = 1, 2 the modulus is 1 or 2, the inner loop never runs, `a`
  stays 1 and `a*(f>2)` prints 0. For n ≥ 3, f ≥ 6 and the order is a
  real period.
- The term is printed in the `while[print(...)]:` condition, before the
  next factorial is formed.

**Notes**

- Exact integer arithmetic (three-argument `pow` on numbers of up to a few
  thousand bits).
- The 200-term b-file takes about 12 s; the bar is all 200 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000976), CC BY-SA 4.0.
