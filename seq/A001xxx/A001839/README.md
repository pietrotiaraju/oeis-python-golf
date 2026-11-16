# A001839

> The coding-theoretic function A(n,4,3).
> — [OEIS A001839](https://oeis.org/A001839)

Offset 1: 0, 0, 1, 1, 2, 4, 7, 8, 12, 13, 17, 20, 26, 28, 35, 37, 44, 48, 57, …

### Python 3 — 43 bytes

```python
n=1
while[print(n*(n-1>>1)//3-n%6//5)]:n+=1
```

**How it works**

- A(n,4,3) is the largest number of weight-3 binary words of length n at
  pairwise distance at least 4, that is, of 3-subsets of an n-set any two of
  which share at most one point: the packing number D(n,3,2), or the most
  edge-disjoint triangles in Kₙ.
- **Upper bound.** A point lies in at most ⌊(n−1)/2⌋ of the triples, since
  its partners in them are disjoint pairs; counting incidences,
  a(n) ≤ ⌊n/3·⌊(n−1)/2⌋⌋. For n ≡ 5 (mod 6) that bound would leave exactly
  one pair uncovered, while every point has an even number of uncovered
  partners (n − 1 is even and each triple through it covers two), so one
  more is lost.
- **Theorem** (Schönheim 1966, Spencer 1968; Theorem 4 of Brouwer, Shearer,
  Sloane and Smith, *IEEE Trans. Inf. Theory* 36 (1990)): these bounds are
  attained for every n, so
  a(n) = ⌊n/3·⌊(n−1)/2⌋⌋ − [n ≡ 5 (mod 6)].
- **Golf.** `n-1>>1` is ⌊(n−1)/2⌋ (a shift binds looser than `-`), and
  `n*m//3` with an integer m is ⌊n/3·m⌋. `n%6//5` is 1 exactly when
  n ≡ 5 (mod 6). The four closed forms per residue class on the OEIS page
  are this one formula.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10000 terms (n = 1 to 10000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001839), CC BY-SA 4.0.
