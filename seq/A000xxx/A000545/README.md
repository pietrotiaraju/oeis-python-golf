# A000545

> Number of ways of n-coloring a dodecahedron.
> — [OEIS A000545](https://oeis.org/A000545)

Offset 1: 1, 96, 9099, 280832, 4073375, 36292320, 230719293, 1145393152, 4707296613, 16666924000, …

### Python 3 — 51 bytes

```python
n=1
while 1:print((n**12+15*n**6+44*n**4)//60);n+=1
```

**How it works**

- Rotations act on the twelve faces of the dodecahedron. Their cycle
  counts give n¹² for the identity, 15n⁶ for the half-turns, and
  (20+24)n⁴ for the rotations of orders 3 and 5.
- Burnside's lemma divides their sum by the group order 60, giving
  (n¹²+15n⁶+44n⁴)/60.
- Colors are named and may be unused; only rotations identify colorings.
  This gives one coloring at the stated offset n=1.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 1000 terms from the OEIS b-file; the verification
  bar is 1000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000545), CC BY-SA 4.0.
