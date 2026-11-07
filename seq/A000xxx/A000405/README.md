# A000405

> Number of 6-level labeled rooted trees with n leaves.
> — [OEIS A000405](https://oeis.org/A000405)

Offset 0: 1, 1, 6, 51, 561, 7556, 120196, 2201856, 45592666, 1051951026, …

### Python 3 — 85 bytes

```python
t=1;Q=[[]]*5
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

- The e.g.f. in the entry is exp(exp(exp(exp(exp(exp(x)−1)−1)−1)−1)−1):
  start from B₀ = eˣ and substitute eˣ − 1 five times. Substituting
  eˣ − 1 into an e.g.f. with coefficients c(k) is the Stirling transform
  b(n) = Σ_k S(n, k)·c(k), S the Stirling numbers of the second kind.
- One transform runs on a table with T(0, k) = c(k) and
  T(i+1, k) = k·T(i, k) + T(i, k+1); then T(n, 0) = Σ_k S(n, k)·c(k)
  (induction on i: T(i, k) = Σ_j A(i, k, j)·c(j) where A obeys the same
  recurrence, and A(n, 0, j) = S(n, j); checked numerically for n < 10).
- Each list `L` of `Q` is an antidiagonal T(0, n), T(1, n−1), …,
  T(n−1, 1). Its last entry is also T(n, 0) = T(n−1, 1) (the weight is 0
  at k = 0), the level's output b(n). The next antidiagonal starts with
  the new input T(0, n+1) = `t` and adds (n − i)·T(i, n−i) to the
  previous new entry, for i = 0, …, n−1.
- `len(L)*L.pop(0)` supplies that weight and entry together: `len(L)` is
  evaluated before the pop, so the weights run n, n−1, …, 1 while `L` is
  consumed. `L*1` is a copy that only fixes the number of steps.
- `t` carries the last entry of one level into the next as its new input,
  so the five lists chain the five transforms. The innermost e.g.f. eˣ has
  every coefficient 1, hence `t=1` before each round; printing before the
  update gives a(0) = 1.
- `Q=[[]]*5` is five references to one empty list, but the first round
  pops nothing from it and builds five separate lists `[1]`.

**Notes**

- Same program as [A000307](../A000307/) (three lists) and
  [A000357](../A000357/) (four). Weighting with
  `(len(L)-i)*x for i,x in enumerate(L)` instead of popping is 9 bytes
  longer. [A000406](../A000406/) does the first-kind (logarithm) version.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 151 terms (up to a(150)) and prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(1423) is the first term with more than 4300 digits, so printing stops
  there, after about 12 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000405), CC BY-SA 4.0.
