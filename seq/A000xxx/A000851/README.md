# A000851

> Number of n-input 3-output switching networks under action of AG(n,2) on the inputs and complementing group C(3,2) on the outputs.
> — [OEIS A000851](https://oeis.org/A000851)

Offset 1: 8, 50, 2908, 115125476, 30952209248265753648, …

### Python 3 — 225 bytes

```python
n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=len({*m})>>n;k+=r
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  t+=r**3>>3*(1in map(m.count,m))
 print(t//k);n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}³ (n inputs, 3 outputs) up to f ↦ h∘f∘g, where g runs
  over AG(n,2), the 2ⁿ·|GL(n,2)| affine maps x ↦ A·x ⊕ b of the inputs, and h
  over C(2,3), the 8 translations y ↦ y ⊕ e of the outputs. The OEIS name gives
  the groups. A brute-force Burnside over all pairs (g, h) matches the data for
  n ≤ 4.
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
- **Cycle labels.** A000214's test `r=len({*m})>>n` is 1 for a bijection and 0
  otherwise, and `k+=r` counts the bijections. The cycle walk then labels a
  visited point `~r` instead of −1, r doubling each time a cycle closes: every
  point of the i-th cycle holds ~2^i, r ends at 2^c, and the points of a cycle
  of length L carry a label that occurs L times. A singular map keeps r = 0 (all
  its labels are ~0 = −1), so its weight, a multiple of r, is 0.

**The weight**

- e = 0 gives 8^c = r³. For e ≠ 0 the outputs fall into four pairs, so a cycle
  of g takes 8 values if its length is even and none if odd: 7·r³·E₂, E₂ = 1
  when every cycle of g is even. So W = r³(1 + 7E₂) = r³·8^E₂.
- An affine map over GF(2) with a cycle of odd length has a fixed point (the sum
  of the points of that cycle, since A·Σx ⊕ b = Σ(A·x ⊕ b) for an odd number of
  terms), so "every cycle even" is "no fixed point", that is, no label occurring
  once: `1in map(m.count,m)` is 1 − E₂.
- The program adds W/8 = r³·8^(E₂−1) as `r**3>>3*(1in map(m.count,m))` (exact,
  since r ≥ 2), so |H| = 8 needs no factor in k.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every printed term is right.
  The loop visits all 2^(n²+n) pairs (A, b): a(4) takes about 20 s here, and
  a(5) would need 2³⁰ maps, many hours. The bar is the first 4 terms in 60 s;
  the b-file is the OEIS data (6 terms).
- AG(n,2) on the inputs with the range groups of Harrison's table (m = 2/3):
  trivial [A000820](../A000820/)/[A000821](../A000821/), S(m)
  [A000835](../A000835/)/[A000836](../A000836/), C(2,m)
  [A000850](../A000850/)/A000851, S(m) with C(2,m)
  [A000862](../A000862/)/[A000863](../A000863/), GL(m,2)
  [A000880](../A000880/)/[A000881](../A000881/), AG(m,2)
  [A000895](../A000895/)/[A000896](../A000896/). One output and no range group
  is [A000214](../A000214/); other entries of the table take complementing,
  S(n), B(n) or GL(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 225 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000851), CC BY-SA 4.0.
