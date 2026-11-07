# A000643

> a(n) = a(n-1) + 2^a(n-2).
> — [OEIS A000643](https://oeis.org/A000643)

Offset 0: 0, 0, 1, 2, 4, 8, 24, 280, 16777496, …

### Python 3 — 34 bytes

```python
a=b=0
while[print(a)]:a,b=b,b+2**a
```

**How it works**

- The pair (a, b) holds (a(n), a(n + 1)): print a(n), then shift to
  (a(n + 1), a(n + 1) + 2^a(n)), which is a(n + 2) by the recurrence.
- Starting from a = b = 0 gives a(0) = a(1) = 0; the recurrence then gives
  1, 2, 4, 8, 24, 280, 16777496, … .

**Notes**

- Exact integer arithmetic, but the terms explode. When a(9) (85 digits) is
  printed, b already holds a(10) = a(9) + 2^16777496, which Python builds in a
  fraction of a second; it has 5050530 digits, so it could never be printed
  anyway because of the 4300-digit int-to-str limit of Python 3.11+.
- After printing a(9) the program starts on 2^a(9) with a(9) ≈ 1.9·10⁸⁴, which
  no computer can hold: it only ends when memory runs out (an interpreter
  limit). Don't leave it running on its own.
- The b-file has the 10 terms a(0), …, a(9); the bar is all 10, printed in a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000643), CC BY-SA 4.0.
