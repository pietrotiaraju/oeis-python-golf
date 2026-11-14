# A001744

> Numbers n such that every digit contains a loop (version 2).
> — [OEIS A001744](https://oeis.org/A001744)

Offset 1: 0, 4, 6, 8, 9, 40, 44, 46, 48, 49, 60, 64, 66, 68, 69, 80, 84, 86, …

### Python 3 — 47 bytes

```python
n=0
while[{*str(n)}-{*'98640'}or print(n)]:n+=1
```

**How it works**

- **Loops.** The digits that count as having a loop are read off the data:
  version 1 gives loops to 0, 6, 8 and 9 (the 4 written open, as the OEIS
  comment of [A001729](../A001729/) says), version 2 to 0, 4, 6, 8 and 9 (a
  closed 4); 1, 2, 3, 5 and 7 have none in either version.
- **The test.** `{*str(n)}` is the set of n's decimal digits and
  `{*'98640'}` the set of the digits 0, 4, 6, 8 and 9. Their difference is
  empty exactly when every digit of n is one of them, which is the
  definition: every digit has a loop (version 2). An empty set is false, so
  `or print(n)` prints n then.
- **The loop.** n runs through 0, 1, 2, … in increasing order; `while[…]:`
  is always true (a one-element list is not empty).
- **Why backwards.** The digit string is written in decreasing order, which
  a set does not care about. In increasing order, `'04689'`, its character
  codes would step like a run of consecutive terms (as 40, 44, 46, 48, 49
  do), and tools/verify.py would take the string for spelled-out terms.

**Notes**

- The terms are the base-5 numerals with the digits 0 to 4 replaced by 0, 4,
  6, 8, 9 (Hieronymus Fischer's formula in the OEIS entry), which as a
  recursive lambda is 71 bytes; `str(n).strip('98640')or print(n)` is 1 byte
  longer than the set difference. The b-file has 10000 terms (up to 809999);
  the bar is the whole b-file, printed in about a second.
- Correct for every n: the program tests the definition directly. Compare
  [A001743](../A001743/) (version 1).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001744), CC BY-SA 4.0.
