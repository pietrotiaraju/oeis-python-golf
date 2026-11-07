# A000809

> Number of switching networks (see Harrison reference for precise definition).
> — [OEIS A000809](https://oeis.org/A000809)

Offset 1: 36, 1072, 2100736, 17592201773056, 2475880078571033228681936896, …

### Python 3 — 42 bytes

```python
j=6
while[print((3<<j|j-3<<j//2)//j)]:j*=2
```

**How it works**

- What it counts: maps f: {0,1}ⁿ → {0,1}³ up to complementing inputs, with
  nothing acting on the outputs (the 3-output twin of
  [A000808](../A000808/)). The OEIS name only points to Harrison; Sean A.
  Irvine's formula on the entry is this count, and brute-force Burnside
  matches the whole b-file.
- Burnside over the pairs (c, h): with N = 2ⁿ inputs, c ∈ C(2,n) acts by
  x ↦ x ⊕ c and h runs over the range group H. A pair fixes f when
  h(f(x ⊕ c)) = f(x) for every x. For c = 0 that is h∘f = f: Fix(h)^N
  functions, Fix(h) being the number of outputs h fixes. For c ≠ 0 the
  inputs fall into N/2 pairs {x, x ⊕ c}; on a pair, f(x ⊕ c) must be a point
  fixed by h², and then f(x) = h(f(x ⊕ c)): Fix(h²)^(N/2) functions. So
  a(n) = Σ_h [Fix(h)^N + (N − 1)·Fix(h²)^(N/2)] / (N·|H|).
- H is trivial and Fix = 8: a(n) = (8^N + (N − 1)·8^(N/2))/N.
- Put j = 3N (6, 12, 24, …): 8^N = 2^j, 8^(N/2) = 2^(j/2) and N = j/3, so
  a(n) = (3·2^j + (j − 3)·2^(j/2))/j: the three constants fold into the loop
  variable.
- (j − 3)·2^(j/2) < 2^j, so its bits sit below those of `3<<j` and `|` adds
  the two parts with no inner parentheses (`|` binds looser than `<<` and
  `-`).

**Notes**

- Exact integer arithmetic and Burnside's lemma, so every term is right;
  each term costs a few big-integer operations. All 12 terms up to a(12)
  print at once, then the program stops with a `ValueError`: a(13) has 7395
  digits, past CPython's 4300-digit int-to-str limit. The b-file has 9 terms
  (up to a(9)); the bar is the whole b-file.
- With M = N/2 as the counter, `(8**m+m+m-1<<3*m-1)//m` is 45 bytes.
- The same domain group with the other range groups (m = 2/3): trivial
  [A000808](../A000808/)/A000809, S(m)
  [A000823](../A000823/)/[A000824](../A000824/), C(2,m)
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
Sequences](https://oeis.org/A000809), CC BY-SA 4.0.
