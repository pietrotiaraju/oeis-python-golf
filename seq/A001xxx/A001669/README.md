# A001669

> Number of 7-level labeled rooted trees with n leaves.
> — [OEIS A001669](https://oeis.org/A001669)

Offset 0: 1, 1, 7, 70, 910, 14532, 274778, 5995892, 148154860, …

### Python 3 — 85 bytes

```python
t=1;Q=[[]]*6
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

- The e.g.f. in the entry is
  exp(exp(exp(exp(exp(exp(exp(x)−1)−1)−1)−1)−1)−1): start from B₀ = eˣ
  and substitute eˣ − 1 six times. Substituting eˣ − 1 into an e.g.f.
  with coefficients c(k) is the Stirling transform
  b(n) = Σ_k S(n, k)·c(k), S the Stirling numbers of the second kind.
- One transform runs on a table with T(0, k) = c(k) and
  T(i+1, k) = k·T(i, k) + T(i, k+1); then T(n, 0) = Σ_k S(n, k)·c(k)
  (induction on i, as on [A000405](../../A000xxx/A000405/)).
- Each list `L` of `Q` is an antidiagonal T(0, n), T(1, n−1), …,
  T(n−1, 1). Its last entry is also T(n, 0) = T(n−1, 1) (the weight is 0
  at k = 0), the level's output b(n). The next antidiagonal starts with
  the new input T(0, n+1) = `t` and adds (n − i)·T(i, n−i) to the
  previous new entry, for i = 0, …, n−1.
- `len(L)*L.pop(0)` supplies that weight and entry together: `len(L)` is
  evaluated before the pop, so the weights run n, n−1, …, 1 while `L` is
  consumed. `L*1` is a copy that only fixes the number of steps.
- `t` carries the last entry of one level into the next as its new input,
  so the six lists chain the six transforms. The innermost e.g.f. eˣ has
  every coefficient 1, hence `t=1` before each round; printing before the
  update gives a(0) = 1.

**Notes**

- Same program as [A000307](../../A000xxx/A000307/),
  [A000357](../../A000xxx/A000357/) and
  [A000405](../../A000xxx/A000405/) (3, 4 and 5 lists), with six lists
  for seven levels.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 151 terms (up to a(150)) and prints in about 0.15 s; the
  bar is the whole b-file in 60 s.
- a(1385) is the first term with more than 4300 digits, so printing stops
  there, after about 16 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001669), CC BY-SA 4.0.
