# A001327

> Number of equivalence classes of 3-valued Post functions of n variables under action of semi-direct product of symmetric groups S_n and S(n,3).
> — [OEIS A001327](https://oeis.org/A001327)

Offset 1: 10, 438, 5893028544, 14256252837121596073801515513052992, …

a(n) counts the functions f: {0,1,2}ⁿ → {0,1,2} up to permuting the n
variables and applying any permutation of {0,1,2} to each variable
separately (S(n,3) = S₃ⁿ, of order 6ⁿ). Only the inputs are transformed.
Together the two give the wreath product S₃ ≀ Sₙ, of order 6ⁿ·n!.

### Python 3 — 237 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r+k,*L,(k,o))for k in range(-r,0)for o in b'')//r//6or(m:=lcm(*map(prod,L)))and 3**(sum(prod((3>>t//(d:=gcd(t,k))%o*~-o)**d for k,o in L)for t in range(m))//m)
n=1
while[print(f(n))]:n+=1
```

The tuple holds six raw control bytes (0x01, 0x02, 0x02, 0x02, 0x03, 0x03)
that a browser does not show. Byte for byte, the middle of the second line
is

```text
for o in b'<01><02><02><02><03><03>'
```

where `<01>` stands for the single byte 0x01, and so on. Written as
`for o in(1,2,2,2,3,3)` the program is 240 bytes.

**What is counted**

- By Burnside's lemma a(n) = Σ_g 3^c(g) / (6ⁿ·n!), where c(g) is the number
  of cycles of g on the 3ⁿ inputs: a function is fixed by g exactly when it
  is constant on each cycle.
- An element g permutes the coordinates and applies a permutation of
  {0,1,2} to each. Going once round a cycle of the coordinate permutation,
  of length k, composes these into a permutation h of {0,1,2}, the cycle
  product. Its order o is 1 (identity), 2 (a transposition) or 3 (a
  3-cycle).
- gᵗ moves every coordinate t steps along its cycle, so it splits a cycle of
  length k into d = gcd(t,k) orbits of k/d coordinates, and going once round
  such an orbit applies t/d turns of the cycle, a conjugate of h^(t/d). A
  point fixed by gᵗ is fixed by its values on one coordinate per orbit, each
  a fixed point of h^(t/d), so the cycle contributes a factor
  (number of fixed points of h^(t/d))^d. With j = t/d: 3 when o divides j,
  and otherwise 1 for a transposition and 0 for a 3-cycle.
- The order of g is m = lcm(k·o) over the cycles, and Burnside's lemma for
  the cyclic group ⟨g⟩ gives c(g) = (1/m) Σ_{t<m} fix(gᵗ).

**How it works**

- `f(r,*L)` averages over the elements acting on r further coordinates,
  given the cycles `L` chosen so far as pairs (k, o), with k stored negative.
  The cycle through one chosen coordinate has length k with probability
  1/r. Its cycle product is uniform on S₃: for a fixed cycle each of the 6^k
  choices of permutations along it gives each product 6^(k−1) times. S₃ has
  one element of order 1, three of order 2 and two of order 3, hence the
  bytes 1, 2, 2, 2, 3, 3, and f(r,L) = Σ_{k,o} f(r−k, L+[(k,o)]) / (6r):
  `k` runs over −r…−1, `r+k` coordinates are left, and `//r//6` divides.
- At r = 0, `(3>>t//(d:=gcd(t,k))%o*~-o)**d` is the factor of one cycle:
  with j = t/d, `j%o*(o-1)` is 0 when o divides j (3 fixed points), 1 for a
  transposition with j odd (`3>>1` = 1) and at least 2 for a 3-cycle with
  3 ∤ j (`3>>2` = 0). `prod(…)` is fix(gᵗ), `map(prod,L)` gives the k·o
  (negative, which `lcm` ignores), and `3**(sum(…)//m)` is 3^c(g).
- The floors are exact. f(r,L) is (1/|H|) Σ_{h∈H} fix(hτ), with H = S₃ ≀ S_r
  and τ the part already chosen (fix counting the functions fixed); by de
  Bruijn's lemma (for H normal in G and τ in G this is the number of
  H-orbits that τ maps to themselves) it is an integer.
- Exact integers throughout, so the program is right for every n.

**Notes**

- The signed cycles of [A001325](../A001325/) and
  [A000616](../../A000xxx/A000616/) only tell two classes apart; S₃ has
  three, so each cycle carries its order. Iterating `for o in b'122233'`
  and storing `(k,o%4)` is 239 bytes.
- The recursion visits 6·7^(n−1) labelled compositions of n: a(5) arrives
  in 0.4 s, a(6) in 3 s and a(7) in about 25 s. The terms grow like
  3^(3ⁿ)/(6ⁿ·n!): a(9), about 9379 digits, would pass Python's 4300-digit
  limit for printing integers, long after the timeout.
- The OEIS b-file is synthesized from the entry: 5 terms (n = 1 to 5). The
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 237 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001327), CC BY-SA 4.0.
