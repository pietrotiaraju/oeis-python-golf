# A000835

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000835](https://oeis.org/A000835)

Offset 1: 7, 22, 153, 15209, 29281010032, …

### Python 3 — 236 bytes

```python
n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=1
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  if max(m)<0:k+=2;t+=r*r+2**sum(2-m.count(v)%2for v in{*m})
 print(t//k);n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}² (n inputs, 2 outputs) up to f ↦ h∘f∘g, where g runs
  over AG(n,2), the 2ⁿ·|GL(n,2)| affine maps x ↦ A·x ⊕ b of the inputs, and h
  over S(2), which swaps the two outputs. Sean A. Irvine's comment on the entry
  names the groups. A brute-force Burnside over all pairs (g, h) matches the
  data for n ≤ 4.
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

- The identity fixes all 4 outputs: 4^c = r². The swap fixes 00 and 11 and
  exchanges 01 and 10, so a cycle takes 4 values if its length is even and 2 if
  odd: 2^gcd(L,2) = 2^(2 − L mod 2) per cycle.
- So W = r² + 2^Σ(2 − L mod 2), and `k+=2` divides by |H| = 2.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every printed term is right.
  The loop visits all 2^(n²+n) pairs (A, b): a(4) takes about 14 s here, and
  a(5) would need 2³⁰ maps, many hours. The bar is the first 4 terms in 60 s;
  the b-file is the OEIS data (7 terms).
- AG(n,2) on the inputs with the range groups of Harrison's table (m = 2/3):
  trivial [A000820](../A000820/)/[A000821](../A000821/), S(m)
  A000835/[A000836](../A000836/), C(2,m)
  [A000850](../A000850/)/[A000851](../A000851/), S(m) with C(2,m)
  [A000862](../A000862/)/[A000863](../A000863/), GL(m,2)
  [A000880](../A000880/)/[A000881](../A000881/), AG(m,2)
  [A000895](../A000895/)/[A000896](../A000896/). One output and no range group
  is [A000214](../A000214/); other entries of the table take complementing,
  S(n), B(n) or GL(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 236 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000835), CC BY-SA 4.0.
