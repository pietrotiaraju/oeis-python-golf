# A001151

> Describe the previous term! (method A - initial term is 8).
> — [OEIS A001151](https://oeis.org/A001151)

Offset 1: 8, 18, 1118, 3118, 132118, 1113122118, 311311222118, …

### Python 3 — 82 bytes

```python
import re
s='8'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],s)
```

**How it works**

- The same program as the look-and-say sequence from 1,
  [A005150](../../A005xxx/A005150/), with the seed `'8'` instead of `'1'`.
- `(.)\1*` matches each maximal run of one digit: the group grabs the digit
  and the backreference eats every copy after it, so the run ends where the
  digit changes. `re.sub` hands each match to the lambda, which writes the
  run length followed by the digit (`m[0]` is the run, `m[1]` the digit).
- `str(len(…))` takes any run length, so nothing rests on Conway's theorem
  that runs never pass 3 here. The seed 8 stays a run of length 1 at the end
  of every term, so from a(2) on every term ends in 18.
- `while[print(s)]:` prints in the loop test (the list `[None]` is true).

**Notes**

- Exact for every n: only string operations, and the term stays a string, so
  the 4300-digit limit of `int`-to-`str` conversion never applies.
- The b-file has the first 20 terms and the bar is all of them in 60 s (well
  under a second here). Terms grow by Conway's constant λ ≈ 1.3036 per step,
  so memory is the limit after that.
- As in A005150, `itertools.groupby` and an import-free `lstrip` peel are
  longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001151), CC BY-SA 4.0.
