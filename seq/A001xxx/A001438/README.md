# A001438

> Maximal number of mutually orthogonal Latin squares (or MOLS) of order n.
> — [OEIS A001438](https://oeis.org/A001438)

Offset 2: 1, 2, 3, 4, 1, 6, 7, 8, …

Two Latin squares of order n are orthogonal when the n² ordered pairs of
their entries, cell by cell, are all different; a(n) is the largest number
of Latin squares of order n that are pairwise orthogonal. Nobody knows
a(10).

### Python 3 — 330 bytes

```python
from itertools import*
from math import*
def h(F,P,k):
 c=len(P)
 return k<1 or(h(F+P,[],k-1)if c==n else any(h(F,P+[s],k)for s in permutations(range(n))if s[0]==c and(F or s[c]<1)and all(sum(map(int.__eq__,s,q))==(q in F)for q in F+P)))
n=l=1
while n:=n+1:
 k=1;q=l<(l:=lcm(l,n))
 while k<n-1and(q or h([],[],k+1)):k+=1
 print(k)
```

**How it works**

- Two theorems give a(n) when n is a prime power. There are never more
  than n − 1 MOLS of order n: relabel each square so that its first row
  is 0 … n − 1; then the cell below the first one holds a nonzero symbol
  s in each square, and two squares cannot share it, since the pair
  (s, s) already sits in the first row. And for a prime power q the field
  GF(q) gives q − 1 of them, the squares (x, y) ↦ m·x + y for m ≠ 0
  (Moore 1896, Bose 1938). n is a prime power exactly when lcm(1, …, n) > lcm(1, …, n − 1),
  so `q=l<(l:=lcm(l,n))` with a running lcm; then k climbs to n − 1 with
  no search.
- For other n the program searches, k = 2, 3, … up to n − 1, until
  k MOLS do not exist (a subset of MOLS is MOLS, so the first failure is
  the maximum). This happens at n = 6 (Tarry's theorem, which the search
  re-proves) and would take forever at n = 10.
- A Latin square is a partition of the n² cells into n permutation
  matrices, one per symbol; the permutation s of symbol c puts c in row r,
  column s[r]. Two squares are orthogonal exactly when each permutation of
  one meets each permutation of the other in one cell, and permutations of
  the same square meet in no cell. So `h` builds the squares one symbol
  at a time: a new permutation s must agree in exactly one place with
  every permutation q of the finished squares F, and in none with those
  of the square P being built, `sum(map(int.__eq__,s,q))==(q in F)`.
- Normalization keeps the search small and loses nothing: relabelling
  the symbols of each square separately puts the first row in order
  (symbol c's permutation starts with c, `s[0]==c`), and permuting the
  rows of all squares together puts the first column of the first square
  in order (`F or s[c]<1`: its symbol c sits at row c, column 0). Both keep
  every pair of squares orthogonal.
- `h(F,P,k)` asks for k more squares; a square is finished after n
  permutations (`c==n`) and joins F. For n = 6 the search goes through
  all 9408 normalized first squares and finds no orthogonal mate for any.

**Notes**

- Correct for every n: the prime powers rest on the two theorems above,
  every other n on an exhaustive search. The program prints a(2) … a(9) and
  then searches for 3 MOLS of order 10, an open problem.
- The b-file is synthesized from the OEIS data (8 terms, n = 2 to 9); the
  bar is the whole b-file in 60 s. a(6) comes after about 21 s here and the
  rest at once.
- Testing the prime power as `p**n%n<1`, with p the least prime factor,
  is 8 bytes longer than the running lcm.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 330 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001438), CC BY-SA 4.0.
