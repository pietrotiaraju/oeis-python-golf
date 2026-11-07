# A000824

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000824](https://oeis.org/A000824)

Offset 1: 13, 237, 356026, 2932175712336, 412646680050205587085305856, …

### Python 3 — 67 bytes

```python
m=1
while[print(((w:=4**m+1)**3-w+(2*w-1)*(4*m-2<<m))//12//m)]:m*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to complementing inputs and
  permuting the three outputs (Sean A. Irvine's comment on the entry);
  brute-force Burnside matches the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- H = S(3) on the output bits: the identity has (Fix(h), Fix(h²)) = (8, 8),
  the three transpositions (4, 8), the two 3-cycles (2, 2) (only 000 and
  111). With M = N/2, x = 2^N = 4^M and y = 2^M:
  12M·a(n) = x(x + 1)(x + 2) + (2M − 1)·2y(2x + 1),
  the OEIS formula (b(3,3) + 3b(2,3) + 2b(1,1))/6.
- `m` runs over M = 1, 2, 4, …; w = x + 1 turns the product into w³ − w and
  2x + 1 into 2w − 1, and (2M − 1)·2y is `4*m-2<<m`.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 7394
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 6 terms
  (up to a(6)); the bar is the whole b-file.
- Keeping x (`(x:=4**m)*-~x*(x+2)+(x-~x)*(4*m-2<<m)`) is 69 bytes; counting
  N instead of M costs 2 more (`n-1<<n//2+1`).
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/A000824, C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000824), CC BY-SA 4.0.
