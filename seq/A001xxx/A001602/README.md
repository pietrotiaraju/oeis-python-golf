# A001602

> Fibonacci entry points: a(n) = smallest m > 0 such that the n-th prime divides Fibonacci(m).
> — [OEIS A001602](https://oeis.org/A001602)

Offset 1: 3, 4, 5, 8, 10, 7, 9, 18, 24, 14, 30, 19, 20, 44, 16, 27, 58, 15, 68, 70, …

### Python 3 — 81 bytes

```python
P=k=1
while 1:
 P*=k*k;k+=1;a=b=m=P%k
 while a:a,b=b,(a+b)%k;m+=1
 m and print(m)
```

Sibling: the entry points of all n, [A001177](../A001177/).

**How it works**

- Wilson's theorem: `P` is ((k − 1)!)², so P mod k is 1 when k is prime
  ((k − 1)! ≡ −1) and 0 when k is composite (k divides (k − 1)! for
  composite k > 4, and 36 ≡ 0 (mod 4)).
- `a=b=m=P%k`: for a prime k this is (a, b) = (F(1), F(2)) = (1, 1) with
  m = 1, and `a,b=b,(a+b)%k;m+=1` walks a = F(m) mod k until it is 0. For a
  composite k, a = 0 skips the walk and m = 0 prints nothing.
- The walk always stops: every prime p divides F(p − 1), F(p + 1) or
  F(p) (p = 5), so a(n) ≤ p + 1.

**Notes**

- Exact for every n.
- The walk takes a(n) steps, about 4·10⁷ in all for the first 4000 primes:
  a(4000) arrives after about 24 s on the PC it was written on. The b-file
  has 10000 terms; the bar is 4000 in 60 s.
- The entry point of p divides p − (5/p), so factoring p ± 1 and testing
  its divisors with fast doubling would be far faster, but longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001602), CC BY-SA 4.0.
