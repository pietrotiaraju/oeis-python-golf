# A000174

> Number of partitions of n into 5 squares.
> — [OEIS A000174](https://oeis.org/A000174)

Offset 0: 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, …

### Python 3 — 89 bytes

```python
g=lambda t,i=0:t<1or i*i<=t%m<t and g(t-i*i-m,i)+g(t,i+1)
m=1
while[print(g(6*m-1))]:m+=1
```

**How it works**

- A partition of n into 5 squares (zeros allowed) is a non-decreasing
  list of roots i₁ ≤ … ≤ i₅ with Σ i² = n. With m = n + 1, every part i
  is given the weight i² + m, and the five parts must add up to
  t = n + 5m = 6m − 1.
- Inside the recursion t = r + c·m, where r < m is the square sum still
  to place and c the number of parts still to place, so `t%m` is r and
  `t%m<t` holds exactly when c ≥ 1. The one parameter t does the work
  of two (remaining sum and part counter).
- `i*i<=t%m<t` lets part i in only if it fits and a part is left;
  `g(t-i*i-m,i)` places it (the next part may repeat it, so the list
  stays non-decreasing) and `g(t,i+1)` moves on to larger parts. t never
  goes negative, so `t<1` means "everything placed": c = 0 and r = 0.
  Zeros are the parts with i = 0, which fill the slots left once r = 0.
- The top call never hits the base case, so it returns an int and `print`
  shows 1 rather than `True`.
- The plain version with a separate counter,
  `g=lambda n,k=5,i=1:n<1or k>0<i*i<=n and g(n-i*i,k-1,i)+g(n,k,i+1)`
  (at most five positive squares), is 94 bytes with its driver.

**Notes**

- Exact integer arithmetic, correct for every n. The recursion visits the
  non-decreasing partial lists, O(n²) of them per term; its depth is
  about √n, far below the recursion limit. About 1300 terms come out in
  60 s on the machine that set the bar, which is 1000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000174), CC BY-SA 4.0.
