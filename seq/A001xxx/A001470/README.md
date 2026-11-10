# A001470

> Number of degree-n permutations of order dividing 3.
> — [OEIS A001470](https://oeis.org/A001470)

Offset 0: 1, 1, 1, 3, 9, 21, 81, 351, 1233, 5769, 31041, 142011, 776601, 4874013, 27027729, …

### Python 3 — 50 bytes

```python
a=b=c=n=1
while[print(a)]:a,b,c=b,c,c+n*-~n*a;n+=1
```

**How it works**

- The order of a permutation divides 3 exactly when every cycle has
  length 1 or 3. Point n is fixed, or it lies in a 3-cycle, which is fixed
  by the ordered pair of the two points that follow it: (n−1)(n−2) ways.
  So **a(n) = a(n−1) + (n−1)(n−2)·a(n−3)** with a(0) = a(1) = a(2) = 1
  (the general rule: a(n) = Σ_{d|k} (n−1)!/(n−d)!·a(n−d) for order
  dividing k).
- `a`, `b`, `c` hold a(m−1), a(m), a(m+1) with `n` = m, so
  `c+n*-~n*a` = a(m+1) + (m+1)·m·a(m−1) = a(m+2). The start m = 1
  needs a(0) = a(1) = a(2) = 1 and n = 1: one chained assignment.

**Notes**

- [A001471](../A001471/) (order exactly 3) is the same program
  printing `a-1`.
- Exact integer arithmetic, so the program is right for every n; the
  4300-digit int-to-str limit stops it at a(2214).
- The b-file has 632 terms (n = 0 to 631); all of them print in well under
  a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001470), CC BY-SA 4.0.
