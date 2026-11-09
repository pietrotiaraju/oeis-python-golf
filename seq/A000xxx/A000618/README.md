# A000618

> Number of nondegenerate Boolean functions of n variables: For n > 0, a(n) = A000616(n) - A000616(n-1).
> — [OEIS A000618](https://oeis.org/A000618)

Offset 0: 2, 1, 3, 16, 380, 1227756, 400507805615570, …

### Python 3 — 221 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 1<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m
n=o=0
while[print(-o+(o:=f(n)))]:n+=1
```

**How it works**

- `f(n)` is [A000616](../A000616/)(n), the number of NP-equivalence classes
  of Boolean functions of n variables: Burnside's lemma over the signed
  permutations of the inputs, computed by a recursion over signed cycle
  types (see that page for the recursion, the fixed-point count of gᵗ and
  why every floor is exact).
- The program prints the running difference `-o+(o:=f(n))` with `o`
  starting at 0, so the first line is A000616(0) = 2, the OEIS value of
  a(0), and then A000616(n) − A000616(n−1) for n ≥ 1.

**Notes**

- All 9 b-file terms (n = 0 to 8) come out in well under a second; the bar is
  the whole b-file, 9 terms in 60 s. The recursion visits 2·3^(n−1) signed
  compositions, so later terms slow down by about 3 per step.
- From n = 14 the terms pass Python's 4300-digit limit for printing integers.

## First four terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(3) have to arrive in time.

### Python 3, 4 terms — 203 bytes

```python
from itertools import*
n=o=0
while 1:R=range(2**n);print(-o+(o:=len({min(sum((f>>(s^sum((x>>i&1)<<p[i]for i in p))&1)<<x for x in R)for p in permutations(R[:n])for s in R)for f in range(2**2**n)})));n+=1
```

**How it works**

- `len({…})` is [A000616](../A000616/)(n), the number of NP-equivalence
  classes of Boolean functions of n variables, and the program prints the
  running difference `-o+(o:=…)` as the main record does: A000616(0) = 2 =
  a(0) first, then A000616(n) − A000616(n−1).
- A function is its truth table read as an integer, bit x holding f(x);
  `range(2**2**n)` runs over all 2^(2ⁿ) of them.
- For a permutation p of the coordinates and a mask s,
  `s^sum((x>>i&1)<<p[i]for i in p)` is g(x) = s ⊕ σ̂(x), where σ̂ moves bit i
  of x to position p[i]. `for i in p` visits every index once, only in
  another order, and `R[:n]` is range(n) because n < 2ⁿ. Over all p and s
  these are the 2ⁿ·n! elements of B_n, the group that permutes and negates
  the inputs.
- `sum((f>>g(x)&1)<<x for x in R)` is the truth table of f∘g, so the
  generator yields exactly the NP class of f. Its minimum is the same for
  every member of the class and different classes are disjoint, so the set
  of minima has one element per class.
- Every step is exact integer work, for every n; only the time grows.

**Limits**

- A000616(3) takes 256 functions × 48 transforms of 8 points: the four terms
  come in about 0.1 reference seconds.
- a(4) would take 65 536 functions × 384 transforms of 16 points, about a
  quarter of an hour here, and a(5) a loop over 2³² functions. The main
  record never lists functions: it sums 2^c(g) over signed cycle types.
- 203 bytes is an upper bound on the shortest valid four-term program, not a
  proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 221 | first entry |

**Python 3, 4 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 203 | first entry: smallest truth table of each NP class, over all functions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000618), CC BY-SA 4.0.
