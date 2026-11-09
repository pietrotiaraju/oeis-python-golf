# A001276

> Smallest k such that the product of q/(q-1) over the primes from prime(n) to prime(n+k-1) is greater than 2.
> — [OEIS A001276](https://oeis.org/A001276)

Offset 1: 2, 3, 7, 15, 27, 41, 62, 85, 115, 150, 186, 229, 274, 323, 380, …

a(n) is the number of primes in the product of [A001275](../A001275/):
the least number of distinct prime factors of an abundant number whose
smallest prime factor is prime(n).

### Python 3 — 141 bytes

```python
P=[];N=m=r=1;D=2
while 1:
 m+=1;r+=r*r<=m
 if all(m%d for d in range(2,r)):P+=m,;N*=m;D*=m-1
 while N>D:print(len(P));N//=P[0];D//=P.pop(0)-1
```

**How it works**

- The program of [A001275](../A001275/) with `print(len(P))` in place of
  `print(m)`: it slides a window of consecutive primes, kept as exact
  integers. `P` lists the primes from prime(n) up to the last prime found,
  `N` is their product and `D` is twice the product of the q − 1, so the
  product of q/(q − 1) over the window exceeds 2 exactly when `N>D`.
- `m` runs over 2, 3, 4, … and is prime when no d with 2 ≤ d < r divides
  it, where `r` keeps r² > m (it grows to r + 1 exactly when m reaches r²)
  and stays below m from m = 3 on. Each prime m joins the window.
- While the window exceeds 2, m is the smallest prime that makes the
  product from prime(n) exceed 2, so the window holds a(n) primes:
  `len(P)` is printed, prime(n) leaves the window
  (`N//=P[0];D//=P.pop(0)-1`, both exact) and the test is repeated for
  n + 1 with the same m.
- Nothing is missed: every window from prime(n) to a prime q before the
  end found for n − 1 has a product below the window from prime(n − 1)
  to q, which is at most 2, and a single factor q/(q − 1) is at most 2, so
  the window never empties. For n = 1, 2/1 = 2 is not greater than 2 and
  2/1·3/2 = 3 is, so a(1) = 2.

**Notes**

- `N` is about the product of all primes up to m, about 1.44·m bits, so
  each new prime costs time proportional to m and the run is roughly
  quadratic: a(175) = 88723 arrives after about 13 reference seconds.
- Counting with a separate variable instead of `len(P)` is no shorter.
- The b-file has 650 terms (up to 1504704); the bar is 175 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 141 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001276), CC BY-SA 4.0.
