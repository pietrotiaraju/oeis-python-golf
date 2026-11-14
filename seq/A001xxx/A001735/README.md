# A001735

> 5 in base 10-n.
> — [OEIS A001735](https://oeis.org/A001735)

Offset 0, finite (all 10 terms): 5, 5, 5, 5, 5, 10, 11, 12, 101, 11111.

### Python 3 — 37 bytes

```python
for c in'\ne⭧':print(ord(c))
```

The string holds 7 raw control characters that a browser does not
show, and one character outside ASCII. Byte for byte, the program is

```text
for c in'<05><05><05><05><05>\n<0B><0C>e<U+2B67>':print(ord(c))
```

where `<05>` stands for the single byte 0x05 (and so on), and
`<U+2B67>` for that one character, 3 bytes in UTF-8. With every one of
them escaped the program is plain ASCII and 57 bytes:

```python
for c in'\x05\x05\x05\x05\x05\n\v\fe\u2b67':print(ord(c))
```

**How it works**

- **The terms.** a(n) is 5 written in base 10 − n for n = 0, …, 9, read as a
  decimal number; base 1 is unary, as in the OEIS data:
  - n = 0, base 10: 5 is a single digit, 5;
  - n = 1, base 9: 5 is a single digit, 5;
  - n = 2, base 8: 5 is a single digit, 5;
  - n = 3, base 7: 5 is a single digit, 5;
  - n = 4, base 6: 5 is a single digit, 5;
  - n = 5, base 5: 5 = 1·5 + 0, so 10;
  - n = 6, base 4: 5 = 1·4 + 1, so 11;
  - n = 7, base 3: 5 = 1·3 + 2, so 12;
  - n = 8, base 2: 5 = 1·2^2 + 0·2 + 1, so 101;
  - n = 9, base 1 (unary, the only digit is 1): 5 ones, 11111.
- **Storing them.** Each term is one character of the string, the one whose
  code point is the term, and `ord(c)` gives it back. All ten terms are
  below 1114111 = 0x10FFFF, the largest code point; the unary 11111 is
  U+2B67, 3 bytes in UTF-8. The small terms are control characters, written
  raw (one byte each), except 10 and 13, the line breaks, which a string
  literal needs as `\n` and `\r`; 101 is the letter `e`.
- `for c in'…':print(ord(c))` is 4 bytes under
  `print(*map(ord,'…'),sep='\n')`.
- Writing the terms in decimal instead,
  `print('5\n'*5+'10\n11\n12\n101\n11111')` is 39 bytes.
- There is nothing more to compute: the sequence has exactly these ten terms
  (keywords fini, full), and the program stops after the last one.

**Notes**

- A program that converts 5 into each base (the recursive lambda of
  [A001357](../A001357/) with the base as a second argument, looped over b =
  10, …, 2, then the unary term) is 86 bytes, about twice as long.
- The program spells out the terms, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001735), CC BY-SA 4.0.
