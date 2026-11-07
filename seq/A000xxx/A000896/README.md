# A000896

> Number of switching networks with AG(n,2) acting on the domain and AG(3,2) acting on the range.
> — [OEIS A000896](https://oeis.org/A000896)

Offset 1: 2, 6, 70, 700229, 184239362390740969, …

### Python 3 — 323 bytes

```python
n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=1
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  if max(m)<0:Q=lambda j:2**sum(m.count(v)%j<1for v in{*m});a=r<<Q(2)//r;k+=1344;t+=a*(a*a+224*Q(3)**2)+42*(r*Q(2)<<Q(4)//r)*(a+4*Q(4))+384*Q(7)**3
 print(t//k);n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}³ (n inputs, 3 outputs) up to f ↦ h∘f∘g, where g runs
  over AG(n,2), the 2ⁿ·|GL(n,2)| affine maps x ↦ A·x ⊕ b of the inputs, and h
  over AG(3,2), the 1344 affine maps of the outputs. The OEIS name gives the
  groups. A brute-force Burnside over all pairs (g, h) matches the data for n ≤
  4.
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
- **Q(j)** = 2^c_j, where c_j counts the cycles of g whose length j divides (the
  labels whose count j divides). Q(j) ≤ r = Q(1), with equality exactly when j
  divides every cycle length, so `Q(j)//r` is that 0/1 flag; E₂ and E₄ are the
  flags for j = 2 and 4.

**The weight**

- By cycle type on the 8 outputs: 1⁸ (1 map) gives r³; 1⁴2² (42) r²·Q(2); 2⁴
  (49) r³·E₂; 1²3² (224) r·Q(3)²; 2·6 (224) r·Q(3)²·E₂; 1²·2·4 (168)
  r·Q(2)·Q(4); 4² (252) r³·E₄; 1·7 (384) Q(7)³.
- With D₁ = r·2^E₂ (`a`) and D₂ = r·Q(2)·2^E₄ this is W = D₁(D₁² + 224Q(3)²) +
  42D₂(D₁ + 4Q(4)) + 384Q(7)³: D₁³ and 42D₁D₂ give r³(1 + 49E₂ + 84E₄) +
  42r²Q(2), and 168D₂Q(4) = 168rQ(2)Q(4) + 168r³E₄. `k+=1344` divides by |H|.
- When g has a fixed point (E₂ = 0), W is 8 times the weight of
  [A000881](../A000881/) with that fixed cycle removed (r → r/2): normalizing f
  at the fixed point absorbs the translations of the outputs.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every printed term is right.
  The loop visits all 2^(n²+n) pairs (A, b): a(4) takes about 20 s here, and
  a(5) would need 2³⁰ maps, many hours. The bar is the first 4 terms in 60 s;
  the b-file is the OEIS data (7 terms).
- AG(n,2) on the inputs with the range groups of Harrison's table (m = 2/3):
  trivial [A000820](../A000820/)/[A000821](../A000821/), S(m)
  [A000835](../A000835/)/[A000836](../A000836/), C(2,m)
  [A000850](../A000850/)/[A000851](../A000851/), S(m) with C(2,m)
  [A000862](../A000862/)/[A000863](../A000863/), GL(m,2)
  [A000880](../A000880/)/[A000881](../A000881/), AG(m,2)
  [A000895](../A000895/)/A000896. One output and no range group is
  [A000214](../A000214/); other entries of the table take complementing, S(n),
  B(n) or GL(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 323 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000896), CC BY-SA 4.0.
