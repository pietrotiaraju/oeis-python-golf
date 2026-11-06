# A000455

> Digits of powers of 2.
> — [OEIS A000455](https://oeis.org/A000455)

Offset 0: 1, 2, 4, 8, 1, 6, 3, 2, 6, 4, …

### Python 3 — 39 bytes

```python
n=1
while[print(d)for d in str(n)]:n*=2
```

**How it works**

The integer n successively takes the values 2⁰, 2¹, 2², ….
The comprehension prints each decimal digit on its own line.
Its resulting list is nonempty, so the loop continues.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.
- Python 3.11+ eventually reaches its default 4300-digit integer-to-string limit; that interpreter limit is not counted as a correctness failure.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000455), CC BY-SA 4.0.
