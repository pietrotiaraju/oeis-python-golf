# A000862

> Number of n-input 2-output switching networks under action of AG(n,2) and complementing group C(2,2) on inputs and outputs.
> — [OEIS A000862](https://oeis.org/A000862)

Offset 1: 3, 8, 49, 3963, 7320535610, …

### Python 3 — 268 bytes

```python
n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=1
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  if max(m)<0:k+=8;t+=r*r*(6-(10>>min(map(m.count,m))))+2**-~sum(2-m.count(v)%2for v in{*m})
 print(t//k);n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}² (n inputs, 2 outputs) up to f ↦ h∘f∘g, where g runs
  over AG(n,2), the 2ⁿ·|GL(n,2)| affine maps x ↦ A·x ⊕ b of the inputs, and h
  over the 8 maps that permute and complement the two outputs (S(2) with
  C(2,2)). The OEIS name says "complementing group C(2,2) on inputs and
  outputs", but C(2,2) alone on the outputs gives [A000850](../A000850/);
  permuting and complementing the outputs is the group that fits the data. A
  brute-force Burnside over all pairs (g, h) matches the data for n ≤ 4.
- Burnside: a(n) = Σ_g,h fix(g,h) / (|AG(n,2)|·|H|). A pair fixes f when f(g(x))
  = h(f(x)) for every x, so f is free at one input of each cycle C of g on the
  2ⁿ inputs, and there its value y must satisfy h^|C|(y) = y. So fix(g,h) = Π_C
  Fix(h^|C|), Fix counting the outputs a map fixes, and the program adds the
  weight W(g) = Σ_h fix(g,h) over every g. Below, c is the number of cycles of
  g, r = 2^c and L a cycle length.

**How it works**

- **Every affine map.** As in [A000214](../A000214/): i runs over the N^(n+1)
  choices (N = 2ⁿ); its lowest base-N digit is b and the next n digits are the
  columns of A. The list starts as `[b]` and each column c doubles it with
  `m+=[y^c for y in m]`, so m[x] = g(x); the walrus in `[m:=[i%N]]*n` resets m
  and gives the n passes.
- **Cycle labels.** A000214's cycle walk, except that a visited point gets the
  label `~r` instead of −1, and r (reset to 1 for each map) doubles each time a
  cycle closes. Afterwards every point of the i-th cycle holds ~2^i, r = 2^c,
  and `m.count(v)` over the labels v in `{*m}` are the cycle lengths. A singular
  map never reaches a point outside its image, so that position keeps a value ≥
  0: `max(m)<0` keeps exactly the bijections, and `k` adds |H| for each, ending
  at |AG(n,2)|·|H|.

**The weight**

- By cycle type on the 4 outputs: the identity gives r²; the 3 translations (two
  2-cycles) give r² when every cycle of g is even (E₂) and 0 otherwise; the 2
  swaps with two fixed outputs give 2^Σgcd(L,2), as in [A000835](../A000835/);
  the 2 four-cycles give r² when 4 divides every cycle length (E₄) and 0
  otherwise. So W = r²(1 + 3E₂ + 2E₄) + 2·2^Σgcd(L,2).
- With u = `min(map(m.count,m))`, the shortest cycle length, E₂ = [u > 1] (an
  odd cycle forces a fixed point, see the sum argument on
  [A000850](../A000850/)) and E₄ = [u > 2] (a cycle of length ≡ 2 mod 4 gives g²
  an odd cycle, hence a fixed point, which lies on a cycle of g of length 1 or
  2). So 1 + 3E₂ + 2E₄ is 1, 4, 6 for u = 1, 2, ≥ 4: `6-(10>>u)`. The last term
  is `2**-~sum(2-L%2…)`, and `k+=8` divides by |H|.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every printed term is right.
  The loop visits all 2^(n²+n) pairs (A, b): a(4) takes about 18 s here, and
  a(5) would need 2³⁰ maps, many hours. The bar is the first 4 terms in 60 s;
  the b-file is the OEIS data (7 terms).
- AG(n,2) on the inputs with the range groups of Harrison's table (m = 2/3):
  trivial [A000820](../A000820/)/[A000821](../A000821/), S(m)
  [A000835](../A000835/)/[A000836](../A000836/), C(2,m)
  [A000850](../A000850/)/[A000851](../A000851/), S(m) with C(2,m)
  A000862/[A000863](../A000863/), GL(m,2)
  [A000880](../A000880/)/[A000881](../A000881/), AG(m,2)
  [A000895](../A000895/)/[A000896](../A000896/). One output and no range group
  is [A000214](../A000214/); other entries of the table take complementing,
  S(n), B(n) or GL(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 268 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000862), CC BY-SA 4.0.
