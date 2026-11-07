# A000854

> Number of n-input 3-output switching networks under action of complementing group C(2,n) on inputs and S(3) and C(2,3) on outputs.
> — [OEIS A000854](https://oeis.org/A000854)

Offset 1: 4, 51, 46218, 366543984720, 51580835042395388382652416, …

### Python 3 — 69 bytes

```python
m=1
while[print(((w:=4**m+2)**3-4*w+(5*w-6)*(8*m-4<<m))//96//m)]:m*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to complementing inputs and
  permuting and complementing the three outputs (the OEIS name):
  h(y) = Py ⊕ d, 48 maps; brute-force Burnside matches the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- Listing the 48 maps gives (Fix(h), Fix(h²)) = (8, 8) once, (4, 8) 6 times,
  (2, 2) 8, (0, 8) 13, (0, 2) 8 and (0, 0) 12. With M = N/2, x = 4^M and
  y = 2^M:
  96M·a(n) = x(x + 2)(x + 4) + (2M − 1)·4y(5x + 4),
  the OEIS formula.
- w = x + 2 turns the product into w³ − 4w and 5x + 4 into 5w − 6;
  (2M − 1)·4y is `8*m-4<<m`.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 7393
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 10
  terms (up to a(10)); the bar is the whole b-file.
- Keeping x is 72 bytes; counting N with w = 2^(N−1) + 1
  (`(w:=2**~-n+1)**3-w+(5*w-3)*(n-1<<n//2)`, over 6N) is also 69.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/A000854, GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000854), CC BY-SA 4.0.
