# A002149

> Largest prime p==3 (mod 8) such that Q(sqrt(-p)) has class number 2n+1.
> — [OEIS A002149](https://oeis.org/A002149)

Offset 0: 163, 907, 2683, 5923, 10627, 15667, 20563, 34483, 37123, 38707, 61483, …

### Python 3 — 300 bytes

```python
B=2383747;C=[0]*B;n=0
for a in range(3,999,2):
 for b in range(1,a,2):C[s::t]=map((1).__add__,C[(s:=4*a*a+8*a-b*b)::(t:=8*a)])
while 1:print(next(p for p in range(B-8|n//50<<180*n,0,-8)if(p<B and C[p]or(4*sum(pow(k,p//2,p)<2for k in range(p//2+1))-p-9)//12)==n and all(p%d for d in range(2,p))));n+=1
```

**How it works**

- **Which sequence.** a(n) is the largest prime p ≡ 3 (mod 8) with
  h(−p) = 2n + 1, h(−p) the class number of Q(√−p). A largest one exists
  because h(−p) → ∞; the program needs an explicit bound for it, which
  two theorems give (below).
- **Class number as a count.** For a prime p ≡ 3 (mod 4), p > 3, the
  reduced forms ax² + bxy + cy² of discriminant −p (|b| ≤ a ≤ c, b ≥ 0
  when |b| = a or a = c) are the principal form (1, 1, (p + 1)/4) and
  pairs (a, ±b, c) with b odd and 1 ≤ b < a < c (a = c is impossible and
  |b| = a forces a = 1, as on [A002143](../A002143/)). So
  h(−p) = 2T(p) + 1 with T(p) the number of triples 1 ≤ b < a < c, b odd,
  4ac − b² = p, and a(n) is the largest prime p ≡ 3 (mod 8), p > 3, with
  T(p) = n (h(−3) = 1 too, but 163 > 3).
- **The table.** `C[D]` counts the triples with D = 4ac − b² < B and
  D ≡ 3 (mod 8), which means 4ac ≡ 4 (mod 8), that is a and c odd: for
  each odd a from 3 and odd b < a, the values for c = a + 2, a + 4, … run
  from 4a(a + 2) − b² in steps of 8a, and
  `C[s::t]=map((1).__add__,C[s::t])` adds 1 along that slice (the right
  side is evaluated first, so its walruses set s and t). a stops at 997,
  since D ≥ 3a² + 12a − 4 > B once a ≥ 891. So `C[D]` = T(D) for every
  D ≡ 3 (mod 8) below B.
- **The bound (n ≤ 49).** Watkins determined every imaginary quadratic
  field with class number at most 100; the largest |discriminant| among
  them is 2383747, with class number 98 (M. Watkins, *Class numbers of
  imaginary quadratic fields*, Math. Comp. 73 (2004), 907–938). So every
  prime p with h(−p) = 2n + 1 ≤ 99 lies below B = 2383747 (B ≡ 3 (mod 8)
  itself has an even class number), and the scan down from B − 8 through
  p ≡ 3 (mod 8) meets a(n) first among the primes with T(p) = n. Trial
  division by every d < p tests primality.
- **The bound (n ≥ 50).** Oesterlé's effective form of the
  Goldfeld–Gross–Zagier theorem gives, for a fundamental discriminant d
  prime to 5077, h(d) > (1/55)·log|d|·∏(1 − ⌊2√q⌋/(q + 1)) over the primes
  q | d with q ≠ |d| (J. Oesterlé, *Le problème de Gauss sur le nombre de
  classes*, Enseign. Math. 34 (1988), 43–67; as stated by D. Goldfeld,
  *The Gauss class number problem for imaginary quadratic fields*). For
  d = −p the product is empty, so p < e^(55h). For n ≥ 50 the scan starts
  at 2^(180n) + B − 8 (`B-8|n//50<<180*n`, ≡ 3 (mod 8)), which exceeds
  e^(55(2n+1)) since 2^180 > e^124.
- **Past the table.** `p<B and C[p]or …` reads the table below B and
  falls back on Dirichlet's class number formula for p ≥ B: for a prime
  p ≡ 3 (mod 8), p > 3, h(−p) = (1/3)·Σ (k/p) over 1 ≤ k ≤ (p − 1)/2 (as
  (2/p) = −1). With Euler's criterion (k/p) ≡ k^((p−1)/2), the number R
  of k in 0…(p − 1)/2 with `pow(k,p//2,p)<2` (k = 0 included) gives
  3h = 2(R − 1) − (p − 1)/2, so T(p) = (4R − p − 9)/12. Below B the
  fallback also runs where `C[p]` is 0: at the primes with h = 1 (11, 19,
  43, 67, 163, where it gives 0, as the table does) and at a few small
  composites.

**Notes**

- So the program is correct for every n, resting on these two theorems;
  in practice a(50) would need class numbers of 9000-bit primes, and the
  program stops making progress there (with little memory). The b-file
  goes on to n = 739, but its terms past n = 49 are conjectural (the
  entry says so; Arno, Robinson and Wheeler had proved n ≤ 11).
- Exact integer arithmetic throughout. The table is a list of B counters
  filled by about 40 million increments; here (about 1.9 times slower
  than the reference) a(0) comes after 3 s and a(49) after 10 s. The bar
  is the 50 terms n = 0…49 that Watkins' theorem covers, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-21 | Python 3 | 300 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002149), CC BY-SA 4.0.
