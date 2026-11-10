# A001472

> Number of degree-n permutations of order dividing 4.
> — [OEIS A001472](https://oeis.org/A001472)

Offset 0: 1, 1, 2, 4, 16, 56, 256, 1072, 6224, 33616, 218656, 1326656, 9893632, 70186624, …

### Python 3 — 66 bytes

```python
a=b=c=d=n=1
while[print(c)]:a,b,c,d=b,c,d,d+n*(c+~-n*(n-2)*a);n+=1
```

**How it works**

- The order of a permutation divides 4 exactly when every cycle has
  length 1, 2 or 4. Point n+1 is fixed, or in a 2-cycle (n choices), or in
  a 4-cycle, fixed by the ordered triple of the points that follow it
  (n(n−1)(n−2) ways). So
  **a(n+1) = a(n) + n·a(n−1) + n(n−1)(n−2)·a(n−3)**
  (the rule a(n) = Σ_{d|k} (n−1)!/(n−d)!·a(n−d) for k = 4).
- `a`, `b`, `c`, `d` hold a(n−3), a(n−2), a(n−1), a(n), and
  `d+n*(c+~-n*(n-2)*a)` is the right-hand side with n factored out
  (`~-n` is n−1). The program prints `c`, one step behind.
- The start is n = 1 with c = a(0) = 1 and d = a(1) = 1; `a` and `b` stand
  for a(−2) and a(−1), which are only ever multiplied by
  n(n−1)(n−2) = 0 (at n = 1 and 2), so they can be 1 too and the whole
  start is one chain `a=b=c=d=n=1`.

**Notes**

- [A001473](../A001473/) (order exactly 4) adds the involutions to the
  same loop.
- Exact integer arithmetic, so the program is right for every n; the
  4300-digit int-to-str limit stops it at a(1996).
- The b-file has 571 terms (n = 0 to 570); all of them print in well under
  a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001472), CC BY-SA 4.0.
