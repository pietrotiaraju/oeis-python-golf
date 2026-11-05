# A000112

> Number of partially ordered sets ("posets") with n unlabeled elements.
> — [OEIS A000112](https://oeis.org/A000112)

Offset 0: 1, 1, 2, 5, 16, 63, 318, 2045, 16999, 183231, 2567284, 46749427, 1104891746, 33823827452, …

There is no formula: the known terms (n ≤ 16) come from Brinkmann and
McKay's computer enumeration ("Posets on up to 16 points", 2002). A short
program can only enumerate and compare up to isomorphism, so it gets a handful
of terms.

### Python 3 — 228 bytes

```python
from itertools import*
n=0;C=combinations
while 1:R=range(n);print(len({min(sum(1<<p[a]*n+p[b]for a,b in P)for p in permutations(R))for k in range(1<<n)for P in C(C(R,2),k)if{(a,c)for a,b in P for x,c in P if b==x}<={*P}}));n+=1
```

**How it works**

- **Natural labellings.** Every finite poset has a linear extension
  (Szpilrajn), so its elements can be numbered 0 … n − 1 with a < b whenever
  a lies below b. In that numbering the order is a set P of pairs (a, b) with
  a < b, and the only condition left is transitivity: antisymmetry comes for
  free. So the program runs over every subset P of the C(n, 2) pairs
  `C(R,2)` and keeps the transitive ones. Each of them is a poset, and every
  poset shows up at least once.
- **Subsets.** `k` runs over `range(1<<n)` and `C(C(R,2),k)` gives the
  subsets of size k. Only k ≤ C(n, 2) matters, and 2ⁿ > C(n, 2) for every n
  (for n = 0 it still lets k = 0 through, which gives the empty poset);
  larger k yield nothing. `combinations` is used twice, so the alias `C`
  saves 7 bytes.
- **Transitivity** as a set inclusion: every composite (a, c) of two pairs
  (a, b), (b, c) must already be in P.
- **Canonical form.** A relabelling p sends the order to the pairs
  (p[a], p[b]), encoded as the integer with bit p[a]·n + p[b] set for each
  pair. The encoding is injective, so the minimum over all n! permutations is
  the same number for isomorphic posets and different numbers for
  non-isomorphic ones. The set of these minima has one element per
  isomorphism class, and its size is a(n).

**Limits**

- For n = 6 the program tries 2¹⁵ = 32 768 subsets, keeps the 4 824
  naturally labelled posets (A006455) and encodes each under 720
  permutations; a(0) … a(6) print in about 3 s. For n = 7 it needs 2²¹
  subsets and 96 428 × 5 040 ≈ 4.9·10⁸ encodings, many minutes, so the bar is
  7 terms in 60 s.
- Exact arithmetic and an exhaustive search: the program is right for every
  n, only slow. The b-file holds the 17 known terms (n = 0 … 16).
- Other shapes tried: the check as `all(b-x or(a,c)in P for a,b in P for
  x,c in P)` (229 bytes); the canonical form as `str(sorted(…))` instead of
  an integer (+5); counting a poset only when it is not in a set D of the
  relabellings seen so far, then adding all of its relabellings (longer, and
  D has n!/|Aut| entries per class). Multiplying the canonical form by the
  `all(…)` check instead of filtering (non-posets give 0, which merges with
  the antichain's 0) is 227 bytes and correct, but it encodes all 2¹⁵
  subsets for n = 6 and needs about 32 s for the 7 terms, too close to the
  bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 228 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000112), CC BY-SA 4.0.
