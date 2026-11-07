# A000342

> Number of n-node rooted trees of height 5.
> — [OEIS A000342](https://oeis.org/A000342)

Offset 1: 0, 0, 0, 0, 0, 1, 5, 19, 61, 180, 498, 1323, 3405, 8557, 21103, …

Let b_h(m) be the number of rooted trees with m + 1 nodes and height at
most h (in edges). A tree of height at most h is a root over a multiset of
trees of height at most h − 1, so each b_h is the Euler transform of
b_{h−1}, and b_1 = 1 (the stars). The entry's a(n) = A001385(n) − A001384(n)
is then a(m + 1) = b_5(m) − b_4(m). This is [A000429](../A000429/)
(height 8) in rows of 5.

### Python 3 — 116 bytes

```python
L=[1]*5;n=0
while[print(L[-5]-L[-4])]:n-=5;exec("L+=sum(d*L[n-d-4]*sum(L[d::d])for d in range(n,0,5))//n,;"*4);L+=1,
```

**How it works**

- Taking the logarithmic derivative of
  Σ_m b_h(m)xᵐ = Π_{k≥1} (1 − xᵏ)^(−b_{h−1}(k−1)) gives the recurrence

  **m·b_h(m) = Σ_{k=1}^{m} k·b_{h−1}(k−1)·Σ_{j≥1} b_h(m − jk).**

- One list holds the layers in rows of 5: b_5(m), b_4(m), b_3(m), b_2(m),
  b_1(m) for m = 0, 1, …; every b_h(0) is 1, so `L=[1]*5` is row 0, and the
  last column, b_1 = 1, is a constant that `L+=1,` appends at the end of
  each row.
- When row m is built, n = −5m and d runs over −5m, …, −5, that is
  d = −5k. Each statement appends one entry, so the column being computed
  always ends at the end of the list, and `L[d::d]` steps back 5k places at
  a time through b_h(m − k), b_h(m − 2k), … of the same column. The factor
  −5 in d cancels against the one in n, and the division is exact by the
  identity.
- **The weight, from the end.** b_{h−1}(k − 1) sits in the next column of
  row k − 1. Counted from the end of the list it is at index
  −5(m − k) − 4 = `n-d-4`, whatever column is being appended, because the
  list grows by one entry per column; for b_2 the next column is the
  constant one. So the four computed columns run the same statement, and
  `exec("…;"*4)` repeats it.
- `L[-5]-L[-4]` is b_5(m) − b_4(m) of the last full row, the trees of
  height exactly 5 with m + 1 nodes; row 0 prints a(1) = 0.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(3000) has 896 digits, so the 4300-digit int-to-str limit is
  far beyond what the program reaches.
- About 3800 terms in 60 s here. The b-file has 200 terms (up to a(200));
  the bar is the whole b-file in 60 s, which prints in a fraction of a
  second.
- The previous record (122 bytes) kept rows of 4 without the constant
  column and gave the b_2 pass weight 1 with `**h`, h = 0:

  ```python
  L=[1]*4;n=0
  while[print(L[-4]-L[-3])]:
   n-=4
   for h in 1,1,1,0:L+=sum(d*L[n-d-3]**h*sum(L[d::d])for d in range(n,0,4))//n,
  ```

  It runs at the same speed (about 3800 terms in 60 s here as well).
  Reading that weight as `L[(n-d-3)*h]` is one byte longer still, and the
  constant column with `for _ in[1]*4:` and `L+=1,` on lines of their own
  instead of `exec` is 123 bytes, as on the A000429 page.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 122 | first entry |
| 2026-11-07 | Python 3 | 116 | constant column b_1 = 1 in rows of 5, `exec` for the four layers (as in A000429) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000342), CC BY-SA 4.0.
