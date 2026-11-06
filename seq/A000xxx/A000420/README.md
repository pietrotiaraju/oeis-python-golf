# A000420

> Powers of 7: a(n) = 7^n.
> — [OEIS A000420](https://oeis.org/A000420)

Offset 0: 1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=7
```

**How it works**

Start at 7⁰ = 1 and multiply by 7 after each print.
`print(n)` returns `None`, so `[print(n)]` is always the nonempty
list `[None]`, and the loop keeps going. This is the
[A000400](../A000400/) loop with multiplier 7.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 101 terms in 60 s; the official b-file contains 101 terms.
- Python 3.11+ eventually stops at its default 4300-digit integer-to-string limit; this interpreter limit is not counted as a correctness failure.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000420), CC BY-SA 4.0.
