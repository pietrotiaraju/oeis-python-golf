# A001760

> Number of permutations of [n] with n-4 sequences.
> — [OEIS A001760](https://oeis.org/A001760)

Offset 1: 2, 60, 836, 9576, 103326, 1106820, 12062152, 135391872, 1575253690, …

### Python 3 — 103 bytes

```python
r=[0,2,12,10,0,0];n=4
while 1:n+=1;r=[k*r[k]+2*r[k-1]+(n-k)*r[k-2]for k in range(n)]+[0,0];print(r[-6])
```

**How it works**

- **Indexing.** The title counts permutations of [n] with n − 4 alternating
  runs, but the entry has offset 1: its a(1) = 2 is the count for
  permutations of [5] with 1 run (only 12345 and 54321). So the terms are
  a(i) = R(i + 4, i) for i ≥ 1, where R(n, k) counts the permutations of [n]
  with k runs, and that is what the program prints.
- **André's recurrence.** Inserting n into a permutation of [n − 1] gives
  R(n, k) = k·R(n − 1, k) + 2·R(n − 1, k − 1) + (n − k)·R(n − 1, k − 2)
  (D. André, 1884; F. N. David and D. E. Barton, *Combinatorial Chance*,
  1962). The program runs it row by row.
- **The row.** `r` holds row n − 1, R(n − 1, 0…n − 2), followed by two
  zeros, so `r[k]` at k = n − 1 and `r[k-1]`, `r[k-2]` at k = 0, 1 (which
  wrap round to the end of the list) all read 0, as they should. The new row
  gets the two zeros again, and R(n, n − 4) is then 6th from the end,
  `r[-6]`. The program starts from row 4, `[0,2,12,10]`, so the first term
  printed is R(5, 1) = 2.

**Notes**

- Same template as [A001759](../A001759/) (n − 3 runs), where the start row
  happens to contain the next n. Through the Euler zigzag numbers Eₙ the
  recurrence gives 3a = Eₙ₊₃ − 6Eₙ₊₂ + (16 − 3n)Eₙ₊₁ + (6n − 18)Eₙ for
  n = i + 4, which is longer to code.
- Exact integer arithmetic, so the program is right for every n.
- The OEIS has no b-file for this sequence; the one here holds the 17 terms of
  the entry (i = 1 to 17), and the bar is all of them in 60 s, which takes
  well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001760), CC BY-SA 4.0.
