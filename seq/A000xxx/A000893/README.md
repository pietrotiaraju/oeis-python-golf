# A000893

> Number of switching networks with GL(n,2) acting on the domain and AG(3,2) acting on the range.
> — [OEIS A000893](https://oeis.org/A000893)

Offset 1: 2, 8, 214, 10740500, 5895494078673763322, …

### Python 3 — 290 bytes

```python
n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n;s=u=v=w=r=len({*m})>>n;k+=1344*r
  for x in m:
   while~x:m[x],x=-1,m[x];i+=1;r<<=x<0
   s<<=i%2;u<<=i%3%2;v<<=i%4==1;w<<=i%7==1;i=0
  t+=r*(r*r+42*s*(r+4*v)+224*u*u)+384*w**3
 print(t//k);n+=1
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to f ↦ h∘f∘A, with
  A ∈ GL(n,2) on the inputs and h ∈ AG(3,2) (affine maps y ↦ By ⊕ b of the
  outputs, 1344 of them).
- Burnside over the pairs (A, h): (A, h) fixes f when f(Ax) = h(f(x)) for
  every x. On a cycle of x ↦ Ax of length L, f is determined by its value y at
  one point, and going round the cycle forces h^L(y) = y. So the pair fixes
  Π F_h(L) maps, the product over the cycles of A on the N = 2ⁿ input
  vectors, where F_h(L) = #{y : h^L(y) = y} is the sum of the lengths of
  the cycles of h that divide L. Only the cycle lengths of A matter, and
  F_h only through the conjugacy class of h, so a short table of classes of
  the range group is enough:

  | h ∈ AG(3,2) | count | cycles on {0,1}³ | F_h(L) |
  |---|---|---|---|
  | identity | 1 | 1⁸ | 8 |
  | linear-like, order 2 | 42 | 1⁴ 2² | 2^(2+[2∣L]) |
  | linear-like, order 3 | 224 | 1² 3² | 2^(1+2[3∣L]) |
  | linear-like, order 4 | 168 | 1² 2 4 | 2^(1+[2∣L]+[4∣L]) |
  | linear-like, order 7 | 384 | 1 7 | 8^[7∣L] |
  | no fixed point | 49 + 224 + 252 | 2⁴, 2 6, 4² | 0 at L = 1 |

  The last row adds nothing: the zero vector is a cycle of length 1 of
  every linear A, and F_h(1) = 0 for an h without a fixed point. An affine
  map with a fixed point is a linear one moved by a translation, so each
  count is the [A000878](../A000878/) count for GL(3,2) times 8/F_h(1).
  With c cycles of A, and e_d of them of length divisible by d:
  a(n) = Σ_A (8^c + 42·2^(2c+e₂) + 224·2^(c+2e₃) + 168·2^(c+e₂+e₄)
  + 384·8^e₇) / (1344·|GL(n,2)|).
- `i` runs over all 2^(n²) n×n matrices over F₂; its n-bit digits are the
  columns, and `for _ in[m:=[0]]*n:` resets `m` to [0] and doubles it n
  times with `m+=[y^col for y in m]`, so that `m[x]` ends as Ax (the
  [A000585](../A000585/) loop). After each column `len({*m})>>n` is
  computed: 0 until the last column, then 1 exactly when A is invertible.
  `s`, `u`, `v`, `w` and `r` start at that flag, and `k` counts 1344·|GL(n,2)|.
- The walk `while~x:m[x],x=-1,m[x]` marks visited points −1, and `r<<=x<0`
  doubles `r` when a cycle closes, so `r` ends at 2^c. After the column
  loop `i` is 0 (n shifts of n bits), so it is free to serve as the step
  counter: after a fresh cycle of length L it is L + 1 (L marks plus the step
  that reads the −1), and 0 when the start point lies in a finished cycle,
  so `i%2`, `i%3%2`, `i%4==1`, `i%7==1` are the indicators [2|L], [3|L], [4|L], [7|L] (all 0 for
  i = 0); `i=0` resets it.
- `s<<=i%2`, `u<<=i%3%2`, `v<<=i%4==1` and `w<<=i%7==1` make s = 2^e₂,
  u = 2^e₃, v = 2^e₄ and w = 2^e₇ (w keeps the invertibility flag, as its
  term has no factor r). The order-2 and order-4 terms share r·s:
  42·r²s + 168·rsv = 42·rs·(r + 4·v), hence `t+=r*(r*r+42*s*(r+4*v)+224*u*u)+384*w**3`.

**Notes**

- The loop visits all 2^(n²) matrices: a(1)–a(4) print in about 2 s here,
  and a(5) would need 2²⁵ matrices on 32 points (around 20 minutes). The
  bar is these 4 terms in 60 s; the b-file is the OEIS data, 6 terms. A
  sum over the conjugacy classes of GL(n,2) would reach them all but costs
  far more bytes.
- Exact integer arithmetic; correctness rests only on Burnside's lemma. The
  class table was checked by enumerating the whole range group, and a
  brute-force Burnside count over both groups matches a(1)–a(4).
- Adding `t+=…` one matrix late in the column loop, as in
  [A000817](../A000817/), does not pay here: every tracker would need an
  initial value.
- Equivalently, a(n) is A000878's sum with the zero vector's cycle left out
  (each term divided by its F_h(1)), with the GL(3,2) weights; in code that
  means `r>>1` or skipping the first walk, both longer than the weights
  42, 224, 168, 384.
- The other range groups with GL(n,2) on the inputs (m = 2/3 outputs): trivial [A000817](../A000817/)/[A000818](../A000818/), S(m) [A000832](../A000832/)/[A000833](../A000833/), C(2,m) [A000847](../A000847/)/[A000848](../A000848/), GL(m,2) [A000877](../A000877/)/[A000878](../A000878/), AG(m,2) [A000892](../A000892/)/A000893. One output: [A000585](../A000585/) (and [A000613](../A000613/), half of it). Complementing inputs instead: [A000808](../A000808/) and its siblings.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 290 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000893), CC BY-SA 4.0.
