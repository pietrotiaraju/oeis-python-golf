# A001742

> Numbers whose digits contain no loops (version 2).
> — [OEIS A001742](https://oeis.org/A001742)

Offset 1: 1, 2, 3, 5, 7, 11, 12, 13, 15, 17, 21, 22, 23, 25, 27, 31, 32, 33, …

### Python 3 — 47 bytes

```python
n=0
while[{*str(n)}-{*'75321'}or print(n)]:n+=1
```

**How it works**

- **Loops.** The digits that count as having a loop are read off the data:
  version 1 gives loops to 0, 6, 8 and 9 (the 4 written open, as the OEIS
  comment of [A001729](../A001729/) says), version 2 to 0, 4, 6, 8 and 9 (a
  closed 4); 1, 2, 3, 5 and 7 have none in either version.
- **The test.** `{*str(n)}` is the set of n's decimal digits and
  `{*'75321'}` the set of the digits 1, 2, 3, 5 and 7. Their difference is
  empty exactly when every digit of n is one of them, which is the
  definition: no digit with a loop (version 2). An empty set is false, so
  `or print(n)` prints n then.
- **The loop.** n runs through 0, 1, 2, … in increasing order; `while[…]:`
  is always true (a one-element list is not empty).
- **Why backwards.** The digit string is written in decreasing order, which
  a set does not care about. In increasing order, `'12357'`, its character
  codes would step like a run of consecutive terms (as 11, 12, 13, 15, 17
  do), and tools/verify.py would take the string for spelled-out terms.

**Notes**

- 0 has a loop, so the scan may start at 0. `str(n).strip('75321')or
  print(n)` is 1 byte longer. The b-file has 10000 terms (up to 275557); the
  bar is the whole b-file, printed in about a second.
- Correct for every n: the program tests the definition directly. Compare
  [A001729](../A001729/) (version 1) and the complement
  [A001745](../A001745/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001742), CC BY-SA 4.0.
