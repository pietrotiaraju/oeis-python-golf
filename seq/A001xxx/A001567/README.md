# A001567

> Fermat pseudoprimes to base 2, also called Sarrus numbers or Poulet numbers.
> — [OEIS A001567](https://oeis.org/A001567)

Offset 1: 341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701, 2821, 3277, 4033, 4369, 4371, 4681, 5461, 6601, 7957, 8321, …

The composite numbers n with 2ⁿ⁻¹ ≡ 1 (mod n).

### Python 3 — 95 bytes

```python
import math
n=F=r=1
while[r*r>n or[F:=F*r,r:=r+1],pow(2,n,n)==2<math.gcd(F,n)and print(n)]:n+=2
```

Sibling: the strong pseudoprimes [A001262](../A001262/).

**How it works**

- Only odd n are tried (`n+=2`): for even n, 2ⁿ⁻¹ − 1 is odd, so n cannot
  divide it. For odd n, 2 is invertible, so 2ⁿ⁻¹ ≡ 1 is the same as
  2ⁿ ≡ 2: `pow(2,n,n)==2` (n = 1 gives 0).
- Compositeness is proved, not guessed. `F` is ⌊√n⌋!, the product of
  1, …, r − 1 where r is the least number with r² > n. A composite n has a
  prime factor at most √n, which divides F; a prime n divides none of the
  factors 1, …, ⌊√n⌋ < n. So gcd(F, n) > 1 exactly when n is composite,
  and since n is odd the gcd is then at least 3: `==2<math.gcd(F,n)`.
- The first item of the list keeps F up to date: when r² ≤ n it multiplies
  F by r and raises r (`[F:=F*r,r:=r+1]`). n grows by 2 per pass and each
  raise lifts r² by 2r + 1 ≥ 3, so one raise per pass is enough.
- The chain only computes the gcd for numbers that pass the Fermat test
  (primes and pseudoprimes), and `and print(n)` prints n only when both
  hold. The list is never empty, so the loop runs forever.
- `import math` rather than `from math import*`, which would hide the
  built-in three-argument `pow`.

**Notes**

- Exact for every n, with no probabilistic step.
- One modular power per odd n dominates: a(800) = 11242465 arrives after
  about 25 s on the PC it was written on. The b-file has 101629 terms (up
  to about 10¹²); the bar is 800 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001567), CC BY-SA 4.0.
