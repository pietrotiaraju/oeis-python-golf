# A001383

> Number of n-node rooted trees of height at most 3.
> — [OEIS A001383](https://oeis.org/A001383)

Offset 0: 1, 1, 1, 2, 4, 8, 15, 29, 53, 98, 177, 319, 565, 1001, 1749, 3047, 5264, …

### Python 3 — 110 bytes

```python
L=[1]*4;n=0
while[print(L[-4])]:
 n-=2
 for h in 1,0:L+=sum(d*L[1-d*h]*sum(L[d:1:d])for d in range(n,0,2))//n,
```

**How it works**

- **The series.** A rooted tree of height at most 2 on k nodes is a partition
  of k − 1 (each child of the root keeps some leaves), so a tree of height at
  most 3 on m + 1 nodes is a multiset of those under the root:
  a(m + 1) = c(m), where c = ∏ₖ (1 − xᵏ)^(−p(k−1)) is the Euler transform of
  p(k − 1) and p is the partition function ([A000041](../../A000xxx/A000041/)).
  This is the g.f. x·∏ₖ (1 − xᵏ)^(−p(k−1)) of the entry; a(0) = 1 is the
  entry's convention.
- **Two recurrences.** Both series come from the log-derivative recurrence
  of an Euler transform, **m·c(m) = Σₖ k·p(k−1)·Σⱼ c(m − jk)** and
  **m·p(m) = Σₖ k·Σⱼ p(m − jk)**, over k = 1…m and j ≥ 1, the template of
  [A000235](../../A000xxx/A000235/) (height exactly 3 = c − p).
- **One list.** `L` = [1, 1, c(0), p(0), c(1), p(1), …]: two dummy entries
  in front, then the two series interleaved. Each round appends c(m) and then
  p(m) with n = −2m, so `d` runs over −2k and `L[d:1:d]` reads c(m−k),
  c(m−2k), … (or p(…) in the second pass, one entry longer); the stop `1`
  keeps the dummies out of these sums.
- **The weight** is `L[1-d*h]`: in the c pass (h = 1) index 1 + 2k, where
  p(k − 1) sits; in the p pass (h = 0) index 1, a dummy 1.
- **The print.** `L[-4]` is c(m − 1) = a(m) after round m; before the first
  round it is the first dummy, the conventional a(0) = 1. So the dummies
  cost one byte in the slice and give a(0) for free.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- The whole b-file (201 terms, up to a(200)) prints in under 0.1 s; the bar is
  the whole b-file in 60 s. The same layout with three or four series gives
  [A001384](../A001384/) and [A001385](../A001385/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 110 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001383), CC BY-SA 4.0.
