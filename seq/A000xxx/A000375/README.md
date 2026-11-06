# A000375

> Topswops (1): start by shuffling n cards labeled 1..n. If top card is m, reverse order of top m cards, then repeat. a(n) is the maximal number of steps before top card is 1.
> — [OEIS A000375](https://oeis.org/A000375)

Offset 1: 0, 1, 2, 4, 7, 10, 16, 22, 30, 38, 51, 65, 80, 101, 113, 139, 159, 191, 221, 249, 282, …

### Python 3 — 125 bytes

```python
from itertools import*
f=lambda d:(k:=d[0])and-~f(d[k::-1]+d[k+1:])
n=1
while[print(max(map(f,permutations(range(n)))))]:n+=1
```

**How it works**

- The cards are 0 … n−1 instead of 1 … n, so the top card k means "reverse
  the top k+1 cards", and the game stops when 0 is on top.
- `f(d)` plays the game from deck d and counts the steps:
  `(k:=d[0])and…` returns 0 when the top card is 0, and otherwise
  1 + f of the deck with its top k+1 cards reversed, `d[k::-1]+d[k+1:]`.
- `max(map(f,permutations(range(n))))` tries every one of the n! decks.

**Notes**

- The game always ends (Conway's topswops theorem; Knuth showed it takes
  at most F(n+1) − 1 steps), so f terminates on every deck. Its recursion
  depth is a(n); Python's default limit of 1000 would only be reached for
  n far beyond the known terms.
- Exhaustive search, exact: 10 terms in about 18 s here, and n = 11 (39.9
  million decks) would take several minutes. The bar is 10 terms in 60 s;
  the b-file has 21 (n = 1 to 21, from much faster searches).
- Running the game backwards from the decks with 0 on top, as in
  [A000376](../A000376/), visits each deck only once and is faster, but it
  needs those (n−1)! starting decks and is about 20 bytes longer.
- `d[0]and-~f(d[d[0]::-1]+d[d[0]+1:])` is the same length as the walrus.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 125 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000375), CC BY-SA 4.0.
