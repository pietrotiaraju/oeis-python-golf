# A000869

> Number of switching networks with C(2,n) acting on domain and GL(3,Z2) acting on range.
> — [OEIS A000869](https://oeis.org/A000869)

Offset 1: 4, 27, 14056, 104751025086, 14737381492157353997140846, …

### Python 3 — 84 bytes

```python
m=1
while[print(((x:=4**m)*(x*x+21*x+84*m+56)+(22*x+56)*(2*m-1<<m))//336//m+1)]:m*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to complementing inputs and
  GL(3,2) on the outputs (the OEIS name); brute-force Burnside matches the
  b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- Listing the 168 matrices: the identity (8, 8), 21 involutions (4, 8), 42
  elements of order 4 (2, 4), 56 of order 3 (2, 2), 48 of order 7 (1, 1).
  With x = 2^N and y = 2^(N/2):
  168N·a(n) = x³ + 21x² + 98x + 48 + (N − 1)(22y³ + 42y² + 56y + 48),
  which is Sean A. Irvine's formula on the entry.
- The constants add up to 48N, 2/7 of the divisor: drop them and add 1 after
  the floor. The y² = x term joins the cubic:
  x(x² + 21x + 42N + 56) + (N − 1)·y(22x + 56).
- `m` runs over M = N/2 (so 42N = 84M and the divisor is 336M) because
  (N − 1)·y is then `2*m-1<<m`, a byte under `n-1<<n//2`.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 7392
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 10
  terms (up to a(10)); the bar is the whole b-file.
- The factored cubic x(x + 7)(x + 14) needs the 42(N − 1)x term in the y
  part, 2 bytes longer.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/A000869, AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000869), CC BY-SA 4.0.
