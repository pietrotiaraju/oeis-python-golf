# A000817

> Number of switching networks under action of GL_n(Z_2) acting on 2 variables.
> — [OEIS A000817](https://oeis.org/A000817)

Offset 1: 16, 80, 1056, 320416, 1858620869536, 16880173675357998942609488800, …

### Python 3 — 192 bytes

```python
n=1
while 1:
 t=k=r=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^~i%2**n for y in m];i>>=n;t+=r*r;r=len({*m})>>n;k+=r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}² (n-input, 2-output switching
  functions) up to f ↦ f∘A with A ∈ GL(n,2), the invertible linear
  substitutions of the inputs; nothing acts on the outputs. Sean A. Irvine's
  check of Harrison's table is this count, and a brute-force Burnside count
  matches the data up to a(4).
- Burnside: A fixes f when f is constant on every cycle of x ↦ Ax on the
  N = 2ⁿ input vectors, with 4 output values per cycle, so
  a(n) = Σ_A 4^c(A) / |GL(n,2)|, c(A) being the number of cycles (the zero
  vector is always one of them).
- `i` runs over all 2^(n²) n×n matrices over F₂: its n-bit digits,
  complemented, are the columns, and `for _ in[m:=[0]]*n:` resets `m` to [0]
  and doubles it n times with `m+=[y^col for y in m]`, so that in the end
  `m[x]` is the image Ax of the input vector x (the [A000585](../A000585/)
  loop).
- `len({*m})>>n` is 1 after the last column when the matrix is invertible
  and 0 otherwise (and 0 after every earlier column), so `k` counts
  |GL(n,2)| and `r` starts at 0 for a singular matrix.
- The walk `while~x:m[x],x=-1,m[x];r<<=x<0` marks visited points −1 and
  doubles `r` each time a cycle closes, so `r` ends at 2^c(A) for an
  invertible A. `t+=r*r` is added to `t` one matrix late, at the first column
  of the next matrix; the last matrix of each n is the zero matrix (all
  digits 1), whose share is 0 anyway.
- `t=k=r=0` starts every n afresh; `t//k` is the exact Burnside average.

**Notes**

- The loop visits all 2^(n²) matrices: a(1)–a(4) print in about 1 s
  here, and a(5) would need 2²⁵ matrices on 32 points (around 20 minutes).
  The bar is these 4 terms in 60 s; the b-file is the OEIS data, 7
  terms. A sum over the conjugacy classes of GL(n,2) (rational canonical
  forms, with each class's cycle lengths on F₂ⁿ) would reach them all but
  costs far more bytes.
- Exact integer arithmetic; correctness rests only on Burnside's lemma.
- With 3 outputs ([A000818](../A000818/)) the only change is `r**3` for
  `r*r`.
- The other range groups with GL(n,2) on the inputs (m = 2/3 outputs): trivial A000817/[A000818](../A000818/), S(m) [A000832](../A000832/)/[A000833](../A000833/), C(2,m) [A000847](../A000847/)/[A000848](../A000848/), GL(m,2) [A000877](../A000877/)/[A000878](../A000878/), AG(m,2) [A000892](../A000892/)/[A000893](../A000893/). One output: [A000585](../A000585/) (and [A000613](../A000613/), half of it). Complementing inputs instead: [A000808](../A000808/) and its siblings.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 192 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000817), CC BY-SA 4.0.
