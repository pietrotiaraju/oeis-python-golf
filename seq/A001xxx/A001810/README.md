# A001810

> a(n) = n!*n*(n-1)*(n-2)/36.
> — [OEIS A001810](https://oeis.org/A001810)

Offset 0: 0, 0, 0, 1, 16, 200, 2400, 29400, 376320, 5080320, 72576000, 1097712000, …

### Python 3 — 47 bytes

```python
f=n=-1
while[print(f*~n*n*~-n//36)]:n+=1;f*=n+1
```

**How it works**

- a(m) = m!·m(m − 1)(m − 2)/36 = m!·C(m, 3)/6 is the total number of
  321 patterns over all permutations of [m]: each of the C(m, 3) triples
  is decreasing in one sixth of the m! permutations. So it is an integer
  for every m.
- The counter runs one behind: `n` is m − 1, so it starts at −1, and
  `f` is −m! = −(n + 1)!, which starts at −0! = −1. Both start values are
  −1, so one chained assignment `f=n=-1` sets them; each pass moves `n`
  on and multiplies `f` by the new n + 1 = m.
- `~n` is −(n + 1) = −m and `~-n` is n − 1 = m − 2, so
  `f*~n*n*~-n` is (−m!)·(−m)(m − 1)(m − 2) = 36·a(m), and the floor
  division by 36 is exact. For m = 0, 1, 2 one factor is 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The plain counter, `f=1;n=0` / `while[print(f*n*~-n*(n-2)//36)]:n+=1;f*=n`,
  is 49 bytes; the shifted counter with a positive factorial needs
  `f=1;n=-1` (also 49). `f*(n-n**3)//36` is the same length as
  `f*~n*n*~-n//36`.
- The ratio a(m) = a(m − 1)·m²/(m − 3) that gives [A001805](../A001805/)
  = 6a(m) in 43 bytes cannot start from the zero terms a(0), a(1), a(2).
- a(1556) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 49 | first entry |
| 2026-11-16 | Python 3 | 47 | counter one behind, f = −(n + 1)!: start `f=n=-1` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001810), CC BY-SA 4.0.
