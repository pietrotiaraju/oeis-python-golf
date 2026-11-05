# A000012

> The simplest sequence of positive numbers: the all 1's sequence.
> — [OEIS A000012](https://oeis.org/A000012)

Offset 0: 1, 1, 1, 1, 1, …

### Python 3 — 16 bytes

```python
while 1:print(1)
```

**How it works**

Prints 1 forever, the same loop as [A000004](../A000004/).

**Notes**

- `while[print(1)]:0` puts the print in the condition, but the body cannot be
  empty, so it is one byte longer (17).
- `for _ in iter(int,1):print(1)` is 29 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 16 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000012), CC BY-SA 4.0.
