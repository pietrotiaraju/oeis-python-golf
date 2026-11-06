# A000299

> Number of n-node rooted trees of height 4.
> — [OEIS A000299](https://oeis.org/A000299)

Offset 1: 0, 0, 0, 0, 1, 4, 13, 36, 93, 225, 528, 1198, 2666, 5815, 12517, …

Let g, c and p hold the counts of rooted trees of height at most 4, 3 and 2,
shifted so that g(m) counts trees with m + 1 nodes. A tree of height at most
h is a root over a multiset of trees of height at most h − 1, so g is the
Euler transform of c, c the Euler transform of p, and p (the partition
numbers) the Euler transform of all ones. The entry's
a(n) = A001384(n) − A001383(n) is then a(m + 1) = g(m) − c(m). This is
[A000235](../A000235/) (height 3) with one more level.

### Python 3 — 121 bytes

```python
*L,n=1,1,1,0
while[print(L[-3]-L[-2])]:
 n-=3
 for h in 1,1,0:L+=sum(d*L[n-d-2]**h*sum(L[d::d])for d in range(n,0,3))//n,
```

**How it works**

- All three series use the log-derivative recurrence of an Euler
  transform, **m·s(m) = Σₖ k·w(k − 1)·Σⱼ s(m − jk)**, with weight w = c for
  g, w = p for c and w = 1 for p.
- One list holds the three interleaved: `L` = [g(0), c(0), p(0), g(1),
  c(1), p(1), …]. Each round appends g(m), c(m) and p(m), and the loop
  condition prints `L[-3]-L[-2]` = g(m) − c(m) = a(m + 1). The start
  `*L,n=1,1,1,0` prints a(1) = 0.
- With n = −3m, `d` runs over −3m, …, −3, that is d = −3k. Each pass
  appends one entry, so the series being computed always ends at the end
  of the list, and `L[d::d]` steps back by 3k through s(m − k), s(m − 2k), …
  The factor 3 in d cancels against the 3 in n.
- **The weight, from the end.** In the g pass the list has 3m entries and
  c(k − 1) sits at position 3k − 2, which is index 3k − 2 − 3m = n − d − 2
  from the end. In the c pass the list is one entry longer and p(k − 1) is
  one place further in, so the same `L[n-d-2]` is p(k − 1). The p pass
  needs weight 1, and `**h` with h = 0 turns whatever it reads into 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(n) has about 0.25·n digits, so the 4300-digit int-to-str limit
  is near n = 17 500, beyond what the program reaches.
- About 4100 terms in 60 s here; the bar is the whole b-file (1000 terms),
  which prints in under 2 s.
- Reading the weights by their position from the start, as A000235 does
  with `L[~d*h]`, needs three different offsets and a constant: the
  shortest found is `L[h and~d-h]` with the list in the order p, c, g and
  `for h in 0,2,1:`, one byte longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000299), CC BY-SA 4.0.
