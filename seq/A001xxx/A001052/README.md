# A001052

> a(n) = n*(n-1)*a(n-1)/2 + a(n-2), a(0) = 1, a(1) = 2.
> — [OEIS A001052](https://oeis.org/A001052)

Offset 0: 1, 2, 3, 11, 69, 701, 10584, 222965, 6253604, 225352709, 10147125509, …

### Python 3 — 49 bytes

```python
a=n=1;b=2
while[print(a)]:n+=1;a,b=b,b*n*~-n//2+a
```

**How it works**

- `a` and `b` hold a(n−2) and a(n−1), starting from a(0) = 1, a(1) = 2
  with `n` = 1. Each pass increments `n` and computes
  a(n) = C(n,2)·a(n−1) + a(n−2), where C(n,2) = n(n−1)/2.
- `~-n` is n − 1, so `b*n*~-n//2` is b·n·(n−1)/2. The product n·(n−1) is
  always even, so the floor division is exact.
- `a,b=b,…` shifts the pair; `print(a)` in the loop condition prints a(0)
  first and then each term once.

**Notes**

- The twin [A001046](../A001046/) is the same program with a(1) = 1, where
  the start collapses to `a=b=n=1` (47 bytes).
- Starting one step earlier, from a(−1) = a(1) − C(1,2)·a(0) = 2, and
  printing `b` (`a=2;b=n=1` / `while[print(b)]:a,b=b,b*n*~-n//2+a;n+=1`) is
  also 49 bytes.
- Exact integers. Python's 4300-digit int-to-str limit stops the program
  at a(906), the first term with 4301 digits, after printing a(0) to
  a(905).
- The b-file has 101 terms (a(0) to a(100), 285 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001052), CC BY-SA 4.0.
