# A000903

> Number of inequivalent ways of placing n nonattacking rooks on n X n board up to rotations and reflections of the board.
> — [OEIS A000903](https://oeis.org/A000903)

Offset 0: 1, 1, 1, 2, 7, 23, 115, 694, 5282, 46066, 456454, 4999004, 59916028, …

### Python 3 — 97 bytes

```python
n=0;f=C=1;c=d=p=q=2
while[print(f+C+q+d+7>>3)]:
 if n%2:C*=n+1;p,q=q,~-n*p
 c,d=d,d+n*c;n+=1;f*=n
```

**The formula**

Burnside's lemma over D₄ (8 symmetries of the board) acting on the n!
solutions, i.e. permutation matrices:

- identity: n! solutions;
- half turn: C(n) = 2ᵏ·k!, k = ⌊n/2⌋ ([A037223](https://oeis.org/A037223)),
  the permutations that commute with i ↦ n+1−i;
- the two quarter turns: R(n) each ([A037224](https://oeis.org/A037224)),
  (2m)!/m! for n = 4m or 4m+1 and 0 otherwise;
- the two diagonal reflections: D(n) each, the involutions
  ([A000085](../A000085/)), D(n+1) = D(n) + n·D(n−1);
- the two axis reflections: none for n ≥ 2 (σ(i) = σ(n+1−i) is impossible),
  and the single (or empty) placement for n ≤ 1.

So 8a(n) = n! + C(n) + 2R(n) + 2D(n) + 2[n ≤ 1], the OEIS formula
(Matthias Engelhardt) plus the n ≤ 1 term. A brute-force orbit count
agrees for n ≤ 8.

**How it works**

- Without the last term the numerator is 6 for n ≤ 1 and a multiple of 8
  from n = 2 on, so `+7>>3` (a ceiling) gives 1, 1 and then the exact
  quotients.
- `f` = n!, `c,d` = (D(n−1), D(n)) and `C` = C(n). D, and the R values
  below, are kept doubled (seeds 2, linear recurrences), which drops the
  `2*(…)` from the print.
- R(n) depends only on j = ⌊n/2⌋: it is x(j) with x(2m) = (2m)!/m! and
  x(2m+1) = 0, and x(j) = 2(j−1)·x(j−2) covers both (the ratio
  (2m)!/m! ÷ (2m−2)!/(m−1)! is 2(2m−1)). `p,q` = (x(j−1), x(j)) and moves,
  with C, only when n is odd, just before n becomes 2j: then
  2(j−1) = n − 1 = `~-n` and C(2j) = 2j·C(2j−1) = `C*=n+1`.
- `c,d=d,d+n*c` is D(n+1) = D(n) + n·D(n−1), done before `n+=1;f*=n`.
- The dummy seeds c = D(−1) and p = x(−1) are multiplied by n = 0 and
  n − 1 = 0 in their first use.

**Notes**

- Exact integer recurrences, correct for every n.
- 1559 terms print almost at once; a(1559) has more than 4300 digits and
  `str()` stops the program with a `ValueError` (Python 3.11+ limit).
- The b-file has 451 terms (n = 0 to 450); the bar is the whole b-file.
- Updating after `n+=1` instead (`if~n%2:C*=n;p,q=q,(n-2)*p`) is 99 bytes;
  one loop line with R tracked as a single factor, `r*=(n-2)**(n%4<1)`
  and `r*(n%4<2)` in the print, is 107.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 99 | first entry |
| 2026-11-08 | Python 3 | 97 | step C and x at odd n, before the increment |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000903), CC BY-SA 4.0.
