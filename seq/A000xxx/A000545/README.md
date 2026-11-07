# A000545

> Number of ways of n-coloring a dodecahedron.
> — [OEIS A000545](https://oeis.org/A000545)

Offset 1: 1, 96, 9099, 280832, 4073375, 36292320, 230719293, 1145393152, 4707296613, 16666924000, …

The faces are coloured with at most n colours, and two colourings are the
same when a rotation (not a reflection) carries one to the other.

### Python 3 — 48 bytes

```python
n=1
while[print(n**4*(n**8+15*n*n+44)//60)]:n+=1
```

**How it works**

- **Burnside's lemma.** The 60 rotations of the dodecahedron permute the
  12 faces; a rotation fixes n^(number of face cycles) colourings: the
  identity has 12 cycles (n¹²); the 24 turns about axes through opposite
  face centres fix those two faces and make two 5-cycles (n⁴); the 20
  turns of ±120° about vertex axes make four 3-cycles (n⁴); the 15 half
  turns about edge axes make six 2-cycles (n⁶). So
  a(n) = (n¹² + 15n⁶ + 44n⁴)/60 = n⁴(n⁸ + 15n² + 44)/60.
- **Exactness.** a(n) is a count of orbits, an integer, so `//60` is an
  exact division.
- **The loop.** `print` sits in the loop condition: it returns `None`, and
  `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms:
  `(n**12+15*n**6+44*n**4)//60` in the same loop: 50 bytes;
  `while 1:print(…);n+=1` with the expanded sum: 51.
- Exact integer arithmetic, so the program is right for every n.
- About 2.0 million terms in 60 s here. The b-file has 1000 terms (up to
  a(1000)); the bar is the whole b-file in 60 s, and it prints in well under
  a second.
- a(n) < n¹² for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n > 10^358: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |
| 2026-11-07 | Python 3 | 48 | factor n⁴, print in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000545), CC BY-SA 4.0.
