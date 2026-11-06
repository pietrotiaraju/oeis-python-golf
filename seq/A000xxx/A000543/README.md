# A000543

> Number of inequivalent ways to color vertices of a cube using at most n colors.
> — [OEIS A000543](https://oeis.org/A000543)

Offset 0: 0, 1, 23, 333, 2916, 16725, 70911, 241913, 701968, 1798281, …

### Python 3 — 47 bytes

```python
n=0
while 1:print(n*n*(n**6+17*n*n+6)//24);n+=1
```

**How it works**

- Burnside's lemma for the 24 rotations of a cube gives the vertex
  cycle index (a₁⁸+9a₂⁴+8a₁²a₃²+6a₄²)/24.
- With n available named colors, every cycle must be monochromatic.
  Substituting n for each cycle variable gives
  (n⁸+17n⁴+6n²)/24=n²(n⁶+17n²+6)/24.
- Reflections are excluded here, as in the OEIS sequence. n=0 has no
  coloring; n=1 has exactly one.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 25 terms from the published OEIS entry; the verification
  bar is 25 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000543), CC BY-SA 4.0.
