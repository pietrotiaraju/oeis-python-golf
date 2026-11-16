# A001777

> Lah numbers: a(n) = n! * binomial(n-1, 4)/5!.
> — [OEIS A001777](https://oeis.org/A001777)

Offset 5: 1, 30, 630, 11760, 211680, 3810240, 69854400, 1317254400, 25686460800, 519437318400, …

### Python 3 — 45 bytes

```python
a=1;n=5
while[print(a)]:n+=1;a=a*n*~-n//(n-5)
```

**How it works**

- The Lah number L(n, k) = n!·C(n−1, k−1)/k! (here k = 5) counts the ways to
  split {1, …, n} into k non-empty ordered lists. Since
  C(n−1, k−1)/C(n−2, k−1) = (n−1)/(n−k), consecutive terms satisfy
  L(n, k) = L(n−1, k)·n(n−1)/(n−k).
- `a` starts at a(5) = 1; each pass moves `n` on and applies that ratio,
  `a=a*n*~-n//(n-5)` (`~-n` is n − 1). The quotient is the integer a(n), so
  the floor division is exact and every term is right.

**Notes**

- a(1556) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- Same length: `a=m=1` / `while[print(a)]:a=a*(m+5)*(m+4)//m;m+=1`
  (m = n − 4 before the step), or the walrus `a=a*n*(n:=n+1)//(n-5)`.
- The b-file has 96 terms (a(5) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Lah numbers: [A001286](../A001286/) (k = 2), [A001754](../A001754/) (k = 3), [A001755](../A001755/) (k = 4), [A001777](../A001777/) (k = 5), [A001778](../A001778/) (k = 6).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001777), CC BY-SA 4.0.
