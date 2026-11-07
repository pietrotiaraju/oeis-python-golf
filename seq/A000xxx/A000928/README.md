# A000928

> Irregular primes: primes p such that at least one of the numerators of the Bernoulli numbers B_2, B_4, ..., B_{p-3} (A000367) is divisible by p.
> — [OEIS A000928](https://oeis.org/A000928)

Offset 1: 37, 59, 67, 101, 103, 131, 149, 157, 233, 257, 263, 271, 283, 293, 307, 311, 347, 353, 379, 389, …

### Python 3 — 99 bytes

```python
P=p=1
while[0in(sum(a**k for a in range(p))%p**2for k in range(2,P%p*p,2))and print(p)]:P*=p*p;p+=1
```

**How it works**

- For a prime p and an even k with 2 ≤ k ≤ p−3, Faulhaber's formula
  Σ_{a=0}^{p−1} aᵏ = (1/(k+1)) Σ_j C(k+1, j) B_j p^(k+1−j) gives
  Σ aᵏ ≡ p·B_k (mod p²): the j = k term is p·B_k, the j = k−1 term is
  −p²/2 or 0, and the rest carry p³ against at most one p in the
  denominator of B_j (von Staudt–Clausen), with coefficients whose
  denominators k+1−j < p. B_k itself has no p in its denominator since
  p−1 ∤ k. So p divides the numerator of B_k exactly when p² divides
  Σ_{a<p} aᵏ, and p is irregular when that happens for some such k.
- k runs over `range(2,p,2)`, which also takes k = p−1; that one never
  fires, since Σ a^(p−1) ≡ p−1 (mod p) by Fermat.
- `P` is ((p−1)!)², so `P%p` is 1 for a prime p and 0 otherwise (Wilson's
  theorem): `range(2,P%p*p,2)` is empty for composites, so they cost
  nothing and need no separate test.
- `0in(...)` stops at the first k that works; inside `while[...]` the
  `and print(p)` prints the irregular primes.

**Notes**

- Exact integer arithmetic. `a**k` builds big powers and is slower than
  `pow(a,k,p*p)` (7 bytes more, about 85 terms in 60 s); the program gives
  58 terms in 60 s, the cost per prime growing like p² powers.
- The b-file has 10000 terms; the bar is 45 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 99 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000928), CC BY-SA 4.0.
