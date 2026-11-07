# A000701

> One half of number of non-self-conjugate partitions; also half of number of asymmetric Ferrers graphs with n nodes.
> — [OEIS A000701](https://oeis.org/A000701)

Offset 0: 0, 0, 1, 1, 2, 3, 5, 7, 10, 14, 20, 27, 37, 49, 66, 86, 113, 146, 190, 242, …

### Python 3 — 79 bytes

```python
L=[[1]]
while[print(sum(L[0][-2::-2]))]:k=0;L=[[sum(r[:(k:=k+1)])for r in L]]+L
```

**How it works**

- a(n) is also the number of cycle types of odd permutations of n elements
  (an OEIS comment): a permutation with k cycles has sign (−1)ⁿ⁻ᵏ, so
  a(n) = Σ p(n,k) over n−k odd, where p(n,k) counts partitions of n into
  exactly k parts. The signed sum Σ (−1)ⁿ⁻ᵏ p(n,k) is the coefficient of xⁿ
  in ∏ 1/(1+(−x)ʲ) = ∏ (1+x²ʲ⁻¹), the self-conjugate partitions
  [A000700](../A000700/); so the odd half is (p(n) − A000700(n))/2, the
  definition.
- `L` holds the rows of the triangle p(n,k) ([A008284](https://oeis.org/A008284)),
  newest first: a row is [p(m,1), …, p(m,m)], and row 0 is `[1]`, standing
  for p(0,0).
- Removing one from each of the k parts gives p(n,k) = number of partitions
  of n−k into at most k parts = the sum of the first k entries of row n−k.
  Walking `L` from the newest row, the k-th row met is row n−k, so a counter
  that goes 1, 2, 3, … along the walk is exactly the prefix length:
  `sum(r[:(k:=k+1)])`. When k ≥ n−k the slice is clipped to the whole row,
  which is right (at most k parts is then no restriction).
- The new row is put in front, and `L[0][-2::-2]` takes its entries for
  k = n−1, n−3, …, the ones with n−k odd. For n = 0 and 1 the slice is
  empty and prints 0.
- The walrus counter, reset with `k=0`, is 4 bytes shorter than
  `for k,r in enumerate(L,1)`.

**Notes**

- Exact integer additions; the only facts used are the two identities
  above (removing a column, and the sign of a permutation).
- Row n costs about n²/4 additions and every row is kept (about n²/2
  integers): 2506 terms in 60 s, using about 190 MB.
- The b-file has 10001 terms; the bar is 1900 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000701), CC BY-SA 4.0.
