# A001095

> a(n) = n + n*(n-1)*(n-2)*(n-3)*(n-4).
> — [OEIS A001095](https://oeis.org/A001095)

Offset 0: 0, 1, 2, 3, 4, 125, 726, 2527, 6728, 15129, …

### Python 3 — 39 bytes

```python
n=0
while[print(n*(n*n-5*n+5)**2)]:n+=1
```

**How it works**

- With w = n² − 5n + 5 the four factors after n pair up as
  (n−1)(n−4) = w − 1 and (n−2)(n−3) = w + 1, so their product is w² − 1.
- Then n + n·(w² − 1) = n·w²: the added n cancels the −1, and
  a(n) = n·(n² − 5n + 5)², a perfect square times n.

**Notes**

- The definition as written, `n*(n-1)*(n-2)*(n-3)*(n-4)+n`, makes a
  50-byte program.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s.
- Siblings with four and six factors: [A001094](../A001094/) and
  [A001096](../A001096/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001095), CC BY-SA 4.0.
