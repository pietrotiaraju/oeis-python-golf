# A002118

> 5th powers written backwards.
> — [OEIS A002118](https://oeis.org/A002118)

Offset 0: 0, 1, 23, 342, 4201, 5213, 6777, 70861, 86723, 94095, 1, 150161, …

### Python 3 — 43 bytes

```python
n=0
while[print(int(str(n**5)[::-1]))]:n+=1
```

**How it works**

- `str(n**5)[::-1]` reads the decimal digits of n^5 backwards, and `int`
  drops the leading zeros that the trailing zeros of n^5 become, so 10^5
  gives 1, as in the data. From n = 0, which gives 0.

**Notes**

- `f'{n**5}'` is as long as `str(n**5)`.
- Exact integer arithmetic, right for every n. The b-file has 1001 terms;
  the bar is the whole b-file in 60 s, a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002118), CC BY-SA 4.0.
