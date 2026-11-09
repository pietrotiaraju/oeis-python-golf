# A001391

> To get the 3rd term, for example, note that 2nd term has three (11 in binary!) 1's and one (1) 0, giving 11 1 1 0.
> — [OEIS A001391](https://oeis.org/A001391)

Offset 1: 10, 1110, 11110, 100110, 1110010110, 111100111010110, 100110011110111010110, 1110010110010011011110111010110, …

### Python 3 — 85 bytes

```python
import re
s='10'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:f'{len(m[0]):b}'+m[1],s)
```

**How it works**

- The binary look-and-say program of [A001387](../A001387/) with the seed `'10'`: from 10, one 1 and one 0 give `1`·`1`·`1`·`0` = 1110, then three (`11`) 1s and one 0 give 11110, as in the OEIS name.
- `(.)\1*` matches each maximal run of one digit: the group grabs the digit
  and the backreference eats every copy after it, so the run ends where the
  digit changes. `re.sub` hands each match to the lambda, which writes the
  run length in binary followed by the digit (`m[0]` is the run, `m[1]` the
  digit).
- `f'{len(m[0]):b}'` formats the run length in binary whatever its size,
  so no bound on the run lengths is needed.
- `while[print(s)]:` prints in the loop test (the list `[None]` is true).

**Notes**

- Exact for every n: only string operations, and the term stays a string, so
  the 4300-digit limit of `int`-to-`str` conversion never applies.
- The b-file has the first 17 terms and the bar is all of them in 60 s
  (well under a second here). Terms grow by a factor near 1.46 per step, so memory is the limit after that.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001391), CC BY-SA 4.0.
