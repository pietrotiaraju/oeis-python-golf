# A001778

> Lah numbers: a(n) = n!*binomial(n-1,5)/6!.
> — [OEIS A001778](https://oeis.org/A001778)

Offset 6: 1, 42, 1176, 28224, 635040, 13970880, 307359360, 6849722880, 155831195520, 3636061228800, …

### Python 3 — 45 bytes

```python
a=1;n=6
while[print(a)]:n+=1;a=a*n*~-n//(n-6)
```

**How it works**

- The Lah number L(n, k) = n!·C(n−1, k−1)/k! (here k = 6) counts the ways to
  split {1, …, n} into k non-empty ordered lists. Since
  C(n−1, k−1)/C(n−2, k−1) = (n−1)/(n−k), consecutive terms satisfy
  L(n, k) = L(n−1, k)·n(n−1)/(n−k).
- `a` starts at a(6) = 1; each pass moves `n` on and applies that ratio,
  `a=a*n*~-n//(n-6)` (`~-n` is n − 1). The quotient is the integer a(n), so
  the floor division is exact and every term is right.

**Notes**

- a(1555) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- Same length: `a=m=1` / `while[print(a)]:a=a*(m+6)*(m+5)//m;m+=1`
  (m = n − 5 before the step), or the walrus `a=a*n*(n:=n+1)//(n-6)`.
- The b-file has 95 terms (a(6) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Lah numbers: [A001286](../A001286/) (k = 2), [A001754](../A001754/) (k = 3), [A001755](../A001755/) (k = 4), [A001777](../A001777/) (k = 5), [A001778](../A001778/) (k = 6).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001778), CC BY-SA 4.0.
