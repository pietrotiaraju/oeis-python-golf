# A002015

> a(n) = n^2 reduced mod 100.
> — [OEIS A002015](https://oeis.org/A002015)

Offset 0: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 21, 44, 69, 96, 25, 56, 89, …

### Python 3 — 30 bytes

```python
n=0
while[print(n*n%100)]:n+=1
```

**How it works**

- `n*n%100` is the last two digits of n², printed for n = 0, 1, 2, ….

**Notes**

- The sequence has period 50, since (n + 50)² = n² + 100n + 2500.
- The b-file has the 60 terms of the OEIS data (n = 0 to 59); the bar is
  the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002015), CC BY-SA 4.0.
