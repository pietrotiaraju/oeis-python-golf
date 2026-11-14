# A001736

> 4 in base 10-n.
> — [OEIS A001736](https://oeis.org/A001736)

Offset 0, finite (all 10 terms): 4, 4, 4, 4, 4, 4, 10, 11, 100, 1111.

### Python 3 — 34 bytes

```python
print('4\n'*6+'10\n11\n100\n1111')
```

**How it works**

- **The terms.** a(n) is 4 written in base 10 − n for n = 0, …, 9, read as a
  decimal number; base 1 is unary, as in the OEIS data:
  - n = 0, base 10: 4 is a single digit, 4;
  - n = 1, base 9: 4 is a single digit, 4;
  - n = 2, base 8: 4 is a single digit, 4;
  - n = 3, base 7: 4 is a single digit, 4;
  - n = 4, base 6: 4 is a single digit, 4;
  - n = 5, base 5: 4 is a single digit, 4;
  - n = 6, base 4: 4 = 1·4 + 0, so 10;
  - n = 7, base 3: 4 = 1·3 + 1, so 11;
  - n = 8, base 2: 4 = 1·2^2 + 0·2 + 0, so 100;
  - n = 9, base 1 (unary, the only digit is 1): 4 ones, 1111.
- **Storing them.** The six leading 4s are `'4\n'*6`; the rest is a string
  with `\n` escapes. With three line breaks left, that is one byte shorter
  than a triple-quoted string with real line breaks (four more quote
  characters, one byte less per break). One character per term, read back
  with `for c in'…':print(ord(c))` as in [A001733](../A001733/), is 36
  bytes.
- There is nothing more to compute: the sequence has exactly these ten terms
  (keywords fini, full), and the program stops after the last one.

**Notes**

- A program that converts 4 into each base (the recursive lambda of
  [A001357](../A001357/) with the base as a second argument, looped over b =
  10, …, 2, then the unary term) is 86 bytes, about twice as long.
- The program spells out the terms, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001736), CC BY-SA 4.0.
