# A001733

> 7 in base 10-n.
> — [OEIS A001733](https://oeis.org/A001733)

Offset 0, finite (all 10 terms): 7, 7, 7, 10, 11, 12, 13, 21, 111, 1111111.

### Python 3 — 39 bytes

```python
for c in'\n\ro􏑇':print(ord(c))
```

The string holds 6 raw control characters that a browser does not
show, and one character outside ASCII. Byte for byte, the program is

```text
for c in'<07><07><07>\n<0B><0C>\r<15>o<U+10F447>':print(ord(c))
```

where `<07>` stands for the single byte 0x07 (and so on), and
`<U+10F447>` for that one character, 4 bytes in UTF-8. With every one of
them escaped the program is plain ASCII and 53 bytes:

```python
for c in'\a\a\a\n\v\f\r\x15o\U0010f447':print(ord(c))
```

**How it works**

- **The terms.** a(n) is 7 written in base 10 − n for n = 0, …, 9, read as a
  decimal number; base 1 is unary, as in the OEIS data:
  - n = 0, base 10: 7 is a single digit, 7;
  - n = 1, base 9: 7 is a single digit, 7;
  - n = 2, base 8: 7 is a single digit, 7;
  - n = 3, base 7: 7 = 1·7 + 0, so 10;
  - n = 4, base 6: 7 = 1·6 + 1, so 11;
  - n = 5, base 5: 7 = 1·5 + 2, so 12;
  - n = 6, base 4: 7 = 1·4 + 3, so 13;
  - n = 7, base 3: 7 = 2·3 + 1, so 21;
  - n = 8, base 2: 7 = 1·2^2 + 1·2 + 1, so 111;
  - n = 9, base 1 (unary, the only digit is 1): 7 ones, 1111111.
- **Storing them.** Each term is one character of the string, the one whose
  code point is the term, and `ord(c)` gives it back. All ten terms are
  below 1114111 = 0x10FFFF, the largest code point; the unary 1111111 is
  U+10F447, 4 bytes in UTF-8. The small terms are control characters,
  written raw (one byte each), except 10 and 13, the line breaks, which a
  string literal needs as `\n` and `\r`; 111 is the letter `o`.
- `for c in'…':print(ord(c))` is 4 bytes under
  `print(*map(ord,'…'),sep='\n')`.
- Writing the terms in decimal instead, a triple-quoted string of the
  decimal terms with `'1'*7` appended is 44 bytes.
- There is nothing more to compute: the sequence has exactly these ten terms
  (keywords fini, full), and the program stops after the last one.

**Notes**

- A program that converts 7 into each base (the recursive lambda of
  [A001357](../A001357/) with the base as a second argument, looped over b =
  10, …, 2, then the unary term) is 86 bytes, about twice as long.
- The program spells out the terms, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001733), CC BY-SA 4.0.
