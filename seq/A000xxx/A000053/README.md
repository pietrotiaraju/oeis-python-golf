# A000053

> Local stops on New York City 1 Train (Broadway-7 Avenue Local) subway.
> — [OEIS A000053](https://oeis.org/A000053)

Offset 1, finite (all 29 terms): 14, 18, 23, 28, 34, 42, 50, 59, 66, 72, 79, 86, 96, 103, 110, 116, 125, 137, 145, 157, 168, 181, 191, 207, 215, 225, 231, 238, 242.

### Python 3 — 62 bytes

```python
s=0
for c in b".$%%&(()'&''*''&),(,+-*0(*&'$":s+=c-32;print(s)
```

**How it works**

- The sequence is a list of numbered street stops of the 1 train (as of
  February 2000), so there is nothing to compute: the program just stores
  the 29 numbers as compactly as it can and stops after the last one.
- It stores the gaps between consecutive stops instead of the stops: the
  gaps run from 4 to 16 (the first "gap" is the first stop, from 0).
  Each gap plus 32 is a printable ASCII byte, so all of them fit one byte
  each in a bytes literal; looping over `b"…"` yields the byte values as
  ints, `s+=c-32` adds the gap back and `print(s)` shows the running total.
- The literal holds a `'` (gap 7) but no `"` or `\`, so it is written
  with double quotes and needs no escapes.

**Notes**

- The stops themselves go up to 242, and 12 of them are above 127: a
  bytes literal only takes ASCII, and in a str literal each of those costs
  2 bytes of UTF-8. `for c in'…':print(ord(c))` comes to 65 bytes.
- The raw gaps (with no `-32`) would save 3 bytes of code, but some gaps
  are 10 or 13 (newline and carriage return), which need a 2-byte escape
  in the literal (four of them), one byte more in all. `s-=~c` (adds c + 1) is
  one byte under `s+=c-32` but still needs an escape and only ties.
- Finite sequence (keywords fini, full): the bar is all 29 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000053), CC BY-SA 4.0.
