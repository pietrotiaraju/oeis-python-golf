# A000784

> Number of symmetrical planar partitions of n (planar partitions (A000219) that when regarded as 3-D objects have just one symmetry plane).
> — [OEIS A000784](https://oeis.org/A000784)

Offset 1: 0, 1, 2, 2, 4, 6, 6, 11, 16, 20, 28, 41, 51, 70, 93, 122, 158, 211, 266, 350, …

### Python 3 — 230 bytes

```python
g=lambda B,s,x=[]:(x and g(x+[-1],s)or s==0)+sum(g(B[1:],s+1-(3*v+2<<(x>[])),x+[v])for v in range(min(B[1]+1,s,*x[-1:])))
*a,n=1,0
while 1:n+=1;a+=sum(d*(d%2or-d//4)*sum(a[d::d])for d in range(-n,0))//-n,;print(a[-1]-g([n]*3*n,n))
```

**How it works**

- **Burnside.** As 3-D objects, plane partitions of n are stacks of n unit
  cubes in the corner of space, closed downward; two are the same object when
  a permutation of the three axes (the group S₃) maps one to the other.
  Write P(n) for all plane partitions ([A000219](../A000219/)), S(n) for the
  ones fixed by the swap x↔y (symmetric plane partitions,
  [A005987](https://oeis.org/A005987)), C(n) for the ones fixed by the
  3-cycle x→y→z→x (cyclically symmetric, [A096419](https://oeis.org/A096419))
  and T(n) for the ones fixed by all of S₃ (totally symmetric,
  [A048141](https://oeis.org/A048141)).
- **One mirror plane.** An object with exactly one symmetry plane has a
  stabilizer of order 2 in S₃: its three placements are fixed by one swap
  each, and exactly one of them is fixed by x↔y. A partition fixed by x↔y
  and by any other permutation is fixed by all of S₃ (two swaps generate
  S₃, and so do a swap and a 3-cycle). So a(n) = S(n) − T(n).
- **S(n)** comes from the Euler product Π_i 1/(1 − x^(2i−1)) ·
  Π_{i<j} 1/(1 − x^(2(i+j−1))) (Andrews, Gordon; Stanley 1971,
  Prop. 14.3), i.e. exponents b(k) = 1 for odd k and ⌊k/4⌋ for even k, and
  the recurrence m·S(m) = Σ_k k·b(k)·(S(m−k) + S(m−2k) + …) of
  [A000041](../A000041/): with d = −k, `d%2or-d//4` is b(k) and the slice
  `a[d::d]` is S(m−k), S(m−2k), ….
- **Totally symmetric partitions by size** have no product formula (the
  q-TSPP theorem counts orbits of cubes, not cubes), so T(n) is counted by a
  search. Cut a totally symmetric π by its smallest coordinate t: the cubes
  (t, j, k) with j, k ≥ t form a symmetric Ferrers diagram cornered at
  (t, t); write it by its diagonal arms a₀ > a₁ > … ≥ 0 (Frobenius
  coordinates). π is closed downward exactly when, for every t, layer t+1
  fits inside layer t minus its first row and column: it has fewer arms and
  a′ᵢ ≤ aᵢ₊₁. Layer t holds the 3a₀ + 1 + Σ_{i≥1} (6aᵢ + 3) cubes whose
  smallest coordinate is t. (Checked against the A048141 b-file up to 150.)
- **The search `g(B,s,x)`.** x is the layer being built (its arms so far),
  s the cubes still to place, and B the previous layer followed by −1,
  consumed one place per arm, so that `B[1]` is the bound aᵢ₊₁ for the next
  arm (and the −1 stops a layer from getting as long as the one before).
  The next arm v is below `B[1]+1`, below s (pruning) and below the previous
  arm (`*x[-1:]`, empty at the start of a layer). `3*v+2<<(x>[])` minus 1
  is 3v+1 for the first arm and 6v+3 after it. `x and g(x+[-1],s)or s==0`
  closes the layer and starts the next one; an empty layer ends π, which
  counts when s = 0 (`or` cannot hide a count: g of a new layer is ≥ 1
  when s = 0). The first call `g([n]*3*n,n)` leaves the first layer
  unbounded: a layer with p arms costs at least 3p − 2 cubes, so `B[1]`
  always exists.
- Reading the bound one place ahead (`B[1]` of `x+[-1]`) instead of
  `B[0]` of `x[1:]+[-1]` saves 4 bytes.

**Notes**

- Exact integer arithmetic; correct for every n (the product formula for
  S is a theorem, the search for T is exhaustive). Matches the whole
  b-file.
- The search visits every totally symmetric partition of n, again for each
  n (about 1.5·10⁵ of them up to n = 150): 172 terms in 60 s here. The
  b-file has 150 terms; the bar is 150 terms in 60 s.
- Layers have strictly fewer arms each time and a first layer of L arms
  costs at least 3L² − 3L + 1 cubes, so the recursion is about n/6 levels
  deep (two frames each): Python's default limit of 1000 frames is only
  reached near n = 2700, far out of reach in time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 230 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000784), CC BY-SA 4.0.
