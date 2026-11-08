# A000952

> Numbers k == 2 (mod 4) that are the orders of conference matrices.
> — [OEIS A000952](https://oeis.org/A000952)

Offset 1: 2, 6, 10, 14, 18, 26, 30, 38, 42, 46, 50, 54, 62, 66, 74, 82, …

### Python 3 — 203 bytes

```python
f=lambda R,t:t<0 or any(f(R+[r],t-1)for x in range(1<<t)for r in[[s[~t]for s in R]+[0]+[x>>j&1or-1for j in range(t)]]if all(sum(map(int.__mul__,r,s))==0for s in R))
n=2
while 1:f([],n-1)and print(n);n+=4
```

**How it works**

- Exhaustive search, one row at a time. A matrix with C Cᵀ = (n−1)I has
  exactly one zero in each row and column, so the zeros can be moved to
  the diagonal. For n ≡ 2 (mod 4) such a matrix is equivalent to a
  symmetric one (Delsarte–Goethals–Seidel 1971: after negating rows and
  columns so that the first row and column are all ones off the diagonal,
  it is symmetric), so only symmetric matrices are searched.
- `f(R,t)` places row i = n−1−t. Its first i entries are column i of the
  rows already placed, `s[~t]` (= s[n−1−t], rows have length n); then the
  zero on the diagonal; then t free entries ±1 from the bits of x
  (`x>>j&1or-1`). The row has to be orthogonal to every earlier row; once
  all n rows are in, C Cᵀ = (n−1)I because each row has n−1 entries ±1.
- Row 0 is searched too, instead of being fixed to the normalized
  (0, 1, …, 1): its first candidate x = 0 is (0, −1, …, −1), which is the
  normalized row up to negating row 0 and column 0, so when a matrix
  exists that first branch already finds one, and other candidates are
  only tried when it fails.
- Counting t down saves bytes: `range(1<<t)`, `range(t)`, `s[~t]` and the
  stop test `t<0`.

**Notes**

- Exact search, using only the symmetrization theorem.
- 2, 6, 10, 14, 18 come in well under a second. Order 22 does not exist
  (Belevitch: n−1 must be a sum of two squares, and 21 is not), but this
  program can only find that out by finishing the search, which it never
  does in practice. Skipping 22 by that theorem does not help much: the
  same search finds nothing for 26 within 3 minutes, and the shortcut that
  would (Paley: n−1 a prime power ≡ 1 mod 4) runs out at 46, which needs
  Mathon's construction. Beyond 82 the OEIS terms are partly open.
- The b-file is synthesized from the 16 terms of the entry; the bar is
  5 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000952), CC BY-SA 4.0.
