# A000358

> Number of binary necklaces of length n with no subsequence 00, excluding
> the necklace "0".
> — [OEIS A000358](https://oeis.org/A000358)

Offset 1: 1, 2, 2, 3, 3, 5, 5, 8, 10, 15, 19, 31, 41, 64, 94, 143, …

### Python 3 — 99 bytes

```python
import math
l=[2,n:=1]
while[print(sum(l[math.gcd(j,n)]for j in range(n))//n)]:n+=1;l+=l[-1]+l[-2],
```

**How it works**

- Burnside's lemma over the n rotations, as in [A000031](../A000031/):
  rotating by j splits the n positions into gcd(j, n) cycles of equal
  length, so a word fixed by it is a word of length g = gcd(j, n) repeated,
  and it has no cyclic 00 exactly when that short word has none,
  read cyclically.
- The cyclic binary words of length g ≥ 1 with no 00 are counted by the
  Lucas number L(g) (1, 3, 4, 7, 11, …): a 0 must be followed by a 1, which
  gives the transfer matrix [[1, 1], [1, 0]], and L(g) is the trace of its
  g-th power. So a(n) = (1/n) Σ_{j=0}^{n−1} L(gcd(j, n)), the formula on
  the OEIS page.
- At length 1 the word "0" is next to itself, so L(1) = 1 counts only "1":
  the necklace "0" is excluded by the same rule, with no special case.
- `l` holds L(0), L(1), …, L(n): `l=[2,n:=1]` sets L(0) = 2, L(1) = 1 and
  the counter n = 1 at once, and each pass appends L(n + 1) = L(n) + L(n − 1).

**Notes**

- Exact integers; the division by n is exact by Burnside's lemma.
- `from math import*` with `gcd` is 1 byte longer. Growing the list from
  a `for x in l:` loop (`l+=x+l[-1],`) is also 99 bytes.
- Brute force over the 2ⁿ words, keeping those minimal among their
  rotations with no 00 in the doubled word, is 120 bytes and more and
  exponential.
- The whole b-file (1000 terms) prints in under a second; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 99 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000358), CC BY-SA 4.0.
