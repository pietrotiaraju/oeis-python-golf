# A000884

> Number of switching networks with C(2,n) acting on the domain and AG(3,2) acting on the domain.
> — [OEIS A000884](https://oeis.org/A000884)

Offset 1: 2, 10, 2104, 13098898366, 1842172695541070949024622, …

### Python 3 — 87 bytes

```python
m=1
while[print(((v:=4**m//2)*(v*v+21*v+84*m+56)+(23*v+56)*(2*m-1<<m))//336//m+1)]:m*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to complementing inputs and
  affine maps of the outputs, AG(3,2) (the OEIS name says "on the domain"
  twice, but its formula and data are for the outputs); brute-force Burnside
  matches the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- Listing the 1344 maps y ↦ Ay ⊕ b: (8, 8) once, (4, 8) 42 times, (2, 4)
  168, (2, 2) 224, (1, 1) 384, (0, 8) 49, (0, 2) 224, (0, 0) 252. With
  x = 2^N and y = 2^(N/2):
  1344N·a(n) = x³ + 42x² + 392x + 384 + (N − 1)(92y³ + 168y² + 448y + 384),
  which is Sean A. Irvine's formula on the entry.
- The constants add up to 384N, 2/7 of the divisor: dropped, with +1 after
  the floor (as in [A000869](../A000869/)). With v = x/2 = 2^(N−1) the rest
  is 8·[v(v² + 21v + 42N + 56) + (N − 1)·y(23v + 56)], so the divisor
  shrinks to 168N; `m` runs over M = N/2, which makes it 336M with
  (N − 1)·y = `2*m-1<<m`.
- The cubic part in v is the same as A000869's in x.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 7392
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 10
  terms (up to a(10)); the bar is the whole b-file.
- Keeping x is 88 bytes; counting N (`(v:=2**~-n)`, `n-1<<n//2`, divisor
  168N) is also 87.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/A000884. Other entries of Harrison's table take
  S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000884), CC BY-SA 4.0.
