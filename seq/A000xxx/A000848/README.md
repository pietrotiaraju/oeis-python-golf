# A000848

> Number of n-input 3-output switching networks under action of GL(n,2) on the inputs and complementing group C(3,2) on the outputs.
> — [OEIS A000848](https://oeis.org/A000848)

Offset 1: 8, 120, 16880, 1791651440, 990442962518469863888, …

### Python 3 — 195 bytes

```python
n=1
while 1:
 t=k=r=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^~i%2**n for y in m];i>>=n;t+=r**3;r=len({*m})>>n;k+=8*r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to f ↦ c ⊕ f∘A with
  A ∈ GL(n,2) on the inputs and the complementing group (XOR with a constant
  c ∈ {0,1}³) on the outputs; the OEIS name writes it C(3,2).
- Why it is a plain division by 2^m: a pair (A, c) with c ≠ 0 complementing
  outputs fixes no f at all, because the zero input vector is fixed by every
  linear A, and f(0) = f(0) ⊕ c is impossible. Only c = 0 is left, so
  a(n) = Σ_A 8^c(A) / (8·|GL(n,2)|) = [A000818](../A000818/)(n)/8.
- `i` runs over all 2^(n²) n×n matrices over F₂: its n-bit digits,
  complemented, are the columns, and `for _ in[m:=[0]]*n:` resets `m` to [0]
  and doubles it n times with `m+=[y^col for y in m]`, so that in the end
  `m[x]` is the image Ax of the input vector x (the [A000585](../A000585/)
  loop).
- `len({*m})>>n` is 1 after the last column when the matrix is invertible
  and 0 otherwise (and 0 after every earlier column), so `k` counts
  |GL(n,2)|, times 8, and `r` starts at 0 for a singular matrix.
- The walk `while~x:m[x],x=-1,m[x];r<<=x<0` marks visited points −1 and
  doubles `r` each time a cycle closes, so `r` ends at 2^c(A) for an
  invertible A. `t+=r**3` is added to `t` one matrix late, at the first column
  of the next matrix; the last matrix of each n is the zero matrix (all
  digits 1), whose share is 0 anyway.
- `t//k` is the exact Burnside average.

**Notes**

- The loop visits all 2^(n²) matrices: a(1)–a(4) print in about 2 s
  here, and a(5) would need 2²⁵ matrices on 32 points (around 20 minutes).
  The bar is these 4 terms in 60 s; the b-file is the OEIS data, 6
  terms. A sum over the conjugacy classes of GL(n,2) (rational canonical
  forms, with each class's cycle lengths on F₂ⁿ) would reach them all but
  costs far more bytes.
- Exact integer arithmetic; correctness rests only on Burnside's lemma.
- The program is A000818's with `k+=8*r` for `k+=r`.
- The other range groups with GL(n,2) on the inputs (m = 2/3 outputs): trivial [A000817](../A000817/)/[A000818](../A000818/), S(m) [A000832](../A000832/)/[A000833](../A000833/), C(2,m) [A000847](../A000847/)/A000848, GL(m,2) [A000877](../A000877/)/[A000878](../A000878/), AG(m,2) [A000892](../A000892/)/[A000893](../A000893/). One output: [A000585](../A000585/) (and [A000613](../A000613/), half of it). Complementing inputs instead: [A000808](../A000808/) and its siblings.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 195 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000848), CC BY-SA 4.0.
