# A001292

> Concatenations of cyclic permutations of initial positive integers.
> — [OEIS A001292](https://oeis.org/A001292)

Offset 1: 1, 12, 21, 123, 231, 312, 1234, 2341, 3412, 4123, 12345, …

For each n the n cyclic shifts of (1, 2, …, n) are written as one number
each, and these are listed in increasing order. The order only matters
from n = 10 on: as the OEIS comment notes, a(46) = 10123456789, not
12345678910.

### Python 3 — 86 bytes

```python
l=[]
while 1:l+=str(len(l)+1),;[*map(print,sorted(''.join(l:=l[1:]+l[:1])for x in l))]
```

**How it works**

- `l` holds the decimal strings `'1'`, …, `'n'`; each pass appends the
  next one, `str(len(l)+1)`.
- In the generator, the iterable `l` is evaluated once, when the generator
  is made, so it runs n times. Each step rotates `l` by one place (the
  walrus rebinds the module-level `l`) and joins it: the n rotations give
  every cyclic shift once and leave `l` as it was for the next pass.
- All shifts of one row use the same numbers, so their strings have the
  same length and `sorted` puts them in numerical order. Row n + 1 has
  more digits than row n, so the rows come out in increasing order too:
  the whole output is the sorted sequence.
- The terms are printed as the joined strings, never converted to `int`,
  so Python's 4300-digit int-to-str limit does not apply.

**Notes**

- Without sorting, `print(*range(i,n+1),*range(1,i),sep='')` in a
  single loop is 67 bytes, but it is wrong from a(46) on.
- Slicing by index, `''.join(l[i:]+l[:i])for i in range(len(l))`, is 9
  bytes longer than rotating `l` in place; a separate counter `n` for
  `str(n)` costs 2 bytes more than `len(l)+1`.
- The b-file has 10000 terms (rows 1 to 140 and the first 130 entries of
  row 141); the bar is the whole b-file in 60 s, which takes about 0.2 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001292), CC BY-SA 4.0.
