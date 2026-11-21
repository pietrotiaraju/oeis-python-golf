# A002138

> 6th powers written backwards.
> — [OEIS A002138](https://oeis.org/A002138)

Offset 0: 0, 1, 46, 927, 6904, 52651, 65664, 946711, 441262, 144135, 1, 1651771, …

### Python 3 — 43 bytes

```python
n=0
while[print(int(str(n**6)[::-1]))]:n+=1
```

**How it works**

- `str(n**6)[::-1]` reads the decimal digits of n^6 backwards, and `int`
  drops the leading zeros that the trailing zeros of n^6 become, so 10^6
  gives 1, as in the data. From n = 0, which gives 0.

**Notes**

- `f'{n**6}'` is as long as `str(n**6)`.
- Exact integer arithmetic, right for every n. The b-file has 10001 terms;
  the bar is the whole b-file in 60 s, a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002138), CC BY-SA 4.0.
