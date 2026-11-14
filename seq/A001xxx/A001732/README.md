# A001732

> 8 in base 10-n.
> — [OEIS A001732](https://oeis.org/A001732)

Offset 0, finite (all 10 terms): 8, 8, 10, 11, 12, 13, 20, 22, 1000, 11111111.

### Python 3 — 46 bytes

```python
print("""8
8
10
11
12
13
20
22
1000
"""+'1'*8)
```

**How it works**

- **The terms.** a(n) is 8 written in base 10 − n for n = 0, …, 9, read as a
  decimal number; base 1 is unary, as in the OEIS data:
  - n = 0, base 10: 8 is a single digit, 8;
  - n = 1, base 9: 8 is a single digit, 8;
  - n = 2, base 8: 8 = 1·8 + 0, so 10;
  - n = 3, base 7: 8 = 1·7 + 1, so 11;
  - n = 4, base 6: 8 = 1·6 + 2, so 12;
  - n = 5, base 5: 8 = 1·5 + 3, so 13;
  - n = 6, base 4: 8 = 2·4 + 0, so 20;
  - n = 7, base 3: 8 = 2·3 + 2, so 22;
  - n = 8, base 2: 8 = 1·2^3 + 0·2^2 + 0·2 + 0, so 1000;
  - n = 9, base 1 (unary, the only digit is 1): 8 ones, 11111111.
- **Storing them.** The first nine terms sit in a triple-quoted string, one
  per line with real line breaks (one byte each, where `\n` costs two), and
  the unary term is appended as `'1'*8`, 2 bytes shorter than writing it
  out; `print` adds the final line break. Storing the terms as code points,
  as in [A001733](../A001733/), does not work here: the unary term 11111111
  is above 1114111 = 0x10FFFF, the largest code point.
- There is nothing more to compute: the sequence has exactly these ten terms
  (keywords fini, full), and the program stops after the last one.

**Notes**

- A program that converts 8 into each base (the recursive lambda of
  [A001357](../A001357/) with the base as a second argument, looped over b =
  10, …, 2, then the unary term) is 86 bytes, about twice as long.
- The program spells out the terms, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001732), CC BY-SA 4.0.
