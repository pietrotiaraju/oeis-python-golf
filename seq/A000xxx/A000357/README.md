# A000357

> Number of 5-level labeled rooted trees with n leaves.
> — [OEIS A000357](https://oeis.org/A000357)

Offset 0: 1, 1, 5, 35, 315, 3455, 44590, 660665, 11035095, 204904830, 4183174520, 93055783320, 2238954627848, …

### Python 3 — 85 bytes

```python
t=1;Q=[[]]*4
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

- The e.g.f. is exp(exp(exp(exp(exp(x)−1)−1)−1)−1). Each exp(·−1) is a
  Stirling transform: a(n) = Σ_k S(n, k)·b(k), where b is the sequence one
  level down, so a is four Stirling transforms applied to 1, 1, 1, …
- This is the program of [A000258](../A000258/) (three exponentials) with
  two more levels; see that page for the triangle T(i+1, k) = k·T(i, k) +
  T(i, k+1), whose antidiagonals the program keeps, one list per level.
  The head of each new antidiagonal is the newest term of the level below,
  carried over in `t`, and the last list ends with the next term.
- `Q=[[]]*4` is step 0: four references to one empty list. That is safe
  because the first pass pops nothing from an empty list and builds four
  new, separate lists `[1]`. It is 5 bytes under `Q=[],[],[],[]`.

**Notes**

- `len(L)*L.pop(0)`: while the comprehension runs over the copy `L*1`, L
  still holds the old entries from position i on, so `len(L)` is the
  weight and `pop(0)` hands over the entry; `len(L)` is evaluated first.
- The same program with `[[]]*3` is [A000307](../A000307/) (4 levels).
- Exact integer arithmetic, so the program is right for every n. Python
  3.11+ stops with a `ValueError` at the first term with more than 4300
  digits (the int-to-str limit), which is not counted as a failure.
- The b-file has 401 terms (n = 0 to 400); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000357), CC BY-SA 4.0.
