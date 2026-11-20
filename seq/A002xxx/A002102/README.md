# A002102

> Number of nonnegative solutions to x^2 + y^2 + z^2 = n.
> — [OEIS A002102](https://oeis.org/A002102)

Offset 0: 1, 3, 3, 1, 3, 6, 3, 0, 3, 6, 6, 3, …

### Python 3 — 85 bytes

```python
S={0};n=0
while[print(sum(n-x-y in S for x in S for y in S))]:n+=1;S|={len(S)**2}&{n}
```

**How it works**

- a(n) counts ordered triples (x, y, z) of nonnegative integers with
  x² + y² + z² = n, that is, the ordered pairs of squares (x², y²) for
  which n − x² − y² is also a square.
- `S` holds the squares 0, 1, 4, …, (s−1)² up to n: after `n+=1`,
  `{len(S)**2}&{n}` is {s²} when n is the next square s² and empty
  otherwise, so S gains each square exactly when n reaches it.
- `sum(n-x-y in S for x in S for y in S)` then counts the pairs (x², y²);
  a negative difference is never in S, and every square up to n is, so
  this is exactly a(n).
- `while[print(…)]:` prints before each step; a one-element list is
  always true.

**Notes**

- Integer arithmetic only, so it is correct for every n; a term costs
  about n set lookups.
- The b-file has 10001 terms (n = 0…10000); the bar is all of them in
  60 s, about 11 s here.

## First 700 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 700 terms have to arrive in time.

### Python 3, 700 terms — 75 bytes

```python
S={0};n=0
while[print(sum(n-x-y in S for x in S for y in S))]:n+=1;S|={n*n}
```

**How it works**

- The same count, but `S|={n*n}` adds a square at every step, so S holds
  0, 1, 4, …, n². Every square up to n is in it (k² ≤ n implies k ≤ n),
  and the larger ones never equal n − x − y, so the count is unchanged.
- S then has n + 1 elements, so a term costs about n² lookups instead
  of n.

**Limits**

- Here a(699) arrives after about 23 s, far short of the main bar of
  10001 terms; the program saves 10 bytes by giving that up.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 85 | first entry |

**Python 3, 700 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 75 | first entry: every square up to n² in the set, about n² lookups a term |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002102), CC BY-SA 4.0.
