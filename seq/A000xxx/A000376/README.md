# A000376

> Topswops (2): start by shuffling n cards labeled 1..n. If the top card is m, reverse the order of the top m cards. Repeat until 1 gets to the top, then stop. Suppose the whole deck is now sorted (if not, discard this case). a(n) is the maximal number of steps before 1 got to the top.
> — [OEIS A000376](https://oeis.org/A000376)

Offset 1: 0, 1, 2, 4, 7, 10, 16, 22, 30, 38, 51, 63, 80, 101, 112, 130, 159, 191, 207, 231, …

### Python 3 — 102 bytes

```python
g=lambda d:max([-~g(d[k::-1]+d[k+1:])for k in d if d[k]==k>0]+[0])
d=[0]
while[print(g(d))]:d+=len(d),
```

**Playing backwards**

- The cards are 0 … n−1, so the top card k means "reverse the top k+1
  cards", and the game stops with 0 on top.
- If deck e has top card k ≥ 1, one step turns it into d with d[k] = k:
  card k ends up at position k. Conversely, if d[k] = k for some k ≥ 1,
  reversing the top k+1 cards of d gives a deck with k on top whose step
  leads back to d, because the same reversal undoes itself. So the decks
  one step before d are exactly the reversals at the positions k ≥ 1 that
  hold card k.
- The game always ends (Conway's topswops theorem), so following these
  steps backwards from the sorted deck reaches every deck whose game ends
  sorted, each once, at a depth equal to its number of steps. a(n) is the
  height of that tree.

**How it works**

- `g(d)` is that height below d: 0 when no position k ≥ 1 holds card k, and
  otherwise 1 more than the highest branch. `+[0]` gives the 0 for leaves.
- `for k in d` runs over the card values, which are exactly 0 … n−1, so it
  needs no `range(len(d))`; `d[k]==k>0` keeps the positions k ≥ 1 that
  hold card k.
- `d` grows from `[0]` by one card at a time (`d+=len(d),`), so it is the
  sorted deck of every size in turn.

**Notes**

- Exhaustive, exact, and much faster than trying all n! decks: it only
  visits the decks whose game ends sorted. 12 terms take about 13 s here,
  and n = 13 takes minutes. The bar is 12 terms in 60 s; the b-file has 20.
- The recursion depth is a(n), far below Python's limit of 1000 for every
  reachable n.
- Playing forwards from all n! decks, as in [A000375](../A000375/), with a
  penalty `-([*d]!=sorted(d))<<len(d)` for games that end unsorted, is 153
  bytes and reaches 10 terms.
- `max(0,*(…))` fails on a leaf, where the generator is empty and `max(0)`
  gets a single int; `for k in d[1:]if d[k]==k` is a byte longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 102 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000376), CC BY-SA 4.0.
