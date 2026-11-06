# A000382

> Restricted permutations.
> — [OEIS A000382](https://oeis.org/A000382)

Offset 4: 6, 11, 20, 36, 65, 119, 218, 400, 735, 1351, 2484, 4568, …

### Python 3 — 49 bytes

```python
a,b,c=1,3,6
while[print(c+(a>1))]:a,b,c=b,c,a+b+c
```

**How it works**

- The entry gives the recurrence a(n) = a(n−1) + a(n−2) + a(n−3) − 2,
  marked as conjectured (it is Plouffe's 1992 generating function
  (6 − z − 2z² − 4z³ − z⁴)/((1 − z)(1 − z − z² − z³))); it holds from
  n = 8 on.
- Then c(n) = a(n) − 1 satisfies the plain tribonacci recurrence, and
  for n ≥ 5 it is [A020992](https://oeis.org/A020992)(n) (0, 2, 1, 3, 6,
  10, 19, 35, …). The window `a,b,c` walks A020992 from
  (A020992(2), A020992(3), A020992(4)) = (1, 3, 6) with the tuple update
  of [A000213](../A000213/).
- The first term breaks the pattern: a(4) = 6 = A020992(4), not
  A020992(4) + 1. `c+(a>1)` adds 1 on every pass but the first, when the
  oldest entry a is still 1.

**Notes**

- Correctness beyond the first terms rests on the conjectured
  recurrence above. The b-file (997 terms, n = 4 to 1000, V. Librandi) is
  itself computed from it, and the program prints all of it at once; the
  bar is the whole b-file in 60 s. Only the 4300-digit int-to-str limit
  of Python 3.11+ stops the program, after about 16000 terms.
- What the terms count is not settled here: the entry says "the fourth
  column of A008305, divided by 4", but that is the permanent of
  I + P + P² + P³ (P the n-cycle) over 4, which is 264/4 = 66 at n = 8,
  not 65; the two agree only for n ≤ 7 (the permanent minus 4·a(n) is
  4, 8, 16, 32, 60, … for n = 8, 9, 10, …). No set of at most
  five allowed displacements in −3 … 4, cyclic or not, reproduces the
  terms.
- Keeping a(n) itself, with `-2` in the update and a patch for a(4), is
  53 bytes, and a window of four values in which a(4) never enters the
  recurrence is 56.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000382), CC BY-SA 4.0.
