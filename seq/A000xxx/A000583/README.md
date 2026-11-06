# A000583

> Fourth powers: a(n) = n^4.
> — [OEIS A000583](https://oeis.org/A000583)

Offset 0: 0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**4)]:n+=1
```

**How it works**

- Raise each nonnegative integer n to the defining power 4.
  The initial value at n=0 is included.
- `print` returns `None`, but the containing list is nonempty, so the
  loop continues after every output and advances n by one.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000583), CC BY-SA 4.0.
