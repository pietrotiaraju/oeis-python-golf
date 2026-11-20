# A002108

> 4th powers written backwards.
> — [OEIS A002108](https://oeis.org/A002108)

Offset 1: 1, 61, 18, 652, 526, 6921, 1042, 6904, 1656, 1, 14641, 63702, 16582, …

### Python 3 — 43 bytes

```python
n=1
while[print(int(str(n**4)[::-1]))]:n+=1
```

**How it works**

- `str(n**4)[::-1]` reads the decimal digits of n^4 backwards, and `int`
  drops the leading zeros that the trailing zeros of n^4 become, so 10^4
  gives 1, as in the data. n starts at 1, the offset.

**Notes**

- `f'{n**4}'` is as long as `str(n**4)`.
- Exact integer arithmetic, right for every n. The b-file has 1000 terms;
  the bar is the whole b-file in 60 s, a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002108), CC BY-SA 4.0.
