# A001388

> Describe the previous term (in base 3)!.
> — [OEIS A001388](https://oeis.org/A001388)

Offset 1: 1, 11, 21, 1211, 111221, 1012211, 1110112221, 101102110211, 111021101221101221, …

### Python 3 — 94 bytes

```python
import re
s='1'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str((k:=len(m[0]))+k//3*7)+m[1],s)
```

**How it works**

- Look-and-say in base 3: the decimal program of [A005150](../../A005xxx/A005150/) with each run length written in base 3. From 111221: three 1s give `10`·`1`, two 2s `2`·`2`, one 1 `1`·`1`, so the next term is 1012211.
- `(.)\1*` matches each maximal run of one digit: the group grabs the digit
  and the backreference eats every copy after it, so the run ends where the
  digit changes. `re.sub` hands each match to the lambda, which writes the
  run length in base 3 followed by the digit (`m[0]` is the run, `m[1]` the
  digit).
- **Base 3 without a converter.** For a run length k ≤ 8, write
  k = 3q + r with q, r ≤ 2; its base-3 numeral is the two digits q, r, which
  read in decimal is 10q + r = k + 7q = `k+k//3*7` (for k < 3 this is just
  k). `str` turns it into the digits. The walrus keeps k for the second use.
- **Why k ≤ 8 is enough: runs never pass 5.** Suppose every run in a term
  is at most 5 long (true for the one-digit seed). Then each run length has
  at most two base-3 digits, so the next term is a chain of tokens
  (count, digit) of 2 or 3 characters, and neighbouring tokens end in
  different digits (adjacent runs differ). A run of a digit x in the next
  term can contain at most one whole token: two neighbours would both end
  in x. If it contains one, it cannot reach into the token before (that one
  ends in a digit other than x) and takes at most the first 2 characters of
  the token after (its last digit is not x): at most 3 + 2 = 5. If it
  contains none, it lies in the end of one token and a proper beginning of
  the next: at most 3 + 2 = 5 again. By induction every run in every term
  is at most 5 (the longest run in the first 40 terms is 3), so `k+k//3*7` is the
  right base-3 numeral for every count the program meets.
- `while[print(s)]:` prints in the loop test (the list `[None]` is true).

**Notes**

- Exact for every n: only string operations, and the term stays a string, so
  the 4300-digit limit of `int`-to-`str` conversion never applies.
- The b-file has the first 23 terms and the bar is all of them in 60 s
  (well under a second here). Terms grow by a factor near 1.32 per step, so memory is the limit after that.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001388), CC BY-SA 4.0.
