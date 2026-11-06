# A000393

> Number of n-node rooted trees of height 6.
> — [OEIS A000393](https://oeis.org/A000393)

Offset 1: 0, 0, 0, 0, 0, 0, 1, 6, 26, 94, 308, 941, 2744, 7722, 21166, …

Let g₆, g₅, g₄, g₃ and p hold the counts of rooted trees of height at most
6, 5, 4, 3 and 2, shifted so that g(m) counts trees with m + 1 nodes. A
tree of height at most h is a root over a multiset of trees of height at
most h − 1, so each series is the Euler transform of the next one, and p
(the partition numbers) is the Euler transform of all ones. The entry's
a(n) = A034823(n) − A001385(n) is then a(m + 1) = g₆(m) − g₅(m). This is
[A000342](../A000342/) (height 5) with one more level.

### Python 3 — 124 bytes

```python
L=[1]*5;n=0
while[print(L[-5]-L[-4])]:
 n-=5
 for h in 1,1,1,1,0:L+=sum(d*L[n-d-4]**h*sum(L[d::d])for d in range(n,0,5))//n,
```

**How it works**

- All five series use the log-derivative recurrence of an Euler
  transform, **m·s(m) = Σₖ k·w(k − 1)·Σⱼ s(m − jk)**, with weight w = g₅
  for g₆, g₄ for g₅, g₃ for g₄, p for g₃ and 1 for p.
- One list holds the five interleaved: `L` = [g₆(0), g₅(0), g₄(0), g₃(0),
  p(0), g₆(1), …]. Each round appends g₆(m), g₅(m), g₄(m), g₃(m) and p(m),
  and the loop condition prints `L[-5]-L[-4]` = g₆(m) − g₅(m) = a(m + 1).
  The start `L=[1]*5` (every series is 1 at m = 0) prints a(1) = 0.
- With n = −5m, `d` runs over −5m, …, −5, that is d = −5k. Each pass
  appends one entry, so the series being computed always ends at the end
  of the list, and `L[d::d]` steps back by 5k through s(m − k), s(m − 2k), …
  The factor 5 in d cancels against the 5 in n.
- **The weight, from the end.** In the g₆ pass the list has 5m entries and
  g₅(k − 1) sits at position 5k − 4, which is index 5k − 4 − 5m = n − d − 4
  from the end. Each later pass finds the list one entry longer and its
  weight series one place further in, so the same `L[n-d-4]` reads the
  right weight in every pass. The p pass needs weight 1, and `**h` with
  h = 0 turns whatever it reads into 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(2600) has 894 digits, so the 4300-digit int-to-str limit is
  far beyond what the program reaches.
- About 2650 terms in 60 s here; the bar is the whole b-file (200 terms),
  which prints in a fraction of a second.
- `L=[1]*5;n=0` is 5 bytes under a start like `*L,n=1,1,1,1,1,0`. Reading
  the p pass weight as `L[(n-d-4)*h]` (h = 0 reads L[0] = 1) is one byte
  longer than `L[n-d-4]**h`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 124 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000393), CC BY-SA 4.0.
