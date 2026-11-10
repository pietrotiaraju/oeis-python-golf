# A001479

> Let p = A007645(n) be the n-th generalized cuban prime and write p =  x^2 + 3*y^2; a(n) = x.
> — [OEIS A001479](https://oeis.org/A001479)

Offset 1: 0, 2, 1, 4, 2, 5, 4, 7, 8, 5, 2, 7, 10, 1, 10, 8, 2, 7, 4, 13, 1, …

### Python 3 — 87 bytes

```python
P=n=1;S={0}
while 1:[print(x)for x in range(P%n*n)if n-x*x in S];P*=n*n;S|={3*n*n};n+=1
```

**How it works**

- **Which primes, which x.** The generalized cuban primes (A007645) are 3
  and the primes p ≡ 1 (mod 3). By Fermat and Euler, a prime is of the form
  x² + 3y² exactly when it is one of these, and then x and y are unique up
  to sign (Euler; for 3 it is 0² + 3·1²). So
  a(n) is the unique x ≥ 0, as in the data. Other primes never qualify:
  x² + 3y² ≡ x² ≢ 2 (mod 3), and 2 is not of the form.
- **Wilson's theorem.** `P` is ((n − 1)!)², so `P%n` is 1 when n is prime
  and 0 when it is not (n = 1, 4 and every larger composite), and
  `range(P%n*n)` is range(n) at primes and empty otherwise.
- **The search.** `S` holds 3k² for every k < n. For a prime n the
  comprehension prints each x < n with n − x² in `S`, that is
  n = x² + 3k²; by uniqueness that prints exactly one x for n = 3 or
  n ≡ 1 (mod 3), and nothing for the others. Primes come in increasing
  order, so the x's come in the order of A007645.

**Notes**

- Exact integers throughout; the cost is about n set lookups per prime and
  the growing factorial. The 1000-term b-file (primes up to about 17400)
  prints in about 5 s on a slow PC; the bar is the whole b-file in 60 s.
- [A001480](../A001480/) is the same program printing y, with the
  squares in `S`. Checking `isqrt(abs(m:=n-x*x)//3)**2*3==m` with
  `from math import*` instead of the set is 109 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001479), CC BY-SA 4.0.
