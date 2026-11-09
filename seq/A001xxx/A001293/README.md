# A001293

> Leech triangle: k-th number (0 <= k <= n) in n-th row (0 <= n) is number of octads in S(5,8,24) containing k given points and missing n-k given points.
> — [OEIS A001293](https://oeis.org/A001293)

Offset 0: 759, 506, 253, 330, 176, 77, 210, 120, 56, 21, 130, 80, 40, 16, 5, 78, 52, 28, 12, 4, 1, 46, 32, 20, 8, 4, 0, 1, 30, 16, 16, 4, 4, 0, 0, 1, 30, 0, 16, 0, 4, 0, 0, 0, 1

A finite triangle with rows n = 0 … 8. The given points are n points of one
octad: rows 0–5 are the same for any n points (S(5,8,24) is a 5-design),
and rows 6–8 are those of points inside an octad (row 8 counts the octads
meeting a fixed octad in exactly a given set of 0, 2, 4 or 8 of its points).

### Python 3 — 147 bytes

```python
C={0};L={}
for i in range(12):C|={c^6378<<i^1for c in C};L[76377%4**i]=0
[b>a or print(sum(c&a^b==8-c.bit_count()for c in C))for a in L for b in L]
```

**How it works**

- The code: the cyclic Golay code of length 23 is the set of multiples
  m(x)·g(x), deg m < 12, of g(x) = x¹¹ + x¹⁰ + x⁶ + x⁵ + x⁴ + x² + 1 (binary
  110001110101 = 3189), and an overall parity bit makes it the extended
  Golay code [24, 12, 8]. A word is a 24-bit integer: bit 0 is the parity point and
  bits 1–23 hold x⁰ … x²². Row `6378<<i^1` is xⁱ·g(x) moved up one place
  plus the parity bit, which is 1 because g has weight 7. Closing `C` under
  adding each row makes it their span: 4096 words, of weights 0, 8, 12, 16,
  24 (1, 759, 2576, 759, 1 words). The 759 octads, the words of weight 8, are
  the blocks of S(5,8,24), which is unique up to isomorphism (Witt).
- The given points are those of the octad O = 76377 = {0, 3, 4, 6, 9, 11,
  13, 16}. Each pair of bits 2j, 2j + 1 holds at most one point of O, so the
  masks O mod 4ⁱ, i = 0 … 11, are its 9 prefixes (its first n points, n = 0 …
  8), some of them repeated; the dict `L` keeps each once, in increasing
  order.
- Row a (first n points), entry b (first k points; b ≤ a means k ≤ n)
  counts the words c with c AND a = b, which contain the k points and miss
  the other n − k, and have weight 8. `c&a^b==8-c.bit_count()` tests both:
  the right side is negative for weights 12, 16 and 24, and for weight 8 it
  asks c AND a = b. For c = 0 it would ask b = 8, the set {3}, which is not
  a prefix of O.
- Any octad and any choice of the points give the same numbers: M₂₄ is
  transitive on octads, and the stabilizer of an octad acts on it as A₈,
  which is transitive on the pairs (k-set ⊂ n-set) inside it.

**Notes**

- The first version, a sorted list of prefixes of the octad 6379 (the first
  row of the code) and the test `c.bit_count()==8`, was 168 bytes. The dict
  `L` filled in the code's own loop needs an octad whose prefixes come out of
  12 masks: with 6379 and `2**i` the loop has to run to i = 13
  (`6378<<i%12`), 149 bytes.
- Exact integers. The b-file is synthesized from the 45 entries, the whole
  triangle; it prints in about 0.1 s, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001293), CC BY-SA 4.0.
