# A000448

> Smallest number that is the sum of 2 squares in at least n ways.
> — [OEIS A000448](https://oeis.org/A000448)

Offset 1: 0, 25, 325, 1105, 4225, 5525, 27625, 27625, 71825, 138125, …

### Python 3 — 319 bytes

```python
from functools import*
@cache
def G(d,i,b):
 if d<2:return 1
 t=p=P[i];v=p*G(-~d//2,i+1,1)
 for e in range(2,min(b+1,d)):
  t*=p
  if t>=v:break
  v=min(v,t*G((d+e)//-~e,i+1,e))
 return v
P=[];p=t=n=1
print(0)
while n:=n+1:
 while len(P)<(2*n).bit_length():
  t*=p*p;p+=1;P+=[p]*(t%p>0<p%4==1)
 print(G(d:=2*n-1,0,d-1))
```

**How it works**

- By the two-square count and exchange argument on
  [A000446](../A000446/), a positive minimum uses increasing
  primes p_i≡1 mod 4 with nonincreasing positive exponents e_i.
  It has ⌈∏(e_i+1)/2⌉ unordered nonnegative-square
  representations, so the target here is **∏(e_i+1)≥2n−1**.
- `G(d,i,b)` finds the least remaining product using primes from
  P[i] onward, requiring an exponent-factor product at least d,
  with the next exponent at most b. If d<2, no further prime is
  needed and the answer is the multiplicative identity 1.
- Choosing exponent e leaves threshold ⌈d/(e+1)⌉. The integer
  expression `(d+e)//-~e` computes it exactly, and passing e
  as the next bound enforces nonincreasing exponents.
- The exponent-1 choice gives an initial valid candidate
  `p*G((d+1)//2,i+1,1)`. The loop then tries exponents 2
  through min(b,d−1), maintaining t=pᵉ. Larger exponents need
  not be tried: e=d−1 already satisfies the entire remaining
  threshold with this prime alone.
- Once t≥v, even multiplying t by the smallest possible remaining
  factor 1 cannot improve the current valid answer v. Breaking there
  is a rigorous pruning bound, not an arbitrary search cutoff.
- Every positive exponent multiplies the factor count by at least
  2, so only logarithmically many prime positions are needed. The
  loop extends P to `(2*n).bit_length()` primes and retains the
  same prime prefix between outputs.
- P contains successive primes 1 mod 4. Immediately before
  testing p, t is ((p−1)!)²: multiply by the preceding p²,
  then increment p. For primes, Wilson's theorem makes t%p=1.
  For composite p>4, (p−1)! is divisible by p, so t%p=0.
  The exceptional composite 4 is excluded by p%4==1 anyway.
  Thus `t%p>0<p%4==1` selects exactly the required primes.
- Print 0 first for n=1, then call `G(d:=2*n-1,0,d-1)`.
  The initial exponent bound d−1 is sufficient by the same argument
  used inside the recursion.

**Notes**

- Every admissible exponent pattern is either evaluated or excluded
  by a lower bound already no smaller than a valid answer. Thus the
  memoized search returns the global minimum using exact integers.
- For n=7, 27625=5³·13·17 has factor product 4·2·2=16,
  giving eight representations. It qualifies both here and for n=8,
  explaining the repeated output 27625.
- Unlike the exact-count sequence [A000446](../A000446/), these
  minima are nondecreasing: increasing the threshold only removes
  candidates. Enforcing exact equality would incorrectly reject
  useful candidates that overshoot the threshold.
- `@cache` reuses `(d,i,b)` states across calls and output indices.
  Cache storage and large-integer products are the main resource
  costs; no bound on the numerical size of the minimum is imposed.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 366 | first entry |
| 2026-11-06 | Python 3 | 361 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 319 | use Wilson prime generation and shorten exact threshold expressions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000448), CC BY-SA 4.0.
