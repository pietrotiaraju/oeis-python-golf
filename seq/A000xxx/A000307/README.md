# A000307

> Number of 4-level labeled rooted trees with n leaves.
> — [OEIS A000307](https://oeis.org/A000307)

Offset 0: 1, 1, 4, 22, 154, 1304, 12915, 146115, 1855570, 26097835, 402215465, 6734414075, 121629173423, 2355470737637, …

### Python 3 — 85 bytes

```python
t=1;Q=[[]]*3
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

- The e.g.f. is exp(exp(exp(exp(x)−1)−1)−1). Each exp(·−1) is a Stirling
  transform: a(n) = Σ_k S(n, k)·b(k), where b is the sequence one level
  down. So a is the Stirling transform of the Stirling transform of the
  Stirling transform of 1, 1, 1, …
- This is the program of [A000258](../A000258/) (three exponentials) with
  one more level; see that page for the triangle T(i+1, k) = k·T(i, k) +
  T(i, k+1), whose antidiagonals the program keeps, one list per level.
  The head of each new antidiagonal is the newest term of the level below,
  carried over in `t`, and the last list ends with the next term.
- `Q=[[]]*3` is step 0: three references to one empty list. That is safe
  because the first pass pops nothing from an empty list and builds three
  new, separate lists `[1]`. It is 2 bytes under `Q=[],[],[]`.

**Notes**

- `len(L)*L.pop(0)`: while the comprehension runs over the copy `L*1`, L
  still holds the old entries from position i on, so `len(L)` is the
  weight and `pop(0)` hands over the entry; `len(L)` is evaluated first.
- The number of levels is the number in `[[]]*3`: `[[]]*4` prints
  [A000357](https://oeis.org/A000357) (5 levels) at the same length.
- Exact integer arithmetic, so the program is right for every n. Python
  3.11+ stops with a `ValueError` at the first term with more than 4300
  digits (the int-to-str limit), which is not counted as a failure.
- The b-file has 441 terms (n = 0 to 440); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000307), CC BY-SA 4.0.
