# A001731

> a(n) is 9 written in base 10-n.
> — [OEIS A001731](https://oeis.org/A001731)

Offset 0, finite (all 10 terms): 9, 10, 11, 12, 13, 14, 21, 100, 1001, 111111111.

### Python 3 — 46 bytes

```python
print(*range(9,15),21,100,1001,'1'*9,sep='\n')
```

**How it works**

- **The terms.** a(n) is 9 written in base 10 − n for n = 0, …, 9, read as a
  decimal number; base 1 is unary, as in the OEIS data:
  - n = 0, base 10: 9 is a single digit, 9;
  - n = 1, base 9: 9 = 1·9 + 0, so 10;
  - n = 2, base 8: 9 = 1·8 + 1, so 11;
  - n = 3, base 7: 9 = 1·7 + 2, so 12;
  - n = 4, base 6: 9 = 1·6 + 3, so 13;
  - n = 5, base 5: 9 = 1·5 + 4, so 14;
  - n = 6, base 4: 9 = 2·4 + 1, so 21;
  - n = 7, base 3: 9 = 1·3^2 + 0·3 + 0, so 100;
  - n = 8, base 2: 9 = 1·2^3 + 0·2^2 + 0·2 + 1, so 1001;
  - n = 9, base 1 (unary, the only digit is 1): 9 ones, 111111111.
- **Storing them.** `print(*…,sep='\n')` prints its arguments one per line.
  9 to 14 are a run, `*range(9,15)`; then come 21, 100, 1001, and the unary
  111111111 as the string `'1'*9`. The ten terms in a triple-quoted string,
  with `'1'*9` appended, are 48 bytes.
- There is nothing more to compute: the sequence has exactly these ten terms
  (keywords fini, full), and the program stops after the last one.

**Notes**

- A program that converts 9 into each base (the recursive lambda of
  [A001357](../A001357/) with the base as a second argument, looped over b =
  10, …, 2, then the unary term) is 86 bytes, about twice as long.
- The program spells out the terms, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001731), CC BY-SA 4.0.
