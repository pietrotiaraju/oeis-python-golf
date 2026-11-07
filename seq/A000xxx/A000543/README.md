# A000543

> Number of inequivalent ways to color vertices of a cube using at most n colors.
> — [OEIS A000543](https://oeis.org/A000543)

Offset 0: 0, 1, 23, 333, 2916, 16725, 70911, 241913, 701968, 1798281, …

Two colourings are the same when a rotation of the cube (not a
reflection) carries one to the other.

### Python 3 — 46 bytes

```python
n=0
while[print(n*n*(n**6+17*n*n+6)//24)]:n+=1
```

**How it works**

- **Burnside's lemma.** The 24 rotations of the cube permute the 8
  vertices; a colouring is fixed by a rotation when each vertex cycle has
  one colour, so the rotation contributes n^(number of cycles):
  the identity has 8 cycles (n⁸); the 6 quarter turns about face axes have
  two 4-cycles (n²); the 3 half turns about face axes, the 8 turns of
  ±120° about vertex diagonals (two fixed vertices and two 3-cycles) and
  the 6 half turns about edge axes all have 4 cycles (17n⁴). So
  a(n) = (n⁸ + 17n⁴ + 6n²)/24 = n²(n⁶ + 17n² + 6)/24.
- **Exactness.** a(n) is a count of orbits, an integer, so `//24` is an
  exact division.
- **The loop.** `print` sits in the loop condition: it returns `None`, and
  `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: counting down with `n-=1`
  (the polynomial is even): also 46 bytes; the expanded numerator
  `(n**8+17*n**4+6*n*n)//24` and `while 1:print(…);n+=1`: 47 each.
- Exact integer arithmetic, so the program is right for every n.
- About 1.9 million terms in 60 s here. The b-file has 25 terms (up to a(24));
  the bar is the whole b-file in 60 s, and it prints at once.
- a(n) < n⁸ for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n > 10^537: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 47 | first entry |
| 2026-11-07 | Python 3 | 46 | print in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000543), CC BY-SA 4.0.
