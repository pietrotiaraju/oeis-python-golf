# A002239

> 9th powers written backwards.
> — [OEIS A002239](https://oeis.org/A002239)

Offset 0: 0, 1, 215, 38691, 441262, 5213591, 69677001, 70635304, 827712431, …

### Python 3 — 43 bytes

```python
n=0
while[print(int(str(n**9)[::-1]))]:n+=1
```

**How it works**

- `str(n**9)[::-1]` is the decimal digits of n^9 in reverse order, and
  `int` reads them back as a number, which drops the leading zeros that
  the trailing zeros of n^9 leave behind: 10^9 written backwards is 1,
  as a(10) = 1 in the entry.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends; `n+=1` steps through n = 0, 1, 2, … Exact integers, so it is
  right for every n.

**Notes**

- `f'{n**9}'` is as long as `str(n**9)`, and `'%d'%n**9` needs
  parentheses before the slice. Stripping the zeros with `.lstrip('0')`
  is longer and prints an empty line for n = 0.
- n^9 has at most 4300 digits until n ≈ 10^477, so the
  int-to-str limit of Python 3.11+ never matters here.
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002239), CC BY-SA 4.0.
