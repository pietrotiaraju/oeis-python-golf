# A000241

> Crossing number of complete graph with n nodes.
> — [OEIS A000241](https://oeis.org/A000241)

Offset 0: 0, 0, 0, 0, 0, 1, 3, 9, 18, 36, 60, 100, 150, 225, 315, …

### Python 3 — 39 bytes

```python
n=2
while[print((n*n-1>>1)**2>>4)]:n-=1
```

**How it works**

- The program prints Hill's formula
  Z(n) = ⌊n/2⌋·⌊(n−1)/2⌋·⌊(n−2)/2⌋·⌊(n−3)/2⌋/4
  ([A028723](https://oeis.org/A028723)), the Harary–Hill conjecture, which
  the OEIS entry now records as proved (see the notes).
- Put p = n − 2. A product of two consecutive floors is a quarter square,
  ⌊k/2⌋·⌈k/2⌉ = ⌊k²/4⌋, so ⌊n/2⌋⌊(n−1)/2⌋ = ⌊(p+1)²/4⌋ and
  ⌊(n−2)/2⌋⌊(n−3)/2⌋ = ⌊(p−1)²/4⌋. Then
  - p odd: 64·Z = (p² − 1)²;
  - p even: 64·Z = p²(p² − 4) = (p² − 2)² − 4.
- `n*n-1>>1` is w = ⌊(p² − 1)/2⌋, that is (p² − 1)/2 for odd p and
  (p² − 2)/2 for even p. So w² = 16·Z for odd p and w² = 16·Z + 1 for even
  p, and `w**2>>4` is Z in both cases.
- Z only depends on p², so the program runs the variable downwards,
  n = 2 − k for the k-th term (p² = (k − 2)²). The first five values
  n = 2, 1, 0, −1, −2 give w = 1, 0, −1, 0, 1 (Python's `>>` floors), so
  w² ≤ 1 and the terms are 0, as they should be for K₀ to K₄.

**Notes**

- Correctness for every n rests on the Harary–Hill theorem. Before 2026
  the formula was known only for n ≤ 12 (Guy for n ≤ 10; Pan and Richter,
  *The crossing number of K₁₁ is 100*, J. Graph Theory 56 (2007), for
  n = 11, 12). The OEIS entry (comment of Oct 27, 2026) cites a proof for
  all n: OpenAI, *The Crossing Number of Complete Graphs*, preprint (2026),
  reported as formalized in Lean, with an exposition by Martin Balko,
  *Proof of the Harary–Hill conjecture: an exposition*, arXiv:2610.34444.
  The b-file (15 terms, up to n = 14) is the bar.
- Longer forms: the product of the two quarter squares
  (`n*n//4*((n+2)**2//4)//4`, n from −3) is 48 bytes; stepping w by
  `w+=p|1` with a separate counter p is 41.
- No constant shift c gives Z = ⌊(p² − c)²/64⌋ for both parities: odd p
  forces c = 1 and even p forces c = 2 (otherwise the error grows like
  p²), hence the parity-dependent `-1>>1`. A search over
  `(n*n+a OP b)**2>>c` (OP in `>> & | ^ // %`) with starts −12..12 and
  steps ±1..±4 found nothing shorter, only same-length variants such as
  `(n*n-1>>3)**2>>4` from n = 4 with `n-=2`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000241), CC BY-SA 4.0.
