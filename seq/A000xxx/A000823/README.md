# A000823

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000823](https://oeis.org/A000823)

Offset 1: 7, 46, 4336, 134281216, 288230380379570176, …

### Python 3 — 42 bytes

```python
n=4
while[print((2**n|n-1<<n//2)//n)]:n*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}² up to complementing inputs and
  swapping the two outputs (Sean A. Irvine's comment on the entry);
  brute-force Burnside matches the b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- H = S(2): the identity fixes all 4 outputs, the swap fixes 00 and 11 and
  squares to the identity. So
  a(n) = (4^N + 2^N + 2(N − 1)·2^N)/(2N) = (2^K + (K − 1)·2^(K/2))/K with
  K = 2N.
- That is [A000231](../A000231/) at n + 1: read f as g(x, b) = f(x)_b, a
  Boolean function of n + 1 variables; complementing b swaps the two
  outputs, so the two group actions are the same (the entry says it is
  essentially the same sequence as A000231).
- So the program is A000231's, started at K = 4: `n` runs over K, and
  (K − 1)·2^(K/2) < 2^K, so `|` adds the two parts with no inner
  parentheses.

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 4928
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 7 terms
  (up to a(7)); the bar is the whole b-file.
- Written in N, `(2**n+2*n-1<<n-1)//n` from n = 2 is 43 bytes.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/[A000809](../A000809/), S(m)
  A000823/[A000824](../A000824/), C(2,m)
  [A000838](../A000838/)/[A000839](../A000839/), S(m) with C(2,m)
  [A000853](../A000853/)/[A000854](../A000854/), GL(m,2)
  [A000868](../A000868/)/[A000869](../A000869/), AG(m,2)
  [A000883](../A000883/)/[A000884](../A000884/). Other entries of Harrison's
  table take S(n), B(n), GL(n,2) or AG(n,2) on the inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000823), CC BY-SA 4.0.
