# A000732

> Boustrophedon transform of 1 & primes: 1,2,3,5,7,...
> — [OEIS A000732](https://oeis.org/A000732)

Offset 0: 1, 3, 8, 22, 66, 222, 862, 3838, 19542, 111894, 712282, 4987672, 38102844, 315339898, 2810523166, …

### Python 3 — 79 bytes

```python
t=k=P=1;r=[]
while~P%k or[r:=[t:=t+x for x in[k-t]+r[::-1]],print(t)]:P*=k;k+=1
```

**How it works**

- With u = 1, 2, 3, 5, 7, 11, … (1 and the primes), the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
- Wilson's theorem: with P = (k−1)!, ~P mod k = (−1−P) mod k is 0 exactly when
  k is prime, and also at k = 1 (everything is 0 mod 1). So `~P%k` is 0 at
  k = 1 and at the primes, which are exactly the inputs 1, 2, 3, 5, 7, …,
  and only then does the `or` build a new row, with first entry k. At every
  other k the header is already true and the body just moves on,
  `P*=k;k+=1`. The program starts from the empty row `r=[]`, so k = 1 builds
  row 0, `[1]`.
- The new row and the print sit in one list display,
  `[r:=…,print(t)]`: it is non-empty, so the header stays true, and the
  print runs right after the row is built, when `t` is its last entry, the
  current term.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `k-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry.

**Notes**

- The 80-byte first entry printed inside the slice, `r[:print(t):-1]`, with
  `-P%k^1or` (k = 1 excluded) and `r=[1]`. `P*=k*k` with `P%k<1` (Wilson
  squared) is 2 bytes longer; a two-line `if P%k:` version is longer still.
- The values were checked for every printed term against
  b(n) = Σₖ C(n,k)·E(n−k)·u(k), the e.g.f. product (sec x + tan x)·U(x), with
  E = [A000111](../A000111/) computed from 2E(n+1) = Σₖ C(n,k)E(k)E(n−k).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about a second.
- The b-file has 401 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 80 | first entry |
| 2026-11-07 | Python 3 | 79 | `~P%k` also accepts k = 1, print in a list display after the row |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000732), CC BY-SA 4.0.
