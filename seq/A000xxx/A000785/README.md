# A000785

> Number of asymmetrical planar partitions of n: planar partitions (A000219) that when regarded as 3-D objects have no symmetry.
> — [OEIS A000785](https://oeis.org/A000785)

Offset 1: 0, 0, 0, 1, 2, 5, 11, 21, 39, 73, 129, 226, 388, 659, 1100, 1821, 2976, 4828, 7754, 12370, …

### Python 3 — 297 bytes

```python
g=lambda B,s,x=[]:(x and g(x+[-1],s)or s==0)+sum(g(B[1:],s+1-(3*v+2<<(x>[])),x+[v])for v in range(min(B[1]+1,s,*x[-1:])))
L=[1,-3,-1];n=0
while 1:n+=1;exec("L+=sum(d*[-d,d%2or-d//4,-~-d%3-1or(3-d)//9][len(L)%3]*sum(L[3*d::3*d])for d in range(-n,0))//-n,;"*3);print((sum(L[-3:])+3*g([n]*3*n,n))//6)
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
- **No symmetry.** A partition with trivial stabilizer lies in a free orbit
  of 6. The partitions with a nontrivial stabilizer are the union of the
  three sets fixed by a swap (S(n) each) and the set fixed by the 3-cycles
  (C(n)); any two or more of these four sets meet exactly in the totally
  symmetric ones, so by inclusion–exclusion the union has
  3S + C − 6T + 4T − T = 3S + C − 3T elements and
  6·a(n) = P(n) − 3·S(n) − C(n) + 3·T(n).
- **Three Euler products.** P, S and C have product generating functions
  Π_k (1 − x^k)^(−b(k)):
  - P: b(k) = k (MacMahon);
  - S: Π_i 1/(1 − x^(2i−1)) · Π_{i<j} 1/(1 − x^(2(i+j−1))) (Andrews,
    Gordon; Stanley 1971, Prop. 14.3), so b(k) = 1 for odd k and ⌊k/4⌋ for
    even k;
  - C: the Mills–Robbins–Rumsey theorem (Macdonald's conjecture, 1982)
    gives the size generating function of the cyclically symmetric plane
    partitions in an m×m×m box as
    Π_{i=1..m} (1 − x^(3i−1))/(1 − x^(3i−2)) · Π_{j=i..m} (1 − x^(3(m+i+j−1)))/(1 − x^(3(2i+j−1))).
    A cyclically symmetric partition that reaches coordinate m contains
    (m,0,0), (0,m,0), (0,0,m) and everything below them, so at least 3m+1
    cubes; below degree 3m+1 the box does not matter and the factors that
    change with m have degree above 3m, so the limit m → ∞ is
    Π_i (1 − x^(3i−1))/(1 − x^(3i−2)) · Π_{i≤j} 1/(1 − x^(3(2i+j−1))):
    b(k) = 1 and −1 for k ≡ 1, 2 (mod 3) and ⌊(k+3)/9⌋ for k ≡ 0 (the
    number of i ≤ j with 2i+j−1 = k/3).
- **Euler transform.** For F = Π (1 − x^k)^(−b(k)) the logarithmic
  derivative gives m·f(m) = Σ_k k·b(k)·(f(m−k) + f(m−2k) + …), an exact
  division. The three series live interleaved in one list
  `L = [P(0), −3·S(0), −C(0), P(1), …]`, each pre-scaled by its Burnside
  weight (the recurrence is linear, so scaling the start scales the whole
  series). With d = −k the slice `L[3*d::3*d]` steps back 3k places, i.e.
  k terms of the series being computed, whichever it is.
  `L=[1,-3,-1]` holds P(0), −3·S(0), −C(0), and `sum(L[-3:])` is
  P − 3S − C.
- **Weights in d = −k.** `-d` is k; `d%2or-d//4` is 1 for odd k, else
  ⌊k/4⌋ (`-d//4` floors −d = k); `-~-d%3-1` is (k+1) mod 3 − 1, i.e. 1, −1, 0
  for k ≡ 1, 2, 0 (mod 3), and the `or` falls through to `(3-d)//9` =
  ⌊(k+3)/9⌋ exactly when it is 0.
- The three passes are one `exec("…;"*3)` string; `[len(L)%3]` says which
  series the pass computes (1 byte under a `for t in 0,1,2:` block, which
  needs its own lines).
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

- Exact integer arithmetic. Correctness for every n rests on the product
  formulas for S (Andrews–Gordon/Stanley) and C (Mills–Robbins–Rumsey);
  the search for T is exhaustive. Matches the whole b-file.
- The search visits every totally symmetric partition of n, again for each
  n: 172 terms in 60 s here. The b-file has 150 terms; the bar is
  150 terms in 60 s.
- Layers have strictly fewer arms each time and a first layer of L arms
  costs at least 3L² − 3L + 1 cubes, so the recursion is about n/6 levels
  deep (two frames each): Python's default limit of 1000 frames is only
  reached near n = 2700, far out of reach in time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 297 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000785), CC BY-SA 4.0.
