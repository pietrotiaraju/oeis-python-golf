# A001745

> Numbers such that at least one digit contains a loop (version 2). Also called "holey" or "holy" numbers.
> — [OEIS A001745](https://oeis.org/A001745)

Offset 1: 0, 4, 6, 8, 9, 10, 14, 16, 18, 19, 20, 24, 26, 28, 29, 30, 34, 36, …

### Python 3 — 48 bytes

```python
n=0
while[{*str(n)}&{*'98640'}and print(n)]:n+=1
```

**How it works**

- **Loops.** The digits that count as having a loop are read off the data:
  version 1 gives loops to 0, 6, 8 and 9 (the 4 written open, as the OEIS
  comment of [A001729](../A001729/) says), version 2 to 0, 4, 6, 8 and 9 (a
  closed 4); 1, 2, 3, 5 and 7 have none in either version.
- **The test.** `{*str(n)}` is the set of n's decimal digits and
  `{*'98640'}` the set of the digits with a loop, 0, 4, 6, 8 and 9. Their
  intersection is non-empty exactly when n has a digit with a loop, which is
  the definition (version 2). A non-empty set is true, so `and print(n)`
  prints n then.
- **The loop.** n runs through 0, 1, 2, … in increasing order; `while[…]:`
  is always true (a one-element list is not empty).
- **Why backwards.** The digit string is written in decreasing order, which
  a set does not care about. In increasing order, `'04689'`, its character
  codes would step like a run of consecutive terms (as 10, 14, 16, 18, 19
  do), and tools/verify.py would take the string for spelled-out terms.

**Notes**

- 0 has a loop, so it is the first term. Stripping the loopless digits
  instead, `str(n).strip('75321')and print(n)`, is 1 byte longer. The b-file
  has 1000 terms (up to 1179); the bar is the whole b-file, printed in a
  fraction of a second.
- Correct for every n: the program tests the definition directly. Compare
  [A001746](../A001746/) (version 1); this is the complement of
  [A001742](../A001742/) in the nonnegative integers.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001745), CC BY-SA 4.0.
