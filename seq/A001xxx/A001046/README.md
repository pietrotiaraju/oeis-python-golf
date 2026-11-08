# A001046

> a(n) = n*(n-1)*a(n-1)/2 + a(n-2), a(0) = a(1) = 1.
> — [OEIS A001046](https://oeis.org/A001046)

Offset 0: 1, 1, 2, 7, 44, 447, 6749, 142176, 3987677, 143698548, 6470422337, …

### Python 3 — 47 bytes

```python
a=b=n=1
while[print(a)]:n+=1;a,b=b,b*n*~-n//2+a
```

**How it works**

- `a` and `b` hold a(n−2) and a(n−1), starting from a(0) = a(1) = 1 with
  `n` = 1. Each pass increments `n` and computes
  a(n) = C(n,2)·a(n−1) + a(n−2), where C(n,2) = n(n−1)/2.
- `~-n` is n − 1, so `b*n*~-n//2` is b·n·(n−1)/2. The product n·(n−1) is
  always even, so the floor division is exact.
- `a,b=b,…` shifts the pair; `print(a)` in the loop condition prints a(0)
  first and then each term once.

**Notes**

- The twin [A001052](../A001052/) is the same program with a(1) = 2.
- Keeping the triangular number in its own counter, `a=b=t=n=1` with
  `a,b=b,t*b+a;n+=1;t+=n`, is also 47 bytes; a walrus counter one step
  behind, `b*n*(n:=n+1)//2`, is the same length as `n+=1;` plus `~-n`.
- a(−1) = a(1) − C(1,2)·a(0) = 1, so starting a step earlier changes
  nothing.
- Exact integers. Python's 4300-digit int-to-str limit stops the program
  at a(906), the first term with 4301 digits, after printing a(0) to
  a(905).
- The b-file has 101 terms (a(0) to a(100), 285 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001046), CC BY-SA 4.0.
