# A000296

> Set partitions without singletons: number of partitions of an n-set into blocks of size > 1. Also number of cyclically spaced (or feasible) partitions.
> — [OEIS A000296](https://oeis.org/A000296)

Offset 0: 1, 0, 1, 1, 4, 11, 41, 162, 715, 3425, 17722, 98253, 580317, …

### Python 3 — 56 bytes

```python
r=[t:=1]
while[print(r[0])]:r=[t:=t+x for x in[-r[0]]+r]
```

**How it works**

- **The identity.** B(n) = a(n) + a(n + 1), with B the Bell numbers
  ([A000110](../A000110/)): take a partition of {1, …, n}; if it has no
  singletons it is counted by a(n), and otherwise merging all its
  singletons with n + 1 into one block gives a partition of {1, …, n + 1}
  without singletons. Every partition counted by a(n + 1) arises once
  (split the block of n + 1 back into singletons). So a(n + 1) = B(n) − a(n).
- **The rows.** Row n of the list is a(n) followed by row n − 1 of the
  Bell (Aitken) triangle, which runs from B(n − 1) to B(n); `t` is its
  last entry, B(n). The next row is the running sums from t over
  [−a(n)] + row n: first t − a(n) = a(n + 1), then t − a(n) + a(n) = B(n),
  then B(n) plus each Bell entry in turn, which is exactly how the Bell
  triangle builds row n from row n − 1. So the invariant holds, and t ends
  as B(n + 1).
- This is the [A000110](../A000110/) program (`t,*r=1,` /
  `r=[t:=t+x for x in[0]+r]`) with the 0 replaced by −a(n) and a(n) kept at
  the front of the row. Row 0 is just [a(0)] = [1], with t = B(0) = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(1982)
  passes 4300 digits, so the program prints 1982 terms (n = 0..1981) and
  then stops with CPython's int-to-str `ValueError`. The b-file has 576
  terms, which print in a fraction of a second; the bar is the whole
  b-file in 60 s.
- Same length: `while[print(a:=r[0])]:r=[t:=t+x for x in[-a]+r]`. Keeping
  a(n) apart from the Bell row (`a=t=1;q=[]` /
  `while[print(a)]:a=t-a;q=[t:=t+x for x in[0]+q]`) is 57.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000296), CC BY-SA 4.0.
