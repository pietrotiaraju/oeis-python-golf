# A001759

> Number of permutations of [n] with n-3 sequences.
> — [OEIS A001759](https://oeis.org/A001759)

Offset 4: 2, 28, 236, 1852, 14622, 119964, 1034992, 9434444, 90968602, 927367340, …

### Python 3 — 98 bytes

```python
r=[0,2,n:=4,0,0]
while 1:r=[k*r[k]+2*r[k-1]+(n-k)*r[k-2]for k in range(n)]+[0,0];print(r[-5]);n+=1
```

**How it works**

- **Runs.** A "sequence" here is an alternating run: a maximal increasing or
  decreasing stretch of the permutation. Let R(n, k) count the permutations
  of [n] with k runs; a(n) = R(n, n − 3).
- **André's recurrence.** Inserting n into a permutation of [n − 1] gives
  R(n, k) = k·R(n − 1, k) + 2·R(n − 1, k − 1) + (n − k)·R(n − 1, k − 2)
  (D. André, 1884; F. N. David and D. E. Barton, *Combinatorial Chance*,
  1962), with R(1, 0) = 1. The program runs it row by row.
- **The row.** `r` holds row n − 1, R(n − 1, 0…n − 2), followed by two
  zeros, so `r[k]` at k = n − 1 and `r[k-1]`, `r[k-2]` at k = 0, 1 (which
  wrap round to the end of the list) all read 0, as they should. The new row
  gets the two zeros again, and R(n, n − 3) is then 5th from the end,
  `r[-5]`.
- **The start.** a(4) is the first term, so the program starts from row 3,
  `[0,2,4]`, and n = 4; since R(3, 2) = 4, `n:=4` sits in the list itself.

**Notes**

- Applying the recurrence twice at the top of the triangle (R(n, n) = 0)
  gives a(n) = Eₙ₊₂ − 4Eₙ₊₁ + (5 − n)Eₙ with Eₙ the Euler zigzag numbers, as in
  [A001758](../A001758/). With Seidel's boustrophedon that is 99 bytes,
  `r=[0,5,10,14,16,16]` / `while 1:s=0;r=[s:=s+x for x in[0]+r[::-1]];print(s-4*r[1]+(8-len(r))*(s-r[-3]))`
  (row n + 2 holds Eₙ₊₂ at the end, Eₙ₊₁ at index 1 and Eₙ₊₂ − Eₙ third
  from the end): the factor n costs more than the triangle.
- Exact integer arithmetic, so the program is right for every n.
- The OEIS has no b-file for this sequence; the one here holds the 18 terms of
  the entry (n = 4 to 21), and the bar is all of them in 60 s, which takes
  well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001759), CC BY-SA 4.0.
