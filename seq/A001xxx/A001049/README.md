# A001049

> Numbered stops in Manhattan on the Lexington Avenue subway.
> — [OEIS A001049](https://oeis.org/A001049)

Offset 1, finite (all 16 terms): 8, 14, 23, 28, 33, 42, 51, 59, 68, 77, 86, 96, 103, 110, 116, 125.

### Python 3 — 36 bytes

```python
print(*b'!*3;DMV`gnt}',sep='\n')
```

The bytes literal holds four raw control bytes (8, 14, 23 and 28) that a
browser does not show. Byte for byte, the program is

```text
print(*b'<08><0e><17><1c>!*3;DMV`gnt}',sep='\n')
```

where `<08>` stands for the single byte 0x08, and so on. With those four
bytes escaped (`\b\16\27\34`) the program is 43 bytes.

**How it works**

- The sequence is the list of numbered street stops of the 6 train, so
  there is nothing to compute: the program stores the 16 numbers as
  compactly as it can and stops after the last one.
- Every stop is below 128, so each one is a single ASCII byte, and a bytes
  literal holds them one byte each: 33, 42, 51, … are the characters `!`,
  `*`, `3`, …, and `print(*b'…',sep='\n')` unpacks the byte values as ints
  and prints one per line.
- The four smallest stops are control characters. Python accepts them raw
  inside a literal (only NUL, the line breaks 10 and 13, the backslash and
  the quote are not allowed there), so they cost one byte each like the
  rest. None of the 16 values is 10, 13, 39 (`'`) or 92 (`\`).

**Notes**

- Storing the gaps instead (8, 6, 9, 5, …, as in the 1-train pages
  [A000053](../../A000xxx/A000053/) and [A000054](../../A000xxx/A000054/))
  needs a running sum, `s=0` / `for c in b"…":s+=c-32;print(s)`, 49 bytes:
  here the stops themselves fit in ASCII, which the 1-train stops (up to
  242) do not.
- `for c in b'…':print(c)` is 1 byte longer than the `sep` form.
- Finite sequence (keywords fini, full): the bar is all 16 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001049), CC BY-SA 4.0.
