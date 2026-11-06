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

The integer state visits 1, 10, 100, …, the powers of ten.
The `%o` format specifier writes each exact integer in octal
without a prefix, giving the decimal-digit representation required.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 101 terms in 60 s; the official b-file contains 101 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000468), CC BY-SA 4.0.
