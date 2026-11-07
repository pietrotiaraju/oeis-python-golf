# A000853

> Number of n-input 2-output switching networks under action of complementing group C(2,n) on inputs and S(2) and C(2,2) on outputs.
> — [OEIS A000853](https://oeis.org/A000853)

Offset 1: 3, 18, 1200, 33601536, 72057597192044544, …

### Python 3 — 44 bytes

```python
n=2
while[print((2**n+6*n-4<<n)//n>>3)]:n*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}² up to complementing inputs and
  permuting and complementing the two outputs (the OEIS name),
  h(y) = Py ⊕ d; brute-force Burnside matches the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- The 8 maps h: the identity (4, 4); the 3 complements (0, 4); the swap, and
  the swap followed by complementing both outputs (2, 4); the swap with one
  output complemented (0, 0), since its square complements both. So
  8N·a(n) = 4^N + 6(N − 1)·2^N + 2·2^N = 2^N·(2^N + 6N − 4), the OEIS
  formula.
- `2**n+6*n-4<<n` is that product; `//n>>3` divides by N and by 8.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 4928
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 10
  terms (up to a(10)); the bar is the whole b-file.
- Halving inside, `(2**~-n+3*n-2<<n-2)//n`, is 45 bytes.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  A000853/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000853), CC BY-SA 4.0.
