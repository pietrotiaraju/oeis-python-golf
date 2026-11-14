# A001703

> Decimal concatenation of n, n+1, and n+2.
> — [OEIS A001703](https://oeis.org/A001703)

Offset 0: 12, 123, 234, 345, 456, 567, 678, 789, 8910, 91011, 101112, 111213, …

### Python 3 — 44 bytes

```python
n=0
while[print(int(f"{n}{n+1}{n+2}"))]:n+=1
```

**How it works**

- The f-string writes n, n + 1 and n + 2 in decimal one after another.
- For n = 0 that is `012`; `int` drops the leading zero, so a(0) = 12. For n
  ≥ 1 there is no leading zero and `int` changes nothing.
- `while[print(…)]:` is always true (the list `[None]` is not empty), and
  `n+=1` moves on.

**Notes**

- Printing 12 first and starting the loop at n = 1 without `int` is 5 bytes
  longer, and `{n or''}` instead of `int(…)` ties at 44; updating n inside
  the f-string with a walrus, `{(n:=n+1)}`, is 1 byte longer.
- Exact, correct for every n. The b-file has 1001 terms (n = 0 to 1000); the
  bar is the whole b-file, printed in a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001703), CC BY-SA 4.0.
