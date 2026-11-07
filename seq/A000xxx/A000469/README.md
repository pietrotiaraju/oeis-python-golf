# A000469

> 1 together with products of 2 or more distinct primes.
> — [OEIS A000469](https://oeis.org/A000469)

Offset 1: 1, 6, 10, 14, 15, 21, 22, 26, 30, 33, …

The squarefree numbers that are not prime.

### Python 3 — 54 bytes

```python
Q=n=1
while[Q%n or print(n)]:Q*=n**(pow(Q,n,n)>0);n+=1
```

**How it works**

- **The test.** Q is the product of the primes below n. Then n is in the
  sequence exactly when n divides Q. For n = 1 this holds. A prime n does
  not divide a product of smaller primes. A squarefree composite n is a
  product of distinct primes, each at most n/2, so each divides Q and so
  does n. If p² divides n, then n ∤ Q because p appears in Q only once.
- **Growing Q.** After the test, n is multiplied into Q when it is prime.
  The prime test needs no trial division: for n ≥ 2, n is prime exactly
  when Qⁿ mod n ≠ 0. If n is prime, Q is coprime to n. If n is composite,
  every prime factor p of n is below n and so divides Q, and the exponent
  of p in n is below n, so n divides Qⁿ. At n = 1, `pow(Q,1,1)` is 0 and Q
  stays 1.
- `pow(Q,n,n)>0` is `True` or `False`, so `n**(…)` is n or 1.
- `Q%n or print(n)` prints only when Q mod n = 0, and the one-element list
  around it keeps the `while` condition true (the [A000007](../A000007/)
  loop).

**Notes**

- Other versions that print the same terms: Wilson's theorem instead of the
  power test, `P=Q=n=1` / `while[Q%n or print(n)]:Q*=n**(P%n);P*=n*n;n+=1`
  with P = ((n−1)!)²: also 54 bytes, but about 3.5 times slower (40000
  terms in 60 s); the trial-division test with `isqrt`,
  `all(n%(k*k)for k in r)and(n==1 or any(n%k<1 for k in r))`: 128 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 138000 terms in 60 s here; the b-file's 10000 terms (up to 20203)
  take 0.7 s. The b-file has 10000 terms (up to a(10000)); the bar is the
  whole b-file in 60 s.
- [A000430](../A000430/) is the primes together with the squares of
  primes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |
| 2026-11-06 | Python 3 | 128 | use a shorter math import |
| 2026-11-07 | Python 3 | 54 | n divides the product of the smaller primes |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000469), CC BY-SA 4.0.
