# A001295

> Triangle in which k-th number (0<=k<=n) in n-th row (0<=n) is number of hexads in S(5,6,12) containing k given points and missing n-k given points.
> — [OEIS A001295](https://oeis.org/A001295)

Offset 0: 132, 66, 66, 30, 36, 30, 12, 18, 18, 12, 4, 8, 10, 8, 4, 1, 3, 5, 5, 3, 1, 1, 0, 3, 2, 3, 0, 1

A finite triangle with rows n = 0 … 6. The given points are n points of one
hexad: rows 0–5 are the same for any n points (S(5,6,12) is a 5-design),
and row 6 counts the hexads meeting a fixed hexad in exactly a given set of
0, 2, 3, 4 or 6 of its points.

### Python 3 — 154 bytes

```python
C={0};L={}
for i in range(12):C|={c^6378<<i^1for c in C};L[95%2**i]=0
[b>a or print(sum(c&a^b|(c&916384).bit_count()^2<1for c in C))for a in L for b in L]
```

**How it works**

- The code: the cyclic Golay code of length 23 is the set of multiples
  m(x)·g(x), deg m < 12, of g(x) = x¹¹ + x¹⁰ + x⁶ + x⁵ + x⁴ + x² + 1 (binary
  110001110101 = 3189), and an overall parity bit makes it the extended
  Golay code [24, 12, 8]. A word is a 24-bit integer: bit 0 is the parity point and
  bits 1–23 hold x⁰ … x²². Row `6378<<i^1` is xⁱ·g(x) moved up one place
  plus the parity bit, which is 1 because g has weight 7. Closing `C` under
  adding each row makes it their span: 4096 words, of weights 0, 8, 12, 16,
  24 (1, 759, 2576, 759, 1 words).
- The hexads, from the code: E = 916384 = {5, 7, 8, 9, 11, 12, 13, 14, 15,
  16, 18, 19} is a dodecad, and so is the set D of the other 12 points. An
  octad meets a dodecad in 2, 4 or 6 points, and any 5 points of D lie in
  exactly one octad, which therefore meets D in 6 points: the 132 octads with
  6 points in D cut out on D the hexads of S(5,6,12) (unique up to
  isomorphism, Witt).
- These octads are exactly the codewords with 2 points in E: a dodecad
  meets E in 0, 4, 6, 8 or 12 points, the complement of an octad in 6, 8 or
  10, the words 0 and all-ones in 0 and 12. So `(c&916384).bit_count()^2` is
  0 exactly for them.
- The given points are those of the hexad H = 95 = {0, 1, 2, 3, 4, 6}, the
  part in D of the octad {0, 1, 2, 3, 4, 6, 15, 18}. The masks H mod 2ⁱ, i =
  0 … 11, are its 7 prefixes (first n points, n = 0 … 6), with repeats; the
  dict `L` keeps each once, in increasing order.
- Row a (first n points), entry b (first k points; b ≤ a means k ≤ n)
  counts the octads c of the system with c AND a = b: a ⊆ D, so this says
  that the hexad of c contains the k points and misses the other n − k.
  `c&a^b|…^2<1` is that test and the one above together.
- Any hexad and any choice of the points give the same numbers: M₁₂ is
  transitive on hexads, and the stabilizer of a hexad acts on it as S₆.

**Notes**

- The first version, with a sorted list of prefixes and the same tests, was
  177 bytes. Folding the two tests into one comparison
  (`c&a^b==2-(c&E).bit_count()`) needs a hexad without point 1 and longer
  constants (469 and 982538), so it is no shorter.
- Exact integers. The b-file is synthesized from the 28 entries, the whole
  triangle; it prints in about 0.1 s, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 154 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001295), CC BY-SA 4.0.
