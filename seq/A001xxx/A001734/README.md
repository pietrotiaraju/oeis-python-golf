# A001734

> 6 in base 10-n.
> — [OEIS A001734](https://oeis.org/A001734)

Offset 0, finite (all 10 terms): 6, 6, 6, 6, 10, 11, 12, 20, 110, 111111.

### Python 3 — 38 bytes

```python
for c in'\nn𛈇':print(ord(c))
```

The string holds 7 raw control characters that a browser does not
show, and one character outside ASCII. Byte for byte, the program is

```text
for c in'<06><06><06><06>\n<0B><0C><14>n<U+1B207>':print(ord(c))
```

where `<06>` stands for the single byte 0x06 (and so on), and
`<U+1B207>` for that one character, 4 bytes in UTF-8. With every one of
them escaped the program is plain ASCII and 61 bytes:

```python
for c in'\x06\x06\x06\x06\n\v\f\x14n\U0001b207':print(ord(c))
```

**How it works**

- **The terms.** a(n) is 6 written in base 10 − n for n = 0, …, 9, read as a
  decimal number; base 1 is unary, as in the OEIS data:
  - n = 0, base 10: 6 is a single digit, 6;
  - n = 1, base 9: 6 is a single digit, 6;
  - n = 2, base 8: 6 is a single digit, 6;
  - n = 3, base 7: 6 is a single digit, 6;
  - n = 4, base 6: 6 = 1·6 + 0, so 10;
  - n = 5, base 5: 6 = 1·5 + 1, so 11;
  - n = 6, base 4: 6 = 1·4 + 2, so 12;
  - n = 7, base 3: 6 = 2·3 + 0, so 20;
  - n = 8, base 2: 6 = 1·2^2 + 1·2 + 0, so 110;
  - n = 9, base 1 (unary, the only digit is 1): 6 ones, 111111.
- **Storing them.** Each term is one character of the string, the one whose
  code point is the term, and `ord(c)` gives it back. All ten terms are
  below 1114111 = 0x10FFFF, the largest code point; the unary 111111 is
  U+1B207, 4 bytes in UTF-8. The small terms are control characters, written
  raw (one byte each), except 10 and 13, the line breaks, which a string
  literal needs as `\n` and `\r`; 110 is the letter `n`.
- `for c in'…':print(ord(c))` is 4 bytes under
  `print(*map(ord,'…'),sep='\n')`.
- Writing the terms in decimal instead, the ten decimal terms in a
  triple-quoted string is 43 bytes.
- There is nothing more to compute: the sequence has exactly these ten terms
  (keywords fini, full), and the program stops after the last one.

**Notes**

- A program that converts 6 into each base (the recursive lambda of
  [A001357](../A001357/) with the base as a second argument, looped over b =
  10, …, 2, then the unary term) is 86 bytes, about twice as long.
- The program spells out the terms, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001734), CC BY-SA 4.0.
