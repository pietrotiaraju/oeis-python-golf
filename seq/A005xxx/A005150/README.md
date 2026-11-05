# A005150

> Look and Say sequence: describe the previous term! (method A - initial term is 1).
> — [OEIS A005150](https://oeis.org/A005150)

Offset 1: 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, …

### Python 3 — 82 bytes

```python
import re
s='1'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],s)
```

**How it works**

- The term is kept as a string, so it never meets the 4300-digit limit of
  `int`-to-`str` conversion (a(30) already has 4462 digits).
- `(.)\1*` matches each maximal run of one digit: the group grabs the digit and
  the backreference eats every copy after it, greedily, so the run ends where
  the digit changes. `re.sub` hands each match to the lambda, which writes the
  run length followed by the digit: `m[0]` is the run, `m[1]` the digit.
- `str(len(…))` takes any run length, so the program does not lean on
  Conway's theorem that runs here never pass 3; it would work as well from any
  starting string.
- `while[print(s)]:` prints in the loop test (the list `[None]` is true), one
  byte under `while 1:print(s);`.

**Notes**

- Exact for every n: only string operations. The b-file has the first 25 terms
  and the bar is all of them in 60 s; the program prints 62 terms in 60 s on
  the PC it was written on (a(62) has 21.5 million digits). Terms grow by
  Conway's constant λ ≈ 1.3036 per step, so memory, not time, is the limit
  after that.
- Shortest alternatives found: `itertools.groupby` with
  `''.join(str(len([*g]))+k for k,g in groupby(s))` is 94 bytes, and the
  import-free loop that peels runs with `s.lstrip(s[0])` is 90.
  `f'{len(m[0])}'+m[1]` and `'%d'%len(m[0])+m[1]` tie with the lambda body.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A005150), CC BY-SA 4.0.
