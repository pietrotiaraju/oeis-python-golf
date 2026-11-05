# A000215

> Fermat numbers: a(n) = 2^(2^n) + 1.
> — [OEIS A000215](https://oeis.org/A000215)

Offset 0: 3, 5, 17, 257, 65537, 4294967297, …

### Python 3 — 26 bytes

```python
b=2
while[print(b+1)]:b*=b
```

**How it works**

- Keep b = 2^(2^n) instead of the term itself: squaring doubles the
  exponent, so the update is just `b*=b`, and the term is b + 1.
- Tracking a(n) directly costs more: a(n) = (a(n−1) − 1)² + 1 needs
  something like `a=a*a-2*a+2`, which loses more than the `+1` in the print
  saves. Doubling an exponent (`n*=2` with `print(2**n+1)`) is 3 bytes
  longer.
- `while[print(…)]:` is a non-empty list, so it is always true, one byte
  under `while 1:` plus a `print(…);`.

**Notes**

- Integers only, so every term is exact.
- a(n) has about 0.301·2ⁿ digits, so a(14) (4933 digits) runs into
  Python's 4300-digit limit for converting an int to a string: the program
  prints a(0)…a(13) and stops with a `ValueError`. That is an interpreter
  limit, not a wrong term. The bar is the whole b-file (12 terms) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 26 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000215), CC BY-SA 4.0.
