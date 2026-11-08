# A001074

> Numbers m such that Sum_{k=0..m-1} exp(2*Pi*i*k^3/m) != 0.
> — [OEIS A001074](https://oeis.org/A001074)

Offset 1: 1, 4, 7, 8, 9, 13, 19, 25, 27, 28, 31, 32, 36, 37, 43, 49, 52, 56, 61, 63, …

### Python 3 — 107 bytes

```python
m=1
while 1:
 n=m;d=b=1
 while~-n:
  d+=1;e=0
  while n%d<1:n//=d;e+=1
  b+=e%3==1!=d%3
 b<2==print(m);m+=1
```

**How it works**

Write G(a, q) = Σ_{k mod q} e(ak³/q), with e(x) = exp(2πix); the
sequence lists the m with G(1, m) ≠ 0. The program uses this criterion:

> G(1, m) ≠ 0 exactly when no prime p ≢ 1 (mod 3) divides m to a power
> e ≡ 1 (mod 3) (that is, with pᵉ ∥ m).

Proof sketch (a is always a unit):

- **Coprime moduli.** For m = m₁m₂ with gcd(m₁, m₂) = 1, write
  k = u·m₂ + v·m₁; the cross terms of k³ vanish mod m, so
  G(a, m) = G(am₂², m₁)·G(am₁², m₂), and G(1, m) is a product of
  prime-power sums with unit coefficients.
- **Lifting.** For e ≥ 3, splitting k by its residue mod pᵉ⁻¹ (p ≠ 3) or
  mod 3ᵉ⁻² (p = 3) and summing the linear phase over the rest kills every
  k not divisible by p, which gives G(a, pᵉ) = p²·G(a, pᵉ⁻³). Also
  G(a, p²) = p for p ≠ 3, and G(a, 9) = 3(1 + 2cos(2πa/9)) ≠ 0.
- **Primes.** If p ≢ 1 (mod 3) (p = 2, 3 or p ≡ 2), k ↦ k³ permutes Z/p,
  so G(a, p) = Σ e(ak/p) = 0. If p ≡ 1 (mod 3), Gauss showed the three
  values 1 + 3η of G(a, p) are the roots of y³ − 3py − pc with
  4p = c² + 27d², and none of them is 0.

So G(a, pᵉ) = 0 only for e ≡ 1 (mod 3) and p ≢ 1 (mod 3), and the
product vanishes exactly when one factor does. The rule matches all 1000
terms of the b-file.

The program factors each m by trial division: n is divided by
d = 2, 3, … as long as d | n, with e counting the divisions. Only primes
ever divide n there (the prime factors of a composite d are already
gone), and `b+=e%3==1!=d%3` is the chain e mod 3 = 1 and 1 ≠ d mod 3: a
bad prime. b starts at 1, so `b<2==print(m)` prints m when no bad prime
was found (the chain stops before print when b ≥ 2, and `2==None` is just
False). `while~-n` is `while n>1` for n ≥ 1.

**Notes**

- Exact integer arithmetic; correctness rests on the theorem above (the
  multiplicativity, the lifting identity and Gauss's cubic for the
  periods), not on floating-point sums.
- The whole b-file (1000 terms, up to 4993) prints in about 1.5 s and is
  the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001074), CC BY-SA 4.0.
