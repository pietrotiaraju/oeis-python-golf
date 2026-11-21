# A002140

> 7th powers written backwards.
> — [OEIS A002140](https://oeis.org/A002140)

Offset 0: 0, 1, 821, 7812, 48361, 52187, 639972, 345328, 2517902, 9692874, 1, …

### Python 3 — 43 bytes

```python
n=0
while[print(int(str(n**7)[::-1]))]:n+=1
```

**How it works**

- `str(n**7)[::-1]` reads the decimal digits of n^7 backwards, and `int`
  drops the leading zeros that the trailing zeros of n^7 become, so 10^7
  gives 1, as in the data. From n = 0, which gives 0.

**Notes**

- `f'{n**7}'` is as long as `str(n**7)`.
- Exact integer arithmetic, right for every n. The b-file has 10001 terms;
  the bar is the whole b-file in 60 s, a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002140), CC BY-SA 4.0.
