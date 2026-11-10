# A001528

> NPN-equivalence classes of switching functions of exactly n variables.
> — [OEIS A001528](https://oeis.org/A001528)

Offset 0: 1, 1, 2, 10, 208, 615904, 200253951911058, …

### Python 3 — 234 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 1<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m-(sum(L)==-n)
n=o=0
while[print(-o+(o:=f(n)))]:n+=1
```

**What is counted**

- Two functions {0,1}ⁿ → {0,1} are NPN-equivalent when one becomes the
  other by permuting the inputs, negating some inputs and possibly negating
  the output. The number of inputs a function really depends on (its
  essential variables) is the same for the whole class.
- Moving the k essential inputs of an n-variable function to the front gives
  a function of exactly k variables, and two n-variable functions with k
  essential inputs are equivalent exactly when these k-variable functions
  are. So the NPN classes of all n-variable functions,
  [A000370](../A000370/)(n), are counted by a(0) + a(1) + … + a(n), and
  a(n) = A000370(n) − A000370(n−1) for n ≥ 1, with a(0) = A000370(0) = 1
  (the two constants form one class). This matches all seven OEIS terms.

**How it works**

- `f(r,*L)` is the recursion of [A000370](../A000370/): Burnside's lemma
  over the 2ⁿ·n! signed permutations of the inputs, summed by signed cycle
  type (`k` > 0 is a negative cycle, with an odd number of negations along
  it, and `k` < 0 a positive one), with `//r>>1` dividing by 2r at every level. At r = 0,
  `sum(prod(…)for t in range(m))//m` is the number c of cycles of g on the
  2ⁿ points; that page explains the fixed-point count of gᵗ.
- The weight of g is 2^c for g and 2^c more for g followed by negating the
  output when every cycle of g on the points has even length. As the A000370
  page shows, that happens exactly when g has no fixed point, that is, when
  some cycle of the signed permutation is negative (has an odd number of
  negations); the signed lengths add up to −n only when none is. A000370
  uses the leaf 2^(c + [some negative cycle]) and halves at the end. Here the
  leaf is already halved: `1<<c-(sum(L)==-n)` is 2^(c − 1 + [some negative
  cycle]) (c ≥ 1, so the exponent is never negative), and `f(n)` is
  A000370(n) itself.
- The floors stay exact after halving. With H the signed permutations of the
  r coordinates still free and τ the part already chosen, f(r,L) is half of
  A + B, where A counts the H-orbits of functions that τ maps to themselves
  and B those that τ followed by output negation maps to themselves (de
  Bruijn's lemma, as on the A000370 page). Negating the output pairs up
  H-orbits: an orbit equal to its own negation is counted in A exactly when
  it is counted in B, and the other orbits come in pairs within A and within
  B. So A + B is even at every level.
- `-o+(o:=f(n))` with `o` starting at 0 prints A000370(0) = 1 first and then
  A000370(n) − A000370(n−1).

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  recursion visits 2·3^(n−1) signed compositions of n: all 7 b-file terms
  (n = 0 to 6) come out in a fraction of a second, and the bar is the whole
  b-file in 60 s.
- From n = 14 the terms have more than 4300 digits, Python's int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 234 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001528), CC BY-SA 4.0.
