# A001283

> Triangle read by rows, in which row n consists of n(n+m) for m = 1 .. n-1.
> — [OEIS A001283](https://oeis.org/A001283)

Offset 2: 6, 12, 15, 20, 24, 28, 30, 35, 40, 45, 42, 48, 54, 60, 66, …

Row n (n ≥ 2) has n − 1 entries, n(n+1), n(n+2), …, n(2n−1).

### Python 3 — 46 bytes

```python
n=2;m=1
while[print(n*(n+m))]:m=m%~-n+1;n+=m<2
```

**How it works**

- One loop runs over all entries, with the row n and the index m.
  `~-n` is n − 1, so `m=m%~-n+1` turns m into m + 1 while m < n − 1, and
  into 1 after the last entry m = n − 1; `n+=m<2` moves to the next row
  exactly then.
- Row 2 has the single entry 2·3 = 6: with n = 2, m % 1 + 1 = 1 at once,
  so the loop goes on with n = 3, m = 1.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends. Exact integers, so every entry is right.

**Notes**

- Printing a whole row per pass is longer:
  `while[*map(print,range(n*n+n,2*n*n,n))]:n+=1` (the row is the range
  from n(n+1) below 2n² in steps of n) is 48 bytes, and
  `while[print(n*k)for k in range(n+1,2*n)]:n+=1` is 49.
- The b-file has 4950 terms (rows 2 to 100); the bar is the whole b-file
  in 60 s, which takes about 0.1 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001283), CC BY-SA 4.0.
