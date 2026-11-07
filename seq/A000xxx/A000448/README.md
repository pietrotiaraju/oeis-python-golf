# A000448

> Smallest number that is the sum of 2 squares in at least n ways.
> — [OEIS A000448](https://oeis.org/A000448)

Offset 1: 0, 25, 325, 1105, 4225, 5525, 27625, 27625, 71825, 138125, …

Representations m = x² + y² are counted with 0 ≤ x ≤ y.

### Python 3 — 219 bytes

```python
from functools import*
@cache
def G(c,i):
 p=t=P[i];v=p**c;k=2
 while t<v:v=min(v,t*G(c//k,i+1));t*=p;k+=1
 return v
c=0;P=[];p=t=1
while 1:
 while 2**len(P)<=c:t*=p*p;p+=1;P+=[p]*(t%p>0<p%4<2)
 print(c and G(c,0));c+=2
```

**How it works**

- **The count.** As on [A000446](../A000446/), m has ⌈B/2⌉
  representations, B = Π (e+1) over its primes p ≡ 1 (mod 4) (when the
  primes ≡ 3 (mod 4) have even exponents), and a minimal m > 0 is a
  product of the smallest such primes 5, 13, 17, …, used consecutively.
  At least n ways means B ≥ 2n − 1, that is B > c with c = 2n − 2.
- **The search.** G(c, i) is the least Π_{j≥i} P[j]^(e_j) with every
  exponent at least 1 and Π (e_j + 1) > c. Giving P[i] the exponent e
  (k = e + 1) leaves the condition Π_{rest} > c/k, that is > ⌊c/k⌋, so
  G(c, i) = min over e ≥ 1 of P[i]^e·G(⌊c/(e+1)⌋, i+1), and G(0, i) = 1.
- **Pruning.** v starts at P[i]^c, the exponent e = c alone (c + 1 > c),
  which also makes G(0, i) = p⁰ = 1 with no special case. A candidate with
  exponent e is at least t = pᵉ, so once t ≥ v no larger exponent can win
  and the loop stops; at e = c, t = v at the latest. The `@cache` on
  (c, i) is shared by all n.
- **The code.** `c and G(c,0)` prints a(1) = 0 (0 = 0² + 0²) first. G
  reads P[i] at depth i only after i factors of at least 2 with c ≥ 2
  left at the parent, so 2^i ≤ c; `while 2**len(P)<=c:` keeps
  2^len(P) > c. The primes come from Wilson's theorem as on
  [A000446](../A000446/): before p is tested t = ((p−1)!)², and
  `t%p>0<p%4<2` keeps the primes ≡ 1 (mod 4).

**Notes**

- Other versions that print the same terms:
  - without `@cache`: 189 bytes, but only 1599 terms in 60 s; with a
    nonincreasing-exponent bound instead of the cache,
    `def G(c,i,b)` / `while t<v*(k<b):` / `G(c//k,i+1,k+1)`: 205 bytes,
    5340 terms in 60 s;
  - the bounded search with the cache and the ceiling ⌈d/(e+1)⌉ kept as
    `(d+e)//-~e`, the first version: 319 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 10000 terms print in about 6 s here (26000 terms in 60 s).
  The b-file has 10000 terms (up to a(10000)); the bar is the whole
  b-file in 60 s.
- a(n) is a product of about log₂(2n) small primes, so the 4300-digit
  limit is out of reach.
- The minima are nondecreasing and can repeat: a(7) = a(8) = 27625 =
  5³·13·17, B = 16.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 366 | first entry |
| 2026-11-06 | Python 3 | 361 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 319 | use Wilson prime generation and shorten exact threshold expressions |
| 2026-11-07 | Python 3 | 219 | threshold B > c, start at p^c, no exponent bound, `2**len(P)<=c` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000448), CC BY-SA 4.0.
