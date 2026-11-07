# A000534

> Numbers that are not the sum of 4 nonzero squares.
> — [OEIS A000534](https://oeis.org/A000534)

Offset 1: 0, 1, 2, 3, 5, 6, 8, 9, 11, 14, …

### Python 3 — 62 bytes

```python
a=[*b'\0	 )8`\x80']
for x in a:print(x);a+=4*a[-3],
```

The bytes literal holds twelve raw control bytes (1, 2, 3, 5, 6, 8, 9, 11,
14, 17, 24 and 29; 9 is a tab) that a browser does not show. Byte for
byte, the first line is

```text
a=[*b'\0<01><02><03><05><06><08><09><0b><0e><11><18><1d> )8`\x80']
```

where `<01>` stands for the single byte 0x01, and so on. With those twelve
bytes escaped (`\1\2\3\5\6\b\t\v\16\21\30\35`) the program is 78 bytes.

**How it works**

- **The classification.** A positive integer is a sum of four positive
  squares unless it is 1, 3, 5, 9, 11, 17, 29, 41 or of the form 2·4^m,
  6·4^m or 14·4^m (m ≥ 0), and 0 is not such a sum (Grosswald 1985,
  Theorem 3; formula on the entry). Sorted, the exceptions stop at 41, and
  from 56 on the terms are 4^m·(14, 24, 32) for m = 1, 2, …: 56, 96, 128,
  224, 384, 512, … So every term from 224 on is 4 times the term three
  places before it.
- **The table.** `[*b'…']` unpacks a bytes object into the list of its byte
  values: the 18 terms 0, 1, …, 41, 56, 96, 128, that is, all terms up to
  the point where the rule takes over. 0 is written `\0` (a raw NUL byte is
  not allowed in source), 128 is `\x80` (a bytes literal holds only ASCII),
  and 32, 41, 56, 96 are the characters space, `)`, `8` and `` ` ``.
  Python accepts the other control bytes raw inside a literal (only NUL,
  the line breaks, the backslash and the quote are not allowed there).
- **The loop.** `for x in a:` walks a list that grows while it is read:
  each pass appends `4*a[-3]`. The last three entries are always three
  consecutive terms from 56 on, so the appended value is the next term,
  and the iterator never runs out.

**Notes**

- Other versions that print the same terms: the same list written in
  decimal, `a=[0,1,2,3,5,6,8,9,11,14,17,24,29,32,41,56,96,128]`: 82 bytes;
  printing the 15 small terms with `print(…,sep='\n')` and then running a
  three-entry queue `a=a[1:]+[4*a[0]]`: 102 bytes.
- Correctness for every n rests on the classification theorem above; a
  brute-force list of the numbers up to 20000 that are not sums of four
  positive squares agrees with the program.
- The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s, and it prints at once.
- The terms grow by a factor 4 every three places, so a(21434) is the first
  with more than 4300 digits (Python's int-to-str limit): printing stops
  there, about 6 s in here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 102 | first entry |
| 2026-11-07 | Python 3 | 62 | byte table read as a growing list, 4·a(n−3) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000534), CC BY-SA 4.0.
