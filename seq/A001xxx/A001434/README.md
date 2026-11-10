# A001434

> Number of graphs with n nodes and n edges.
> — [OEIS A001434](https://oeis.org/A001434)

Offset 0: 1, 0, 0, 1, 2, 6, 21, 65, 221, 771, 2769, 10250, 39243, 154658, 628635, …

The graphs with n nodes and n edges, counted by Pólya's method: the
coefficient of a power of x in the edge-weighted cycle index of the
pair action of Sₙ, as on [A000717](../../A000xxx/A000717/).

### Python 3 — 264 bytes

```python
from math import*
f=lambda r,W,*L:r and sum(f(r-j,W*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)%M//j//-~L.count(j),*L,j)for j in range(1,min(L+(r,))+1))or W
n=0
while 1:B=n*n;M=1<<B*-~n;print(f(n,F:=factorial(n))//F>>B*n);n+=1
```

**How it works**

- **Burnside with weights.** The graphs on n unlabeled nodes with m edges
  number [x^m] (1/n!) Σ_π Π_c (1 + x^|c|), the product running over the
  orbits c of the node permutation π on the C(n, 2) possible edges (a graph
  fixed by π is a union of whole orbits). Two cycles of π of lengths j and l
  give gcd(j, l) orbits of length lcm(j, l); one j-cycle gives ⌊(j−1)/2⌋
  orbits of length j on its own edges, plus one of length j/2 (the
  diameters) when j is even. In the code these are
  `(1<<B*lcm(j,l)|1)**gcd(j,l)`, `(1<<B*j|1)**(~-j//2)` and
  `(~j%2<<B*j//2|1)` (`~j%2` is 1 exactly when j is even).
- **One leaf per cycle type.** `f(r,W,*L)` adds cycles in nonincreasing
  order of length (`range(1,min(L+(r,))+1)`), so it reaches each partition
  of n once: p(n) leaves instead of the 2ⁿ⁻¹ compositions of the
  cycle-at-a-time recursion of [A000717](../../A000xxx/A000717/). The weight
  `W` starts at n! and is divided by j for each j-cycle and by the number of
  j-cycles so far (`//j//-~L.count(j)`). At every prefix it is n!/z, where
  z = Π jᵐʲ·mⱼ! for the cycles chosen so far: z divides s! for the s points
  they use, so W is an integer and every division is exact. A leaf then
  holds n!/z_λ times the weight polynomial of its cycle type λ, and their
  sum is n! times the answer polynomial: `//F` removes the n!.
- **One big integer.** The polynomials are numbers in base X = 2^B with
  B = n² (Kronecker substitution), reduced mod M = a power of X after each
  product. Only coefficients up to the wanted one are kept: the high ones
  could overflow, but carries only move upwards. No kept coefficient
  overflows: before or after a division it is at most n!·2^C(n,2), and
  n!·2^C(n,2) < 2^(n²), because log₂ n < (n+1)/2.
- **The answer** is the coefficient of xⁿ. M = Xⁿ⁺¹ keeps xⁿ as the top
  digit, so `//F>>B*n` reads it off.
- `r and … or W` is safe: every partial sum keeps a positive constant digit.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- One leaf per partition of n, but the polynomials have about n³ bits, so
  each term takes about three times as long as the one before: on the PC
  used a(23) arrives after about 7 s. The bar is 24 terms in 60 s; the
  b-file has 51.

### Python 3, 17 terms — 213 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(f(r-j,*L,j)*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)for j in range(1,r+1))%M//r
n=0
while 1:B=n*n;M=1<<B*-~n;print(f(n)>>B*n);n+=1
```

**How it works**

- **Cycle at a time.** `f(r,*L)` is the recursion of
  [A000717](../../A000xxx/A000717/): the cycle through a fixed one of the r
  remaining points has each length j = 1…r for (r − 1)! of the r!
  permutations, so f averages over j, multiplying in the orbit factors of the
  new cycle with itself and with the earlier ones in `L`, and divides by r.
  Each coefficient is an orbit count of edge sets of one size (de Bruijn's
  form of Burnside's lemma), so `//r` is exact; `r<1or` returns True (1) at
  the leaves. No n!, no multiplicities, but all 2ⁿ⁻¹ compositions of n are
  visited.
- The same base X = 2^(n²) and reduction mod M after each sum as the main
  record.
- **The answer.** M = Xⁿ⁺¹ and the answer is the top digit, `f(n)>>B*n`.

**Limits**

- Exact for every n, but the recursion visits all 2ⁿ⁻¹ compositions of n:
  each term takes about three times as long as the one before, and a(16)
  arrives after about 8 s on the PC used, so the bar is 17 terms. The main
  record's partitions reach 24.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 264 | first entry |

**Python 3, 17 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 213 | first entry: cycle-at-a-time Burnside over all compositions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001434), CC BY-SA 4.0.
