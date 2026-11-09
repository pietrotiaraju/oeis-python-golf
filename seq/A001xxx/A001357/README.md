# A001357

> Powers of 2 written in base 9.
> — [OEIS A001357](https://oeis.org/A001357)

Offset 0: 1, 2, 4, 8, 17, 35, 71, 152, 314, 628, 1357, 2725, 5551, 12212, …

### Python 3 — 59 bytes

```python
f=lambda n:n and n%9+10*f(n//9)
n=1
while[print(f(n))]:n*=2
```

**How it works**

- `f(n)` writes n in base 9 and reads the digits back as a decimal number:
  the last base-9 digit is n mod 9, and the digits before it are those of
  ⌊n/9⌋, shifted one decimal place, so f(n) = (n mod 9) + 10·f(⌊n/9⌋),
  with f(0) = 0 ending the recursion (`n and …`).
- The loop doubles n = 2^k and prints f(n); `while[print(…)]:` is always
  true because the list is never empty.

**Notes**

- Exact integer arithmetic, correct for every n. The recursion goes one
  level per base-9 digit, about 0.315·k levels for 2^k, so Python's default
  recursion limit (1000) stops it near k = 3150 with a `RecursionError`, an
  interpreter limit; the b-file ends at k = 1000 (316 digits).
- The bar is the whole b-file (1001 terms, k = 0 to 1000) in 60 s, which
  takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001357), CC BY-SA 4.0.
