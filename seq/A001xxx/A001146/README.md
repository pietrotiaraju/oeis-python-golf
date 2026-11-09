# A001146

> a(n) = 2^(2^n).
> — [OEIS A001146](https://oeis.org/A001146)

Offset 0: 2, 4, 16, 256, 65536, 4294967296, 18446744073709551616, …

### Python 3 — 24 bytes

```python
x=2
while[print(x)]:x*=x
```

**How it works**

- 2^(2^(n+1)) = (2^(2^n))², so each term is the square of the one before:
  `x*=x` doubles the exponent. The same idea as the Fermat numbers
  [A000215](../../A000xxx/A000215/), which print `b+1` from this loop.
- `while[print(x)]:` prints in the loop test (`[None]` is a true list), a
  byte under `while 1:print(x);`.
- Doubling the exponent instead (`n=1` / `while[print(2**n)]:n*=2`) is
  3 bytes longer.

**Notes**

- Integers only, so every term is exact.
- a(n) has about 0.301·2ⁿ digits: a(14) has 4933, past Python's 4300-digit
  limit for converting an int to a string, so the program prints
  a(0)…a(13) and stops with a `ValueError`. That is an interpreter limit,
  not a wrong term; lifting it with `sys.set_int_max_str_digits(0)` would
  cost 41 bytes and only buys terms the b-file doesn't have. The b-file
  has 12 terms (up to a(11), 617 digits) and the bar is all of them in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001146), CC BY-SA 4.0.
