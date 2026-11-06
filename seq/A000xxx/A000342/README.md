# A000342

> Number of n-node rooted trees of height 5.
> — [OEIS A000342](https://oeis.org/A000342)

Offset 1: 0, 0, 0, 0, 0, 1, 5, 19, 61, 180, 498, 1323, 3405, 8557, 21103, …

Let g₅, g₄, g₃ and p hold the counts of rooted trees of height at most 5,
4, 3 and 2, shifted so that g(m) counts trees with m + 1 nodes. A tree of
height at most h is a root over a multiset of trees of height at most
h − 1, so each series is the Euler transform of the next one, and p (the
partition numbers) is the Euler transform of all ones. The entry's
a(n) = A001385(n) − A001384(n) is then a(m + 1) = g₅(m) − g₄(m). This is
[A000299](../A000299/) (height 4) with one more level.

### Python 3 — 122 bytes

```python
L=[1]*4;n=0
while[print(L[-4]-L[-3])]:
 n-=4
 for h in 1,1,1,0:L+=sum(d*L[n-d-3]**h*sum(L[d::d])for d in range(n,0,4))//n,
```

**How it works**

- All four series use the log-derivative recurrence of an Euler
  transform, **m·s(m) = Σₖ k·w(k − 1)·Σⱼ s(m − jk)**, with weight w = g₄
  for g₅, w = g₃ for g₄, w = p for g₃ and w = 1 for p.
- One list holds the four interleaved: `L` = [g₅(0), g₄(0), g₃(0), p(0),
  g₅(1), …]. Each round appends g₅(m), g₄(m), g₃(m) and p(m), and the loop
  condition prints `L[-4]-L[-3]` = g₅(m) − g₄(m) = a(m + 1). The start
  `L=[1]*4` (all four series are 1 at m = 0) prints a(1) = 0.
- With n = −4m, `d` runs over −4m, …, −4, that is d = −4k. Each pass
  appends one entry, so the series being computed always ends at the end
  of the list, and `L[d::d]` steps back by 4k through s(m − k), s(m − 2k), …
  The factor 4 in d cancels against the 4 in n.
- **The weight, from the end.** In the g₅ pass the list has 4m entries and
  g₄(k − 1) sits at position 4k − 3, which is index 4k − 3 − 4m = n − d − 3
  from the end. Each later pass finds the list one entry longer and its
  weight series one place further in, so the same `L[n-d-3]` is g₃(k − 1)
  in the g₄ pass and p(k − 1) in the g₃ pass. The p pass needs weight 1,
  and `**h` with h = 0 turns whatever it reads into 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(3000) has 896 digits, so the 4300-digit int-to-str limit is
  far beyond what the program reaches.
- About 2950 terms in 60 s here; the bar is the whole b-file (200 terms),
  which prints in a fraction of a second.
- `L=[1]*4;n=0` is 3 bytes under the `*L,n=1,1,1,1,0` start of A000299.
  Reading the p pass weight as `L[(n-d-3)*h]` (h = 0 reads L[0] = 1) is
  one byte longer than `L[n-d-3]**h`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000342), CC BY-SA 4.0.
