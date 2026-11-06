# A000258

> Expansion of e.g.f. exp(exp(exp(x)-1)-1).
> — [OEIS A000258](https://oeis.org/A000258)

Offset 0: 1, 1, 3, 12, 60, 358, 2471, 19302, 167894, 1606137, 16733779, 188378402, 2276423485, 29367807524, 402577243425, 5840190914957, …

### Python 3 — 84 bytes

```python
t=1;Q=[],[]
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

- a(n) = Σ_k S(n, k)·B(k): split {1, …, n} into blocks, then split the set
  of blocks. That is the Stirling transform of the Bell numbers B, which are
  themselves the Stirling transform of 1, 1, 1, …
- One triangle gives the Stirling transform of any sequence c without
  Stirling numbers: T(0, k) = c(k) and T(i+1, k) = k·T(i, k) + T(i, k+1).
  Then T(n, 0) = Σ_j S(n, j)·c(j). The reason: T(i, k) sums c(k + j) over
  the ways to put i labelled items into k given boxes, some of them
  perhaps left empty, plus j new non-empty blocks. Item 1 either goes
  into one of the k boxes (k·T(i−1, k)) or opens a new block, which then
  counts as one more given box (T(i−1, k+1)).
- To print forever, the program keeps one antidiagonal per level,
  L = [T(0, n), T(1, n−1), …, T(n−1, 1)]. The next one starts with the
  new head T(0, n+1) = c(n+1), and each entry adds a weighted old entry:
  T(i+1, n−i) = T(i, n+1−i) + (n−i)·T(i, n−i). Its last entry is
  T(n, 1) = 0·T(n, 0) + T(n, 1) = T(n+1, 0), the next term.
- `len(L)*L.pop(0)`: while the comprehension runs over the copy `L*1`,
  L still holds the old entries from position i on, so `len(L)` is the
  weight n−i and `pop(0)` hands over T(i, n−i). Python evaluates
  `len(L)` before the `pop`.
- Two levels, one comprehension. The first list is the triangle of
  c = 1, 1, 1, …, so its head is always 1 (the `t=1`), and it ends with
  B(n+1). That is exactly the head the second list (c = B) needs, so `t`
  simply carries over into its `[t]`. The second list ends with a(n+1),
  which the next `print(t)` prints.
- `Q=[],[]` is step 0, with both antidiagonals empty; the first
  `print(t)` gives a(0) = 1.

**Notes**

- The number of lists is the number of exponentials: `Q=[],` prints the
  Bell numbers [A000110](../A000110/) (that record's Aitken triangle is
  shorter), and `Q=[],[],[]` prints
  [A000307](https://oeis.org/A000307), exp(exp(exp(exp(x)−1)−1)−1).
- A counter for the weights (`k:=k-1`, reset to `n` for each list, plus
  `n+=1`) is 10 bytes longer. The convolution
  a(n+1) = Σ C(n, k)·B(k+1)·a(n−k) needs `math.comb` and a separate Bell
  triangle, and is longer still.
- Exact integer arithmetic, so the program is right for every n.
  a(1671) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit, which is not
  counted as a failure.
- The b-file has 476 terms (n = 0 to 475); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000258), CC BY-SA 4.0.
