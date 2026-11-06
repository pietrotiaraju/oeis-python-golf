# A000243

> Number of trees with n nodes, 2 of which are labeled.
> — [OEIS A000243](https://oeis.org/A000243)

Offset 2: 1, 3, 9, 26, 75, 214, 612, 1747, 4995, 14294, 40967, 117560, …

### Python 3 — 124 bytes

```python
r=s=[n:=1]
while[print(v:=sum(map(int.__mul__,r,s)))]:r+=sum(-~j*r[j]*sum(r[~j::~j])for j in range(n))//n,;s=[v+r[n]]+s;n+=1
```

**How it works**

- Walk from the first labeled node to the second. Every node on that path
  carries the rooted tree that hangs off it, so a tree with two labeled nodes
  is a sequence of at least two rooted trees, and the g.f. is
  A = B²/(1−B), with B the g.f. of rooted trees ([A000081](../A000081/)).
- `r` holds b(1), …, b(m), oldest first, and grows by the Euler-transform
  recurrence **m·b(m+1) = Σ_{e=1..m} e·b(e)·Σ_{j≥1} b(m+1−je)** in the
  same form as [A000151](../A000151/) (without its `2*`): `-~j*r[j]` is
  e·b(e) with e = j+1, and `r[~j::~j]` is b(m+1−e), b(m+1−2e), ….
- `s` holds L(k) = [x^k] 1/(1−B), newest first, where
  L(k) = Σ_{j=1..k} b(j)·L(k−j) and L(0) = 1. Since
  B²/(1−B) = 1/(1−B) − 1 − B, a(m) = L(m) − b(m), which is the same sum
  without its j = m term: **a(m) = Σ_{j=1..m−1} b(j)·L(m−j)**.
- That is exactly what the dot product in the loop condition computes:
  at that point `r` still stops at b(m−1), and `map` stops at the shorter
  list, so the L(0) term never enters. The loop prints it as a(m) and
  keeps it in `v`. Then `r` gets b(m), and L(m) = a(m) + b(m) =
  `v+r[n]` goes in front of `s` (`r[n]` is the new last entry, since `n`
  is still the old length of `r`).
- `r` and `s` start as the same list `[1]`, which is b(1) for `r` and L(1)
  for `s`. The first append therefore also puts an extra 1 at the end of
  `s`; from then on `s` is a fresh list every pass, always one longer than
  `r`, and its last entry is never read.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the
  division is exact because the sum is m times the integer b(m+1).
- Each term costs O(m) dot-product work plus the O(m log m) tree
  recurrence on big integers. The whole b-file (199 terms, n up to 200)
  prints in well under a second, and about 3000 terms come out in 60 s;
  the bar is the whole b-file in 60 s.
- a(n+1)/a(n) tends to 2.9558… (the rooted-tree growth constant), so the
  decimal form passes Python's 4300-digit int-to-str limit near n = 9100,
  past what prints within the timeout.
- Printing A000107 − A000081 instead (store L, print `s[0]-r[-1]` after
  the update) needs a start at n = 2 and comes out at 130 bytes. The
  negative-index form of the tree recurrence used in
  [A000107](../A000107/) is 126 here, because `n` can no longer be set
  inside the list literal.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 124 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000243), CC BY-SA 4.0.
