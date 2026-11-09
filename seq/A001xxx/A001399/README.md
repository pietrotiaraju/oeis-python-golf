# A001399

> a(n) is the number of partitions of n into at most 3 parts; also partitions of n+3 in which the greatest part is 3; also number of unlabeled multigraphs with 3 nodes and n edges.
> — [OEIS A001399](https://oeis.org/A001399)

Offset 0: 1, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 19, 21, 24, 27, 30, 33, 37, 40, …

### Python 3 — 34 bytes

```python
n=3
while[print((n*n+6)//12)]:n+=1
```

**How it works**

- a(n) = round((n+3)²/12), the classical count of partitions into at most
  3 parts (generating function 1/((1−x)(1−x²)(1−x³)); see e.g. Andrews,
  *The Theory of Partitions*, or the entry). Squares are 0, 1, 4 or 9
  mod 12, so (n+3)²/12 is never halfway between two integers, and
  rounding is exactly ⌊((n+3)² + 6)/12⌋.
- The loop runs `n` from 3, so `n*n` is already (n+3)² of the sequence's
  index.

**Notes**

- `(n*n|6)//12` also works (n² ≡ 0 or 1 mod 4, and where n ≡ 2 mod 4 the
  missing 4 never crosses a multiple of 12), but is no shorter.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 17502 terms (a(0) to a(17501)); the whole of it prints in
  a fraction of a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001399), CC BY-SA 4.0.
