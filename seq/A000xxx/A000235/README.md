# A000235

> Number of n-node rooted trees of height 3.
> — [OEIS A000235](https://oeis.org/A000235)

Offset 1: 0, 0, 0, 1, 3, 8, 18, 38, 76, 147, 277, 509, 924, 1648, 2912, …

A rooted tree of height at most 2 on n nodes is a partition of n − 1 (each
child of the root keeps some leaves), so height at most 3 means a multiset of
such trees under the root: the g.f. is x·∏ₖ (1 − xᵏ)^(−p(k−1)). Taking away
the trees of height at most 2 leaves a(n) = c(n−1) − p(n−1), where c counts
those multisets ([A001383](https://oeis.org/A001383) shifted) and p is the
partition function ([A000041](../A000041/)).

### Python 3 — 113 bytes

```python
*L,n=1,1,0
while[print(L[-2]-L[-1])]:
 n-=2
 for h in 1,0:L+=sum(d*L[~d*h]*sum(L[d::d])for d in range(n,0,2))//n,
```

**How it works**

- Both series come from the log-derivative recurrence of an Euler
  transform, as in [A000041](../A000041/) and [A000219](../A000219/):
  **m·c(m) = Σₖ k·p(k−1)·Σⱼ c(m − jk)** and **m·p(m) = Σₖ k·Σⱼ p(m − jk)**,
  over k = 1…m and j ≥ 1. They differ only in the weight, p(k−1) or 1.
- One list holds both, interleaved: `L` = [c(0), p(0), c(1), p(1), …]. Each
  round appends c(m) and then p(m), and the loop condition prints
  `L[-2]-L[-1]` = c(m) − p(m) = a(m+1). The start `*L,n=1,1,0` prints
  a(1) = 0.
- With n = −2m, `d` runs over −2m, −2m+2, …, −2, that is d = −2k. Before
  c(m) is appended the list has 2m entries, so `L[d::d]` starts at index
  2m − 2k and steps back by 2k: c(m−k), c(m−2k), …. Before p(m) is
  appended it has 2m+1 entries and the same slice reads p(m−k), p(m−2k), ….
  The factor 2 in d cancels against the 2 in n.
- The weight is `L[~d*h]`. In the c pass (h = 1) the index ~d = 2k − 1 is
  exactly where p(k−1) sits. In the p pass (h = 0) it is index 0, which
  holds c(0) = 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- About 6100 terms in 60 s here; the bar is the whole b-file (200 terms) in
  60 s. a(6106) has 693 digits, so the 4300-digit int-to-str limit is far
  beyond what the program reaches.
- Two lists, `for a,b in(P,[1]*-n),(C,P):` with weight `b[~d]` and a list of
  ones for the partitions, take 127 bytes. Computing both new entries from
  the old list in one `L+=[… for h in(1,0)]` needs a slice offset and is 3
  bytes longer. Moving `n-=2` into the `for` header as a walrus costs 2.
- Packing the series into big integers, with `pow(1-B**k,-e,M)` for
  (1 − xᵏ)^(−e) mod a power of B = 4ⁿ and e read off as a digit of the
  partition series, comes to about 140 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000235), CC BY-SA 4.0.
