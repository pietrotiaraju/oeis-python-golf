# A000747

> Boustrophedon transform of primes.
> — [OEIS A000747](https://oeis.org/A000747)

Offset 0: 2, 5, 13, 35, 103, 345, 1325, 5911, 30067, 172237, 1096319, 7677155, 58648421, 485377457, 4326008691, …

### Python 3 — 80 bytes

```python
t=k=P=1;r=[]
while-P%k^1or[r:=[t:=t+x for x in[k-t]+r[::-1]],print(t)]:P*=k;k+=1
```

**How it works**

- With u = 2, 3, 5, 7, 11, … (the primes, from 2),
  the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
- Wilson's theorem: with P = (k−1)!, −P mod k is 1 exactly when k is prime
  (k = 1 gives 0). So `-P%k^1` is 0 only at primes, and only then does the
  `or` build a new row, with first entry k. At every other k the header is
  already true and the body just moves on, `P*=k;k+=1`.
- The `or` branch is the list `[r:=…,print(t)]`: it builds the new row, then
  prints its last entry, and as a non-empty list it keeps the header true.
  The program starts with no row at all, `r=[]`, so the first prime, 2,
  builds row 0 = [2] and prints a(0) = 2.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `k-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, printed right after the row is built.

**Notes**

- [A000732](../A000732/) (1 and the primes) prints inside the slice,
  `r[:print(t):-1]`, before each new row. Here that would print a value
  before row 0, so row 0 has to be set up by hand (`t=P=2;k=3;r=[2]`), 2
  bytes longer.
- The values were checked for every printed term against
  b(n) = Σₖ C(n,k)·E(n−k)·u(k), the e.g.f. product (sec x + tan x)·U(x), with
  E = [A000111](../A000111/) computed from 2E(n+1) = Σₖ C(n,k)E(k)E(n−k).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about two seconds.
- The b-file has 401 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000747), CC BY-SA 4.0.
