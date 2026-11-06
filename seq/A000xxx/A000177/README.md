# A000177

> Number of partitions of n into 6 squares.
> — [OEIS A000177](https://oeis.org/A000177)

Offset 0: 1, 1, 1, 1, 2, 2, 2, 1, 2, 3, …

### Python 3 — 94 bytes

```python
f=lambda n,k=6,i=1:(n==1)+sum(f(n-j*j,k-1,j)for j in range(i,n*k))
n=1
while[print(f(n))]:n+=1
```

**How it works**

- Zero is allowed as a part, so a partition into 6 squares is the same as
  a partition into at most 6 positive squares. `f` counts those, with the
  roots in increasing order: `k` parts may still be added, the next root
  is at least `i`, and `n` is the remaining sum plus one.
- The `+1` shift lets the root range be `range(i,n)` instead of
  `range(i,n+1)`, and the main loop starts at `n=1`, which costs nothing.
- `(n==1)` counts the partition that stops here (remaining sum 0); a
  bigger root would leave a negative sum, and a negative `n` gives an empty
  range, so it adds 0.
- `range(i,n*k)` folds in the part limit: with `k=0` the range is empty,
  4 bytes under `k and`. For `k ≥ 1` the extra roots past `n` only lead to
  negative sums.
- `(n==1)+` is the same length as `n==1or`, but it keeps the result an
  int, so the top call prints `1` for a(0) instead of `True`.

**Notes**

- Exact integer arithmetic, correct for every n. Each call scans up to
  `n*k` roots, most of them dead ends, so terms slow down quickly: about
  276 terms come out in 60 s on the machine that set the bar, which is
  200 terms in 60 s. Recursion depth is at most 7.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000177), CC BY-SA 4.0.
