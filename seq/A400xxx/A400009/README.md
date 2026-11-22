# A400009

> Sprague-Grundy value of the sieve game on {2, ..., n}: a move crosses out a
> number not yet crossed out together with all its multiples, and the player
> who makes the last move wins.
> — [OEIS A400009](https://oeis.org/A400009) (draft when added)

Offset 1: 0, 1, 0, 3, 2, 1, 0, 4, 5, 1, 0, 7, 6, 4, 8, 7, 6, 2, 3, 6, 3, 1, 0, 9, 8, …

### Python 3 — 146 bytes

```python
from functools import*
@cache
def g(s):return min({*range(len(s)+1)}-{g((*filter(x.__rmod__,s),))for x in s})
s=()
while[print(g(s))]:s+=len(s)+2,
```

**How it works**

- A position is the tuple of the numbers not yet crossed out, in increasing
  order. The board for n is (2, 3, ..., n); the loop prints a(n) and appends
  the next number, `len(s)+2`, to get the board for n + 1.
- A move picks x in s and crosses out x and every multiple of x still on the
  board. `filter(x.__rmod__,s)` keeps exactly the y with y mod x ≠ 0, so it
  leaves the position after that move, still in increasing order. Each move
  removes at least x itself, so the game ends.
- The player who makes the last move wins, so this is a normal-play impartial
  game and its value is the Sprague–Grundy number: g(s) = mex of g over the
  positions one move away, and g(()) = 0. A position with k numbers has k
  moves, so the mex is at most k and lies in `range(len(s)+1)`; the program
  takes the least value of that range not among the options.
- The same set of numbers always gives the same increasing tuple, and its
  value does not depend on n. So the cache is shared from one n to the next,
  and the work for a new n is only the positions that still contain n.

**Notes**

- This is a plain search over all positions. The 30th term arrives after
  about 18 reference seconds and the 31st after about 34, so the bar is 30
  terms. Memory grows with the cache: about 0.5 GB by the 31st term.
- The draft's terms (n ≤ 65) were computed with reductions that this program
  does not use: a position is the sum of the connected components of its
  divisibility graph, and a mirror argument removes pairs of equivalent primes.
  The simplest one helps even here: a prime p with 2p > n is an isolated Nim
  heap of size 1, so a(n) = a(n−1) XOR 1 when n is prime. Taking those primes
  off the board and keeping their parity reaches 37 terms in the same time,
  for about 60 more bytes.
- The b-file holds the draft's 65 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 146 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A400009), CC BY-SA 4.0.
