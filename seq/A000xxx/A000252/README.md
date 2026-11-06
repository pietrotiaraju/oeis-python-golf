# A000252

> Number of invertible 2 X 2 matrices mod n.
> — [OEIS A000252](https://oeis.org/A000252)

Offset 1: 1, 6, 48, 96, 480, 288, 2016, 1536, 3888, 2880, 13200, 4608, 26208, 12096, 23040, 24576, 78336, 23328, 123120, 46080, …

### Python 3 — 95 bytes

```python
f=lambda n,k:n**k-sum(f(d,k)for d in range(1,n)if n%d<1)
n=1
while[print(n*f(n,1)*f(n,2))]:n+=1
```

**How it works**

- a(n) = n·φ(n)·J₂(n). A matrix (a b; c d) mod n is invertible exactly
  when its determinant ad − bc is a unit. Its first row must have
  gcd(a, b, n) = 1, and there are J₂(n) such rows (Jordan's totient). For
  a fixed such row, (c, d) ↦ ad − bc maps Z_n² onto Z_n, n to one, as in
  [A000056](../A000056/). So each of the φ(n) units is hit by n rows
  (c, d), which gives J₂(n)·n·φ(n).
- `f(n,k)` is Jordan's totient J_k(n). Each of the n^k vectors mod n has
  gcd(entries, n) = n/d for exactly one divisor d of n, and J_k(d) vectors
  have each such gcd, so n^k = Σ_{d|n} J_k(d). `f` subtracts the proper
  divisors' terms from n^k. With k = 1 it is φ(n) and with k = 2 it is J₂(n),
  the same recursion as A000056 with an exponent added.
- `while[print(…)]:n+=1` prints in the loop condition: `[None]` is a
  non-empty list, so it is true.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  recursion is only as deep as a chain of divisors, at most log₂ n + 1
  calls.
- The whole b-file (1000 terms) prints in about 0.5 s, and about 11 800
  terms fit in 60 s. The bar is the whole b-file in 60 s.
- The Euler product n⁴·∏(1 − 1/p)(1 − 1/p²) over primes p | n, with
  Wilson's theorem as the prime test, is also 95 bytes:
  `n=a=1` / `while[print(a)]:` / ` n+=1;a=n**4;P=k=1` /
  ` while k<n:P*=k*k;k+=1;a-=a*(P%k>n%k)*(k*k+k-1)//k**3`.
  P = ((k−1)!)² is 1 mod k for prime k and 0 for composite k (also k = 4),
  so `P%k>n%k` is true exactly for the primes dividing n, and each step
  multiplies a by (k − 1)(k² − 1)/k³ = 1 − (k² + k − 1)/k³. a still has a
  factor k⁴ when the step runs, so the division is exact.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000252), CC BY-SA 4.0.
