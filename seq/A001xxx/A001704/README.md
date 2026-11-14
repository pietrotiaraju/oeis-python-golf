# A001704

> a(n) = n concatenated with n + 1.
> — [OEIS A001704](https://oeis.org/A001704)

Offset 1: 12, 23, 34, 45, 56, 67, 78, 89, 910, 1011, 1112, 1213, 1314, 1415, …

### Python 3 — 34 bytes

```python
n=1
while[print(f"{n}{n+1}")]:n+=1
```

**How it works**

- The f-string writes n and n + 1 in decimal one after the other; printing
  the string prints the concatenated number.
- `while[print(…)]:` is always true (the list `[None]` is not empty), and
  `n+=1` moves on. n starts at 1, the offset, so no term has a leading zero.

**Notes**

- Updating n inside the f-string with a walrus, `while
  1:print(f"{n}{(n:=n+1)}")`, is 1 byte longer.
- Exact, correct for every n. The b-file has 25000 terms; the bar is the
  whole b-file, printed in under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001704), CC BY-SA 4.0.
