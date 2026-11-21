# A002147

> Largest prime == 7 (mod 8) with class number 2n+1.
> — [OEIS A002147](https://oeis.org/A002147)

Offset 0: 7, 31, 127, 487, 1423, 1303, 2143, 2647, 4447, 5527, 5647, 6703, 5503, 11383, …

### Python 3 — 295 bytes

```python
B=2383747;C=[0]*B;n=0
for a in range(2,999):
 for b in range(1,a,2):C[s::t]=map((1).__add__,C[(s:=4*a*-~a-b*b)::(t:=4*a<<a%2)])
while 1:print(next(p for p in range(B-4|n//50<<180*n,0,-8)if(p<B and C[p]or p//4-sum(pow(k,p//2,p)>1for k in range(p//2+1)))==n and all(p%d for d in range(2,p))));n+=1
```

**How it works**

- **Which sequence.** a(n) is the largest prime p ≡ 7 (mod 8) with
  h(−p) = 2n + 1, h(−p) the class number of Q(√−p). A largest one exists
  because h(−p) → ∞; the program needs an explicit bound for it, which
  two theorems give (below).
- **Class number as a count.** For a prime p ≡ 3 (mod 4), p > 3, the
  reduced forms ax² + bxy + cy² of discriminant −p (|b| ≤ a ≤ c, b ≥ 0
  when |b| = a or a = c) are the principal form (1, 1, (p + 1)/4) and
  pairs (a, ±b, c) with b odd and 1 ≤ b < a < c (a = c is impossible and
  |b| = a forces a = 1, as on [A002143](../A002143/)). So
  h(−p) = 2T(p) + 1 with T(p) the number of triples 1 ≤ b < a < c, b odd,
  4ac − b² = p, and a(n) is the largest prime p ≡ 7 (mod 8) with
  T(p) = n.
- **The table.** `C[D]` counts the triples with D = 4ac − b² < B. For
  each a from 2 and odd b < a, the values for c = a + 1, a + 2, … run
  from 4a(a + 1) − b² (`4*a*-~a-b*b`) in steps of 4a, and
  `C[s::t]=map((1).__add__,C[s::t])` adds 1 along that slice (the right
  side is evaluated first, so its walruses set s and t). D ≡ 7 (mod 8)
  means 8 | 4ac, that is ac even: every c when a is even, and only even c
  (from a + 1, steps of 8a, `4*a<<a%2`) when a is odd. a stops at 998,
  since D ≥ 3a² + 6a − 1 > B once a ≥ 891. So `C[D]` = T(D) for every
  D ≡ 7 (mod 8) below B.
- **The bound (n ≤ 49).** Watkins determined every imaginary quadratic
  field with class number at most 100; the largest |discriminant| among
  them is 2383747, with class number 98 (M. Watkins, *Class numbers of
  imaginary quadratic fields*, Math. Comp. 73 (2004), 907–938). So every
  prime p with h(−p) = 2n + 1 ≤ 99 lies below B = 2383747, and the scan
  down from B − 4 through p ≡ 7 (mod 8) meets a(n) first among the primes
  with T(p) = n. Trial division by every d < p tests primality.
- **The bound (n ≥ 50).** Oesterlé's effective form of the
  Goldfeld–Gross–Zagier theorem gives, for a fundamental discriminant d
  prime to 5077, h(d) > (1/55)·log|d|·∏(1 − ⌊2√q⌋/(q + 1)) over the primes
  q | d with q ≠ |d| (J. Oesterlé, *Le problème de Gauss sur le nombre de
  classes*, Enseign. Math. 34 (1988), 43–67; as stated by D. Goldfeld,
  *The Gauss class number problem for imaginary quadratic fields*). For
  d = −p the product is empty, so p < e^(55h). For n ≥ 50 the scan starts
  at 2^(180n) + B − 4 (`B-4|n//50<<180*n`, ≡ 7 (mod 8)), which exceeds
  e^(55(2n+1)) since 2^180 > e^124.
- **Past the table.** `p<B and C[p]or …` reads the table below B and
  falls back on Dirichlet's class number formula for p ≥ B: for a prime
  p ≡ 7 (mod 8), h(−p) = Σ (k/p) over 1 ≤ k ≤ (p − 1)/2 (as (2/p) = 1).
  With Euler's criterion (k/p) ≡ k^((p−1)/2), the number N of
  non-residues k among them (`pow(k,p//2,p)>1`; k = 0 gives 0) gives
  h = (p − 1)/2 − 2N, so T(p) = (p − 3)/4 − N = ⌊p/4⌋ − N. Below B the
  fallback also runs where `C[p]` is 0, which for D ≡ 7 (mod 8) happens
  only at 7 and 15 ((2, 1, (D + 1)/8) is a triple for D > 15); it gives
  T(7) = 0, as the table does.

**Notes**

- So the program is correct for every n, resting on these two theorems;
  in practice a(50) would need class numbers of 9000-bit primes, and the
  program stops making progress there (with little memory). The b-file
  goes on to n = 2246, but its terms past n = 49 are conjectural (the
  entry says so).
- Exact integer arithmetic throughout. The table is a list of B counters
  filled by about 120 million increments; here (about 1.9 times slower
  than the reference) a(0) comes after 17 s and a(49) after 20 s. The bar
  is the 50 terms n = 0…49 that Watkins' theorem covers, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-21 | Python 3 | 295 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002147), CC BY-SA 4.0.
