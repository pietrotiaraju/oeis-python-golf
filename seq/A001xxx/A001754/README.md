# A001754

> Lah numbers: a(n) = n!*binomial(n-1,2)/6.
> — [OEIS A001754](https://oeis.org/A001754)

Offset 1: 0, 0, 1, 12, 120, 1200, 12600, 141120, 1693440, 21772800, …

### Python 3 — 45 bytes

```python
f=n=1
while[print(f*~-n*(n-2)//12)]:n+=1;f*=n
```

**How it works**

- a(n) = n!·C(n−1, 2)/3! is the Lah number L(n, 3): the number of ways to
  split {1, …, n} into 3 non-empty ordered lists. Written out,
  a(n) = n!·(n−1)(n−2)/12.
- `f` holds n! (`f=n=1`, then `n+=1;f*=n`), `~-n` is n − 1, and the product
  n!(n−1)(n−2) is a multiple of 12 (n!/6 is an integer from n = 3 on and
  (n−1)(n−2) is even), so `//12` is exact.
- For n = 1 and 2 the factor (n−1)(n−2) vanishes, which gives the two
  leading zeros of the data with no special case.

**Notes**

- Exact integer arithmetic, correct for every n. a(1557) is the first term
  over 4300 digits, so Python's int-to-str limit stops the program there.
- The ratio recurrence of the other Lah columns,
  `a=1;n=3` / `while[print(a)]:n+=1;a=a*n*~-n//(n-3)`, is also 45 bytes but
  starts at a(3) and cannot produce the two zeros; keeping (n+1)! instead,
  `f=1;m=0` / `while[print(f*m*~-m//12)]:m+=1;f*=m+1`, ties at 45.
- The b-file has 300 terms (a(1) to a(300)); the bar is the whole b-file
  in 60 s, which prints instantly.
- Lah numbers: [A001286](../A001286/) (k = 2), [A001754](../A001754/) (k = 3), [A001755](../A001755/) (k = 4), [A001777](../A001777/) (k = 5), [A001778](../A001778/) (k = 6).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001754), CC BY-SA 4.0.
