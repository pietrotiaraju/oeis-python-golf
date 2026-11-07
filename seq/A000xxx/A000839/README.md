# A000839

> Number of n-input 3-output switching networks under action of complementing group on the inputs and outputs.
> — [OEIS A000839](https://oeis.org/A000839)

Offset 1: 8, 176, 265728, 2199038984192, 309485009821617747608469504, …

### Python 3 — 47 bytes

```python
m=1
while[print((8**~-m+2*m-1<<3*m-1)//m)]:m*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to complementing inputs and
  complementing each output (the OEIS name); brute-force Burnside matches
  the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- H = C(2,3): the identity fixes all 8 outputs, the 7 other translations
  none, and every element squares to the identity. So
  8N·a(n) = 8^N + 8(N − 1)·8^(N/2); with M = N/2,
  a(n) = 8^M·(8^(M−1) + 2M − 1)/(2M), the closed formula on the entry.
- `m` runs over M; `8**~-m+2*m-1<<3*m-1` is (8^(M−1) + 2M − 1)·2^(3M−1), and
  `//m` finishes the division by 2M.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 7394
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 6 terms
  (up to a(6)); the bar is the whole b-file.
- `(8**m+16*m-8<<3*m)//m>>4` is also 47 bytes. The j = 3N substitution of
  [A000809](../A000809/) needs a `+` here (the two parts overlap at n = 1:
  4 + 4) and comes out longer.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/A000839, S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000839), CC BY-SA 4.0.
