# A000799

> a(n) = floor(2^n / n).
> — [OEIS A000799](https://oeis.org/A000799)

Offset 1: 2, 2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 341, 630, 1170, 2184, 4096, 7710, 14563, 27594, 52428, …

### Python 3 — 31 bytes

```python
n=0
while n:=n+1:print(2**n//n)
```

**How it works**

- The definition, term by term: `2**n//n` is ⌊2ⁿ/n⌋ in exact integer
  arithmetic (Python's `//` floors, and both operands are positive).
- `while n:=n+1:` starts the count at 1 from `n=0` and never stops, since
  n is never 0 again; it is two bytes shorter than
  `n=1` … `while 1:print(2**n//n);n+=1`.

**Notes**

- No theorem needed; integers are exact at any size.
- Python 3.11+ refuses to print integers of more than 4300 digits, so the
  program stops near n = 14300 (an interpreter limit).
- The b-file has 300 terms, all printed in well under a second; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000799), CC BY-SA 4.0.
