# A001145

> Describe the previous term! (method A - initial term is 7).
> — [OEIS A001145](https://oeis.org/A001145)

Offset 1: 7, 17, 1117, 3117, 132117, 1113122117, 311311222117, 13211321322117, …

### Python 3 — 82 bytes

```python
import re
s='7'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],s)
```

**How it works**

- The same program as the look-and-say sequence from 1,
  [A005150](../../A005xxx/A005150/), with the seed `'7'` instead of `'1'`.
- `(.)\1*` matches each maximal run of one digit: the group grabs the digit
  and the backreference eats every copy after it, so the run ends where the
  digit changes. `re.sub` hands each match to the lambda, which writes the
  run length followed by the digit (`m[0]` is the run, `m[1]` the digit).
- `str(len(…))` takes any run length, so nothing rests on Conway's theorem
  that runs never pass 3 here. In the terms the 7 stays alone at the end
  (everything before it only ever holds the digits 1–3), so from a(2) on
  every term ends in 17.
- `while[print(s)]:` prints in the loop test (the list `[None]` is true).

**The family**

Seeds 0–9 of method A: 0 [A001155](https://oeis.org/A001155),
1 [A005150](../../A005xxx/A005150/), 2 [A006751](https://oeis.org/A006751),
3 [A006715](https://oeis.org/A006715), 4 [A001140](../A001140/),
5 [A001141](../A001141/), 6 [A001143](../A001143/), 7 A001145 (this page),
8 [A001151](https://oeis.org/A001151), 9 [A001154](https://oeis.org/A001154).
From 4 up the terms differ only in the last digit: the seed is the only
digit above 3, a lone run at the end of every term.

**Notes**

- Exact for every n: only string operations, and the term stays a string, so
  the 4300-digit limit of `int`-to-`str` conversion never applies.
- The b-file has the first 20 terms and the bar is all of them in 60 s.
  Terms grow by Conway's constant λ ≈ 1.3036 per step, so memory, not time,
  is the limit after a few dozen more.
- As in A005150, `itertools.groupby` (94 bytes) and an import-free
  `lstrip` peel (90 bytes) are longer; `'%d'%len(m[0])` ties with
  `str(len(m[0]))` and an f-string is a byte longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001145), CC BY-SA 4.0.
