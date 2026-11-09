# A001221

> Number of distinct primes dividing n (also called omega(n)).
> — [OEIS A001221](https://oeis.org/A001221)

Offset 1: 0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 2, 2, 2, 2, 1, …

### Python 3 — 68 bytes

```python
P=n=1;L=[]
while[print(sum(n%p<1for p in L))]:P*=n*n;n+=1;L+=P%n*[n]
```

**How it works**

- `P` is ((n−1)!)², so by Wilson's theorem `P%n` is 1 when n is prime
  and 0 when it is not (n = 4 included: 3!² = 36 ≡ 0 mod 4).
- `L+=P%n*[n]` appends n exactly when it is prime, so `L` always holds the
  primes up to n, and ω(n) is the number of them that divide n.
- n = 1 sees an empty list and prints 0.

**Notes**

- The sum over all primes up to n makes a term cost about n/ln n steps;
  about 37000 terms in 30 s here. The b-file has 100000 terms; the bar is
  30000 in 60 s.
- [A001222](../A001222/) counts the prime factors with multiplicity.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001221), CC BY-SA 4.0.
