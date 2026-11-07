# A000409

> Singular n X n (0,1)-matrices: the number of n X n (0,1)-matrices having distinct, nonzero ordered rows, but having at least two equal columns or at least one zero column.
> — [OEIS A000409](https://oeis.org/A000409)

Offset 2: 0, 6, 350, 43260, 14591171, 14657461469, 46173502811223, 474928141312623525, 16489412944755088235117, 1985178211854071817861662307, …

"Ordered" means the rows are taken up to order: a(n) counts sets of n
distinct nonzero vectors in {0,1}ⁿ whose matrix has a zero column or two
equal columns (a lower bound for [A000410](../A000410/)).

### Python 3 — 129 bytes

```python
import math
s=[1,-1];n=1
while 1:n+=1;s=[a-n*b for a,b in zip([0]+s,s+[0])];print(sum(s[k]*math.comb(2**k-1,n)for k in range(n)))
```

**How it works**

- The formula is the entry's a(n) = −Σ_{k=0}^{n−1} s(n+1, k+1)·C(2ᵏ − 1, n),
  s the signed Stirling numbers of the first kind. Derivation: add a
  phantom zero column to the n columns. The pattern of equal columns
  among these n + 1 is a set partition of them, and the row sets whose
  columns are equal at least within the blocks of a partition σ with
  k + 1 blocks number C(2ᵏ − 1, n) (the phantom's block is 0, the other k
  blocks are free coordinates, and the n rows are distinct and nonzero).
  Möbius inversion on the partition lattice, where the Möbius values of
  the partitions with k + 1 blocks add up to s(n+1, k+1), counts the row
  sets with all columns distinct and nonzero:
  Σ_{k=0}^{n} s(n+1, k+1)·C(2ᵏ − 1, n). The k = n term is C(2ⁿ − 1, n), all
  row sets, and a(n) is the rest with the sign flipped.
- `s` holds the row negated: s[k] = −s(n+1, k+1), so the printed sum needs
  no minus sign. s(n+1, j) = s(n, j−1) − n·s(n, j) becomes
  `s=[a-n*b for a,b in zip([0]+s,s+[0])]`, the two zero pads standing for
  s(n, 0) = 0 and the entry past the end. The start `s=[1,-1]` is
  −(s(2, 1), s(2, 2)) for n = 1, and the first pass prints a(2).
- `math.comb(2**k-1,n)` is 0 while 2ᵏ − 1 < n, so small k need no special
  case; `import math` plus `math.comb` once is a byte under
  `from math import*`.

**Notes**

- Printing in the header (`while[print(…)]:`, start `s=[2,-3,1];n=2`)
  costs 2 bytes more, and the row update
  `[0]+[s[k-1]-n*s[k]for k in range(1,n+1)]+[1]` is 8 bytes longer than
  the `zip`.
- Exact integer arithmetic; correctness for every n rests on the
  inversion above. A brute-force count over all row sets agrees for
  n ≤ 4.
- The b-file has 14 terms (up to a(15)) and prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(123) is the first term with more than 4300 digits, so printing stops
  there, after about 0.7 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |
| 2026-11-06 | Python 3 | 144 | import math and start the coefficients as a tuple |
| 2026-11-07 | Python 3 | 129 | negated Stirling row by zip, print after the update |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000409), CC BY-SA 4.0.
