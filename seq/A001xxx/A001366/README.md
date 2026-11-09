# A001366

> Maximum number of unattacked squares with n queens on an n X n board (answers for n >= 19 only probable).
> — [OEIS A001366](https://oeis.org/A001366)

Offset 1: 0, 0, 0, 1, 3, 5, 7, 11, 18, 22, …

Place n queens anywhere on the n × n board and count the squares that are
neither occupied nor attacked; a(n) is the largest possible count. Whether
queens block each other's lines does not matter: if a line through a square
holds any queen, the nearest one on it attacks the square. The program is
an exact exhaustive search, so unlike the "probable" values of the OEIS entry
its output is proven for every n it reaches.

### Python 3 — 231 bytes

```python
n=0
while 1:
 n+=1;t=0;r=range(N:=n*n);L=[sum(1<<j for j in r if 0in(u:=j//n-i//n,v:=j%n-i%n,u+v,u-v))for i in r]
 g=lambda i,a,m:N-a.bit_count()>t and(m<1or any(g(s+1,a|L[s],m-1)for s in range(i,N)))
 while g(0,0,n):t+=1
 print(t)
```

**How it works**

- Squares are numbered i = n·row + column. `L[i]` is the bit mask of the
  squares that a queen on i attacks or occupies: j with row difference u
  and column difference v such that one of u, v, u + v, u − v is 0
  (same row, column or diagonal; i itself included).
- `g(i,a,m)` asks whether m more queens, on distinct squares numbered ≥ i,
  can be added to the queens already placed (attacked-or-occupied mask a) so
  that more than t squares stay free. Squares are taken in increasing order,
  so every set of n squares is tried exactly once.
- Pruning: adding a queen can only enlarge a, so once N − |a| ≤ t no
  completion can beat t and the branch returns False. This bound is the
  only cut, so `g(0,0,n)` is True exactly when some placement leaves more
  than t squares free.
- t rises from 0 while such a placement exists; the first t that fails is
  the maximum, a(n).

**Golf notes**

- Counting t upwards is both shorter and about three times faster than
  coming down from n²: the successful searches stop at their first witness,
  and the clustered corner placements that achieve the maximum come early
  in row-major order, so only the last search (t = a(n)) is exhaustive.
- `0in(u:=…,v:=…,u+v,u-v)` is 4 bytes under `u*v*(u*u-v*v)==0`.
- Passing the number of queens still to place (`m<1or`) is 2 bytes under
  comparing a placed count with n.
- Skipping squares whose four lines are already used (they never change
  the count) does not shrink the search here: such squares are almost never
  available in the failing searches, and testing for them costs more.

**Notes**

- Correct for every n: the search covers all C(n², n) placements except
  those cut by a bound that is valid by monotonicity, with exact integer
  bit masks.
- The time grows quickly with n: a(9) comes after about 7 s here and
  a(10) after about 65 s.
- The b-file is synthesized from the OEIS data (30 terms, n = 1 to 30;
  the OEIS calls the terms from n = 19 on probable); the bar is 9 terms
  (up to a(9)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 231 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001366), CC BY-SA 4.0.
