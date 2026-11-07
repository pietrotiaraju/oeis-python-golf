# A000821

> Number of switching networks under action of AG_n(Z_2) acting on 3 variables.
> — [OEIS A000821](https://oeis.org/A000821)

Offset 1: 36, 330, 22060, 920737780, 247617673784972437216, …

### Python 3 — 200 bytes

```python
n=r=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^~i%N for y in m];t+=r**3;r=len({*m})>>n;k+=r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
```

**What it counts**

- Maps f: {0,1}ⁿ → {0,1}³ (n inputs, 3 outputs) up to f ↦ h∘f∘g, where g runs
  over AG(n,2), the 2ⁿ·|GL(n,2)| affine maps x ↦ A·x ⊕ b of the inputs, and h
  over the trivial group (only the identity). The entry's name ("AG_n(Z_2)
  acting on 3 variables") puts no group on the outputs. A brute-force Burnside
  over all pairs (g, h) matches the data for n ≤ 4.
- Burnside: a(n) = Σ_g,h fix(g,h) / (|AG(n,2)|·|H|). A pair fixes f when f(g(x))
  = h(f(x)) for every x, so f is free at one input of each cycle C of g on the
  2ⁿ inputs, and there its value y must satisfy h^|C|(y) = y. So fix(g,h) = Π_C
  Fix(h^|C|), Fix counting the outputs a map fixes, and the program adds the
  weight W(g) = Σ_h fix(g,h) over every g. Below, c is the number of cycles of
  g, r = 2^c and L a cycle length.

**How it works**

- The program is A000214's 197-byte one with `t+=r` changed to `t+=r**3`: there
  r = 2^c, and with no range group the weight is 8^c = r³. See
  [A000214](../A000214/) for the tricks: every affine map from the base-N digits
  of one integer i, `r=len({*m})>>n` to keep the bijections and count them in k,
  the cycle walk `while~x:m[x],x=-1,m[x];r<<=x<0`, and the weight added one map
  late in the doubling loop (the stray initial r = 1 is dropped by the floor,
  since k > 1).

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every printed term is right.
  The loop visits all 2^(n²+n) pairs (A, b): a(4) takes about 17 s here, and
  a(5) would need 2³⁰ maps, many hours. The bar is the first 4 terms in 60 s;
  the b-file is the OEIS data (6 terms).
- AG(n,2) on the inputs with the range groups of Harrison's table (m = 2/3):
  trivial [A000820](../A000820/)/A000821, S(m)
  [A000835](../A000835/)/[A000836](../A000836/), C(2,m)
  [A000850](../A000850/)/[A000851](../A000851/), S(m) with C(2,m)
  [A000862](../A000862/)/[A000863](../A000863/), GL(m,2)
  [A000880](../A000880/)/[A000881](../A000881/), AG(m,2)
  [A000895](../A000895/)/[A000896](../A000896/). One output and no range group
  is [A000214](../A000214/); other entries of the table take complementing,
  S(n), B(n) or GL(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 200 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000821), CC BY-SA 4.0.
