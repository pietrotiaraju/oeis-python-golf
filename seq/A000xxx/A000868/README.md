# A000868

> Number of switching networks with C(2,n) acting on domain and GL(2,Z2) acting on range.
> — [OEIS A000868](https://oeis.org/A000868)

Offset 1: 4, 21, 1531, 44782251, 96076794891512491, …

### Python 3 — 46 bytes

```python
n=2
while[print((2**n+4*n-1<<n)//6//n+1)]:n*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}² up to complementing inputs and
  invertible linear maps of the outputs, GL(2,2) (the OEIS name);
  brute-force Burnside matches the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- GL(2,2) ≅ S(3) permutes the three nonzero outputs and fixes 00: the
  identity (4, 4), three involutions (2, 4), two elements of order 3 (1, 1).
  So
  6N·a(n) = 4^N + 3·2^N + 2 + (N − 1)(4·2^N + 2) = 2^N·(2^N + 4N − 1) + 2N,
  the OEIS formula.
- The lone 2N is a third of the divisor:
  2^N·(2^N + 4N − 1)/(6N) = a(n) − 1/3, so its floor plus one is a(n), 2
  bytes under `+2*n` inside.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 4928
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 10
  terms (up to a(10)); the bar is the whole b-file.
- `|` cannot add the two parts here: at n = 1, 16 and 7·4 share a bit.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  A000868/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000868), CC BY-SA 4.0.
