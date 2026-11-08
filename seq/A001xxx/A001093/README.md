# A001093

> a(n) = n^3 + 1.
> — [OEIS A001093](https://oeis.org/A001093)

Offset -1: 0, 1, 2, 9, 28, 65, 126, 217, 344, 513, …

### Python 3 — 30 bytes

```python
n=-1
while[print(n**3+1)]:n+=1
```

**How it works**

- The counter n starts at the offset, −1, and the program prints the
  definition `n**3+1`; the first term is (−1)³ + 1 = 0.
- `while[print(…)]:` prints in the loop condition: `print` returns `None` and
  the one-element list `[None]` is true. This is
  [A000578](../../A000xxx/A000578/) (n³) plus one, started one step
  earlier.

**Notes**

- `-~n**3` is a tie for `n**3+1` (`**` binds tighter than `~`, so it is
  n³ + 1), and `n=~0` ties `n=-1`.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10002 terms (a(−1) to a(10000)); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001093), CC BY-SA 4.0.
