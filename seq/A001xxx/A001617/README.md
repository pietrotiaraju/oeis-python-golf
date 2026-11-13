# A001617

> Genus of modular group Gamma_0(n). Or, genus of modular curve X_0(n).
> — [OEIS A001617](https://oeis.org/A001617)

Offset 1: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 2, 2, 1, 0, 2, …

### Python 3 — 176 bytes

```python
from math import*
n=1
while[print(1+sum((gcd(x,c,n//c)<2)*(1-6*(x<gcd(c,n//c)))-c//n*(3*(x*x%n==n-1)+4*(-~x*x%n==n-1))for c in range(1,n+1)if n%c<1for x in range(c))//12)]:n+=1
```

**How it works**

- The classical genus formula (Diamond and Shurman, *A First Course in
  Modular Forms*, Theorem 3.1.1 and §3.7–3.8) gives
  **12(g − 1) = ψ − 3ν₂ − 4ν₃ − 6ν∞**, where ψ = ψ(n) is the index of
  Γ₀(n) ([A001615](../A001615/)), ν₂ and ν₃ count its elliptic points of
  order 2 and 3, and ν∞ its cusps ([A001616](../A001616/)).
- ν₂ is the number of x mod n with x² + 1 ≡ 0 and ν₃ the number with
  x² + x + 1 ≡ 0 (by the Chinese remainder theorem and Hensel's lemma these
  are the products Π(1 + (−1/p)) and Π(1 + (−3/p)) of the book, 0 when
  4 | n or 9 | n). In the code: `x*x%n==n-1` and `-~x*x%n==n-1`, with
  −~x = x + 1; both hold for n = 1, where ν₂ = ν₃ = 1.
- ν∞ = Σ φ(g) over the divisors c of n, g = gcd(c, n/c), and the cusp of
  denominator n/c has width c/g, so the widths add up to the index:
  ψ = Σ (c/g)·φ(g). Both are counted over x = 0, …, c − 1: (c/g)·φ(g) of
  them have gcd(x, g) = gcd(x, c, n/c) = 1, and φ(g) of those are below g.
  So `(gcd(x,c,n//c)<2)*(1-6*(x<gcd(c,n//c)))` adds up ψ − 6ν∞.
- The elliptic terms ride along on the divisor c = n, where x runs over all
  residues mod n: `c//n` is 1 there and 0 for every smaller divisor. The
  sum is 12(g − 1), so `1+…//12` is the genus.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Term n costs σ(n) steps (about 1.6·n), so the time grows like n².
- Summing the cusp widths over `range(gcd(c,n//c))` with weight
  `n//c//gcd(c,n//c)-6` is as long, but then the elliptic terms need their
  own sum over `range(n)`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 176 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001617), CC BY-SA 4.0.
