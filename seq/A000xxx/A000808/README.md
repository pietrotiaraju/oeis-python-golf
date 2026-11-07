# A000808

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000808](https://oeis.org/A000808)

Offset 1: 10, 76, 8416, 268496896, 576460756464173056, …

### Python 3 — 39 bytes

```python
n=2
while[print((2**n+n-1<<n)//n)]:n*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}² (n-input, 2-output switching
  functions) up to complementing inputs, f ↦ f∘(x ↦ x ⊕ c), with nothing
  acting on the outputs. The OEIS name only points to Harrison; Sean A.
  Irvine's formula on the entry is this count (a(1) = (16 + 4)/2 = 10), and
  a brute-force Burnside count matches the whole b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- Here H is trivial and Fix = 4, so
  a(n) = (4^N + (N − 1)·4^(N/2))/N = 2^N·(2^N + N − 1)/N, the formula on the
  OEIS page.
- `n` runs over N = 2, 4, 8, …; `2**n+n-1<<n` is (2^N + N − 1)·2^N, since
  `<<` binds looser than `+` and `-`, and `//n` is exact.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 4929
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 12
  terms (up to a(12)); the bar is the whole b-file.
- `(4**n|n-1<<n)//n` (the two parts have disjoint bits, as in
  [A000231](../A000231/)) is also 39 bytes.
- The same domain group with the other range groups (m = 2/3): trivial
  A000808/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000808), CC BY-SA 4.0.
