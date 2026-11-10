# A001480

> Let p = A007645(n) be the n-th generalized cuban prime and write p =  x^2 + 3*y^2; a(n) = y.
> — [OEIS A001480](https://oeis.org/A001480)

Offset 1: 1, 1, 2, 1, 3, 2, 3, 2, 1, 4, 5, 4, 1, 6, 3, 5, 7, 6, 7, 2, 8, …

### Python 3 — 87 bytes

```python
P=n=1;S={0}
while 1:[print(y)for y in range(P%n*n)if n-3*y*y in S];P*=n*n;S|={n*n};n+=1
```

**How it works**

- **Which primes, which y.** The generalized cuban primes (A007645) are 3
  and the primes p ≡ 1 (mod 3). By Fermat and Euler, a prime is of the form
  x² + 3y² exactly when it is one of these, and then x and y are unique up
  to sign (Euler; for 3 it is 0² + 3·1²). So
  a(n) is the unique y ≥ 0, as in the data (y ≥ 1 always). Other primes
  never qualify: x² + 3y² ≡ x² ≢ 2 (mod 3), and 2 is not of the form.
- **Wilson's theorem.** `P` is ((n − 1)!)², so `P%n` is 1 when n is prime
  and 0 when it is not (n = 1, 4 and every larger composite), and
  `range(P%n*n)` is range(n) at primes and empty otherwise.
- **The search.** `S` holds k² for every k < n. For a prime n the
  comprehension prints each y < n with n − 3y² in `S`, that is
  n = k² + 3y²; by uniqueness that prints exactly one y for n = 3 or
  n ≡ 1 (mod 3), and nothing for the others. Primes come in increasing
  order, so the y's come in the order of A007645.

**Notes**

- Exact integers throughout; the cost is about n set lookups per prime and
  the growing factorial. The 1000-term b-file (primes up to about 17400)
  prints in about 6 s on a slow PC; the bar is the whole b-file in 60 s.
- [A001479](../A001479/) is the same program printing x, with 3k² in `S`.
  Checking `isqrt(abs(m:=n-3*y*y))**2==m` with `from math import*`
  instead of the set is 106 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001480), CC BY-SA 4.0.
