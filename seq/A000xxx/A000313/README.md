# A000313

> Number of permutations of length n with 3 consecutive ascending pairs.
> — [OEIS A000313](https://oeis.org/A000313)

Offset 1: 0, 0, 0, 1, 4, 30, 220, 1855, 17304, 177996, 2002440, …

### Python 3 — 43 bytes

```python
e=m=0
while[print(e*~-m//6)]:m+=1;e=(e^1)*m
```

**How it works**

- The terms count permutations of [n] with exactly three successions
  (an entry followed by the next integer): glue 3 of the n − 1 pairs
  (i, i+1), C(n−1, 3) ways, and arrange the n − 3 blocks with no new
  succession, [A000255](https://oeis.org/A000255)(n−4) ways. Since
  A000255(k) = D(k+2)/(k+1) with D = [A000166](../A000166/), this is
  a(n) = (n−1)(n−2)·D(n−2)/6, the formula in the OEIS entry; it is 0 for
  n = 1, 2, 3 as well.
- The counter is m = n − 1, and the program keeps e = m·D(m−1), so a(n)
  is e·(m−1)/6, `e*~-m//6`.
- As in [A000387](../A000387/): D(m) = m·D(m−1) + (−1)^m and D(m) is odd
  exactly when m is even, so e = D(m) xor 1. The next value
  (m+1)·D(m) is therefore `(e^1)*m` once m has been stepped, which is
  why `m+=1` comes first.
- With e = m = 0 the first pass prints 0 and makes e = 1 = 1·D(0), so no
  seed is needed.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (450 terms, n = 1 to 450) prints at once; the program stops after
  a(1558), when the next term passes the 4300-digit int-to-str limit of
  Python 3.11+. The bar is the whole b-file in 60 s.
- With the counter n itself, `e=0;n=1` /
  `while[print(e*(n-2)//6)]:e=(e^1)*n;n+=1`, it is 47 bytes; stepping
  after the update with m = n − 1 (`e=(e^1)*-~m;m+=1`) is 45.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000313), CC BY-SA 4.0.
