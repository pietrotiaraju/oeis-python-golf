# A001387

> Binary "look and say" sequence.
> — [OEIS A001387](https://oeis.org/A001387)

Offset 1: 1, 11, 101, 111011, 11110101, 100110111011, 111001011011110101, 111100111010110100110111011, 100110011110111010110111001011011110101, …

### Python 3 — 84 bytes

```python
import re
s='1'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:f'{len(m[0]):b}'+m[1],s)
```

**How it works**

- Binary look-and-say: the decimal program of [A005150](../../A005xxx/A005150/) with each run length written in base 2. From a(1) = 1: one 1 gives `1`·`1` = 11, two 1s give `10`·`1` = 101, and so on.
- `(.)\1*` matches each maximal run of one digit: the group grabs the digit
  and the backreference eats every copy after it, so the run ends where the
  digit changes. `re.sub` hands each match to the lambda, which writes the
  run length in binary followed by the digit (`m[0]` is the run, `m[1]` the
  digit).
- `f'{len(m[0]):b}'` formats the run length in binary whatever its size,
  so nothing rests on the fact (proved on the OEIS page of A001387) that
  `000` and `11111` never occur.
- `while[print(s)]:` prints in the loop test (the list `[None]` is true).

**Notes**

- Exact for every n: only string operations, and the term stays a string, so
  the 4300-digit limit of `int`-to-`str` conversion never applies.
- The b-file has the first 17 terms and the bar is all of them in 60 s
  (well under a second here). Terms grow by a factor near 1.46 per step, so memory is the limit after that.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001387), CC BY-SA 4.0.
