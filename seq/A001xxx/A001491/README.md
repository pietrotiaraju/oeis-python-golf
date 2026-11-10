# A001491

> Opus numbers of Beethoven's nine symphonies.
> — [OEIS A001491](https://oeis.org/A001491)

Offset 1, finite (all 9 terms): 21, 36, 55, 60, 67, 68, 92, 93, 125.

### Python 3 — 29 bytes

```python
print(*b'$7<CD\]}',sep='\n')
```

The bytes literal holds one raw control byte (21) that a browser does not
show. Byte for byte, the program is

```text
print(*b'<15>$7<CD\]}',sep='\n')
```

where `<15>` stands for the single byte 0x15. Escaped as `\25`, it makes the
program 31 bytes.

**How it works**

- The sequence is the list of opus numbers of Beethoven's nine symphonies,
  in the order of the symphonies: No. 1 in C, Op. 21; No. 2, Op. 36; No. 3
  (Eroica), Op. 55; No. 4, Op. 60; No. 5, Op. 67; No. 6 (Pastoral), Op. 68;
  No. 7, Op. 92; No. 8, Op. 93; No. 9 (Choral), Op. 125. There is nothing to
  compute: the program stores the nine numbers as compactly as it can and
  stops after the last one.
- Every opus number is below 128, so each one is a single ASCII byte, and a
  bytes literal holds them one byte each: 36, 55, 60, … are the characters
  `$`, `7`, `<`, …, and `print(*b'…',sep='\n')` unpacks the byte values as
  ints and prints one per line.
- 21 is a control character, which Python accepts raw inside a literal
  (only NUL, the line breaks 10 and 13, the quote and the backslash need
  care there).
- 92 is the backslash. `\]` is not a known escape, and Python keeps the
  backslash of an unknown escape in the value, so `\]` stands for the two
  bytes 92, 93 at one source byte each; CPython 3.12 only prints a
  `SyntaxWarning` about it on stderr, which the rules ignore. The proper
  escape `\\]` would cost one byte more.

**Notes**

- `for c in b'…':print(c)` is 1 byte longer than the `sep` form, as in
  [A001049](../A001049/).
- Finite sequence (keywords fini, full): the bar is all 9 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001491), CC BY-SA 4.0.
