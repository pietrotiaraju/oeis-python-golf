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

- n runs through 10⁰, 10¹, 10², …, and `'%o'%n` formats it in octal with
  no `0o` prefix.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `f'{n:o}'` is 2 bytes longer
  and `oct(n)[2:]` 4 bytes longer than `'%o'%n`.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 101 terms print in 0.07 s here. The b-file has 101 terms
  (up to a(100)); the bar is the whole b-file in 60 s.
- The output is made by `%o` formatting, which is not limited to 4300
  digits (only decimal int-to-str conversion is), so printing never stops.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000468), CC BY-SA 4.0.
