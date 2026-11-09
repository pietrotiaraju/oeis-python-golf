# A001294

> Triangle in which k-th number (0<=k<=n) in n-th row (0<=n) is number of dodecads in Golay code G_24 containing k given points and missing n-k given points.
> — [OEIS A001294](https://oeis.org/A001294)

Offset 0: 2576, 1288, 1288, 616, 672, 616, 280, 336, 336, 280, 120, 160, 176, 160, 120, 48, 72, 88, 88, 72, 48, 16, 32, 40, 48, 40, 32, 16, 0, 16, 16, 24, 24, 16, 16, 0, 0, 0, 16, 0, 24, 0, 16, 0, 0

A finite triangle with rows n = 0 … 8. The given points are n points of one
octad: rows 0–5 are the same for any n points (the dodecads form a 5-design),
and row 8 is that of an octad, which a dodecad meets in 2, 4 or 6 points.

### Python 3 — 148 bytes

```python
C={0};L={}
for i in range(12):C|={c^6378<<i^1for c in C};L[76377%4**i]=0
[b>a or print(sum(c&a^b==12-c.bit_count()for c in C))for a in L for b in L]
```

**How it works**

- The code: the cyclic Golay code of length 23 is the set of multiples
  m(x)·g(x), deg m < 12, of g(x) = x¹¹ + x¹⁰ + x⁶ + x⁵ + x⁴ + x² + 1 (binary
  110001110101 = 3189), and an overall parity bit makes it the extended
  Golay code G₂₄ (unique up to equivalence). A word is a 24-bit integer: bit 0 is the parity point and
  bits 1–23 hold x⁰ … x²². Row `6378<<i^1` is xⁱ·g(x) moved up one place
  plus the parity bit, which is 1 because g has weight 7. Closing `C` under
  adding each row makes it their span: 4096 words, of weights 0, 8, 12, 16,
  24 (1, 759, 2576, 759, 1 words). The 2576 words of weight
  12 are the dodecads.
- The given points are those of the octad O = 76377 = {0, 3, 4, 6, 9, 11,
  13, 16}. Each pair of bits 2j, 2j + 1 holds at most one point of O, so the
  masks O mod 4ⁱ, i = 0 … 11, are its 9 prefixes (its first n points, n = 0 …
  8), some of them repeated; the dict `L` keeps each once, in increasing
  order.
- Row a (first n points), entry b (first k points; b ≤ a means k ≤ n)
  counts the words c with c AND a = b, which contain the k points and miss
  the other n − k, and have weight 12. `c&a^b==12-c.bit_count()` tests
  both: the right side is negative for weights 16 and 24, and for weights 0
  and 8 it is 12 = {2, 3} or 4 = {2}, which contain point 2, not in O,
  while the left side is a subset of O. For weight 12 it asks c AND a = b.
- Any octad and any choice of the points give the same numbers: M₂₄ is
  transitive on octads and maps dodecads to dodecads, and the stabilizer of
  an octad acts on it as A₈, which is transitive on the pairs (k-set ⊂
  n-set) inside it.

**Notes**

- Same program as [A001293](../A001293/) (octads) but for the weight; there
  `8-c.bit_count()` works with the same octad because 8 = {3} is not a
  prefix. The first version, with a sorted list of prefixes of the octad
  6379 and `c.bit_count()==12`, was 169 bytes.
- Exact integers. The b-file is synthesized from the 45 entries, the whole
  triangle; it prints in about 0.1 s, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 148 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001294), CC BY-SA 4.0.
