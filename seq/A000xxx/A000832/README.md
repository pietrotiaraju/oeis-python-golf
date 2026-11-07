# A000832

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000832](https://oeis.org/A000832)

Offset 1: 10, 46, 556, 160948, 929312039044, 8440086837679170219118159556, …

### Python 3 — 217 bytes

```python
n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n;s=r=len({*m})>>n;k+=2*r
  for x in m:
   while~x:m[x],x=-1,m[x];i^=1;r<<=x<0
   s<<=i;i=0
  t+=r*(r+s)
 print(t//k);n+=1
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}² (n-input, 2-output switching
  functions) up to f ↦ h∘f∘A, with A ∈ GL(n,2) (invertible linear
  substitutions of the inputs) and h ∈ S(2) (swapping the two outputs). The
  OEIS name only points to Harrison; Sean A. Irvine's comment on the entry
  names the two groups.
- Burnside over the pairs (A, h): (A, h) fixes f when f(Ax) = h(f(x)) for
  every x. On a cycle of x ↦ Ax of length L, f is determined by its value y at
  one point, and going round the cycle forces h^L(y) = y. So the pair fixes
  Π F_h(L) maps, the product over the cycles of A on the N = 2ⁿ input
  vectors, where F_h(L) = #{y : h^L(y) = y} is the sum of the lengths of
  the cycles of h that divide L. Only the cycle lengths of A matter, and
  F_h only through the conjugacy class of h, so a short table of classes of
  the range group is enough:

  | h ∈ S(2) | count | cycles on {0,1}² | F_h(L) |
  |---|---|---|---|
  | identity | 1 | 1 1 1 1 | 4 |
  | swap | 1 | 1 1 2 | 2 + 2·[2∣L] = 2^(1+[2∣L]) |

  With c cycles of A, e₂ of them of even length:
  a(n) = Σ_A (4^c + 2^(c+e₂)) / (2·|GL(n,2)|).
- `i` runs over all 2^(n²) n×n matrices over F₂; its n-bit digits are the
  columns, and `for _ in[m:=[0]]*n:` resets `m` to [0] and doubles it n
  times with `m+=[y^col for y in m]`, so that `m[x]` ends as Ax (the
  [A000585](../A000585/) loop). After each column `len({*m})>>n` is
  computed: 0 until the last column, then 1 exactly when A is invertible.
  `s` and `r` start at that flag, and `k` counts 2·|GL(n,2)|.
- The walk `while~x:m[x],x=-1,m[x]` marks visited points −1, and `r<<=x<0`
  doubles `r` when a cycle closes, so `r` ends at 2^c. After the column
  loop `i` is 0 (n shifts of n bits), so it is free to serve as the step
  counter: `i^=1` at each step leaves i = (L+1) mod 2 after a cycle of length L
  (L + 1 steps, the last one reading the −1), that is 1 exactly when L is
  even, so `s<<=i` makes s = 2^e₂, e₂ = number of cycles of even length;
  `i=0` resets it, and a start point inside a finished cycle takes no step.
- `t+=r*(r+s)` adds 4^c + 2^(c+e₂), and 0 for a singular matrix.

**Notes**

- The loop visits all 2^(n²) matrices: a(1)–a(4) print in about 2 s here,
  and a(5) would need 2²⁵ matrices on 32 points (around 20 minutes). The
  bar is these 4 terms in 60 s; the b-file is the OEIS data, 7 terms. A
  sum over the conjugacy classes of GL(n,2) would reach them all but costs
  far more bytes.
- Exact integer arithmetic; correctness rests only on Burnside's lemma. The
  class table was checked by enumerating the whole range group, and a
  brute-force Burnside count over both groups matches a(1)–a(4).
- Adding `t+=…` one matrix late in the column loop, as in
  [A000817](../A000817/), does not pay here: every tracker would need an
  initial value.
- With 3 outputs ([A000833](../A000833/)) the 3-cycles of S(3) need
  [3|L] as well, so the counter counts instead of toggling.
- The other range groups with GL(n,2) on the inputs (m = 2/3 outputs): trivial [A000817](../A000817/)/[A000818](../A000818/), S(m) A000832/[A000833](../A000833/), C(2,m) [A000847](../A000847/)/[A000848](../A000848/), GL(m,2) [A000877](../A000877/)/[A000878](../A000878/), AG(m,2) [A000892](../A000892/)/[A000893](../A000893/). One output: [A000585](../A000585/) (and [A000613](../A000613/), half of it). Complementing inputs instead: [A000808](../A000808/) and its siblings.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 217 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000832), CC BY-SA 4.0.
