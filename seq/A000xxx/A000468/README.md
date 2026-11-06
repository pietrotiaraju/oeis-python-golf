# A000468

> Powers of ten written in base 8.
> — [OEIS A000468](https://oeis.org/A000468)

Offset 0: 1, 12, 144, 1750, 23420, 303240, 3641100, 46113200, 575360400, 7346545000, …

### Python 3 — 30 bytes

```python
n=1
while[print('%o'%n)]:n*=10
```

**How it works**

- n starts at 1=10⁰ and is multiplied by 10 after every output,
  so its exact integer values are the powers of ten.
- `'%o'%n` formats n in base 8 without an `0o` prefix. The
  resulting octal digits are printed as text; the sequence treats
  that digit string as its displayed integer representation.
- For example 10=1·8+2 prints 12, while
  100=1·8²+4·8+4 prints 144. Formatting handles carries
  across octal places automatically.
- `[print(...)]` is a nonempty list after the print returns
  `None`, so it supplies the always-true condition as well as output.

**Notes**

- The program changes the notation, not the integer arithmetic used
  to generate powers of ten. Parsing the formatted text back into
  an integer would add work without changing what must be printed.
- Octal conversion is exact and, as a power-of-two base, is exempt
  from Python 3.11+'s default 4300-digit decimal conversion limit.
  Memory and printing time still grow with the output length.
- The n-th output has ⌊n·log₈(10)⌋+1 octal digits. Only the
  current power and its formatted text are needed.
- The b-file has 101 terms (indices 0 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000468), CC BY-SA 4.0.
