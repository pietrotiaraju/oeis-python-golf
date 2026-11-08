# A001098

> Multiply previous term by 2 and write in binary.
> — [OEIS A001098](https://oeis.org/A001098)

Offset 1: 1, 10, 10100, 100111011101000, 101101100001100111010010100000100111001010010000, …

### Python 3 — 36 bytes

```python
a=1
while[print(a)]:a=int(f'{a:b}0')
```

**How it works**

- Each term is read as a decimal number, doubled, and the double is written
  in binary; that string of 0s and 1s is the next term, again read in
  decimal: 1 → 2 = 10₂ → 20 = 10100₂ → 10100·2 = 20200 = 100111011101000₂.
- Doubling appends a 0 in binary, so the binary digits of 2a are those of
  a followed by `0`: `f'{a:b}0'`, 2 bytes under `bin(2*a)[2:]`. `int`
  reads that string back in base 10.

**Notes**

- Exact big-integer arithmetic. The terms grow fast: a(6) has 158 digits,
  a(7) 523, a(8) 1736. The next string has 5765 digits, and `int` refuses
  to read more than 4300 decimal digits (Python's int–str conversion limit
  since 3.11), so the program stops with a `ValueError` after a(8). That is
  an interpreter limit, not a wrong term.
- The b-file has 7 terms; the bar is all of them.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001098), CC BY-SA 4.0.
