# A000081

> Number of unlabeled rooted trees with n nodes (or connected functions with a fixed point).
> — [OEIS A000081](https://oeis.org/A000081)

Offset 0: 0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, 12486, …

### Python 3 — 87 bytes

```python
r=[n:=0,1]
while[print(r[-n])]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

- The recurrence from the OEIS page, a(m+1) = (1/m) Σ_{k=1..m} c(k)·a(m+1−k)
  with c(k) = Σ_{d|k} d·a(d), with the two sums swapped:
  **m·a(m+1) = Σ_{d=1..m} d·a(d)·Σ_{j≥1} a(m+1−jd)**. This is the Euler
  transform: a rooted tree with m+1 nodes is a root over a multiset of
  rooted trees with m nodes in all.
- `r` lists a(0) … a(m), so `n` = −m is minus the last index. With d running
  over −m … −1, `r[-d]` is a(|d|), and the slice `r[d::d]` starts at
  a(m+1−|d|) and steps back by |d|. It may reach a(0) = 0, which adds
  nothing. The sum is negative because every d is, and dividing by `n` = −m
  makes it a(m+1).
- `r=[n:=0,1]` seeds a(0) = 0 and a(1) = 1 and sets `n=0` within the list
  display, one byte shorter than `r=[0,1];n=0`.
- The loop condition prints a(−n), which is a(m−1) once `n` has dropped to
  −m. The list stays two terms ahead of the printing. `while[print(…)]` loops
  forever because `[None]` is a non-empty list, and `r+=…,` appends a
  one-tuple.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the
  division is exact because the recurrence gives an integer.
- Each term costs O(n log n) big-integer operations. The whole b-file (1001
  terms, n up to 1000) prints in under a second, and about 4200 terms print
  in 60 s. The bar is the whole b-file in 60 s.
- a(n) ~ 0.4399 · 2.9558ⁿ · n^(−3/2) (Otter), so from about n = 9150 its
  decimal form passes Python's 4300-digit int-to-str limit.
- `print(r[-2])` in place of `print(r[-n])` is a tie: the list always holds
  two terms past the one being printed. So is `for x in r:print(x);` in
  place of `while[print(r[-n])]:`, since a `for` loop over a list keeps
  going while the list grows.
- The same recurrence over rooted forests, as in [A000055](../A000055/),
  avoids the a(0) seed but needs a separate `print(0)`, and comes out longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000081), CC BY-SA 4.0.
