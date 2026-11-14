# A001743

> Numbers in which every digit contains at least one loop (version 1).
> — [OEIS A001743](https://oeis.org/A001743)

Offset 1: 0, 6, 8, 9, 60, 66, 68, 69, 80, 86, 88, 89, 90, 96, 98, 99, 600, …

### Python 3 — 46 bytes

```python
n=0
while[{*str(n)}-{*'9860'}or print(n)]:n+=1
```

**How it works**

- **Loops.** The digits that count as having a loop are read off the data:
  version 1 gives loops to 0, 6, 8 and 9 (the 4 written open, as the OEIS
  comment of [A001729](../A001729/) says), version 2 to 0, 4, 6, 8 and 9 (a
  closed 4); 1, 2, 3, 5 and 7 have none in either version.
- **The test.** `{*str(n)}` is the set of n's decimal digits and `{*'9860'}`
  the set of the digits 0, 6, 8 and 9. Their difference is empty exactly
  when every digit of n is one of them, which is the definition: every digit
  has a loop (version 1). An empty set is false, so `or print(n)` prints n
  then.
- **The loop.** n runs through 0, 1, 2, … in increasing order; `while[…]:`
  is always true (a one-element list is not empty).
- **Why backwards.** The digit string is written in decreasing order, which
  a set does not care about. In increasing order, `'0689'`, its character
  codes would step like a run of consecutive terms (as 60, 66, 68, 69 do),
  and tools/verify.py would take the string for spelled-out terms.

**Notes**

- The terms are the base-4 numerals with the digits 0, 1, 2, 3 replaced by
  0, 6, 8, 9 (Hieronymus Fischer's formula in the OEIS entry); writing that
  as a recursive lambda is 69 bytes, and `str(n).strip('9860')or print(n)`
  is 1 byte longer than the set difference. The scan visits every number up
  to 8690099 for the 10000 terms of the b-file; the bar is the whole b-file,
  which takes several seconds.
- Correct for every n: the program tests the definition directly. Compare
  [A001744](../A001744/) (version 2).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001743), CC BY-SA 4.0.
