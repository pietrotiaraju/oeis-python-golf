# A000290

> The squares: a(n) = n^2.
> — [OEIS A000290](https://oeis.org/A000290)

Offset 0: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, …

### Python 3 — 26 bytes

```python
n=0
while[print(n*n)]:n+=1
```

**How it works**

- The [A000027](../A000027/) counter, printing n·n instead of n.
- `print(n*n)` runs in the loop condition. It returns `None`, and `[None]` is
  a non-empty list, so the condition is always true and the body `n+=1`
  moves to the next n.

**Notes**

- `n**2` is the same length as `n*n`, and `while 1:print(n*n);n+=1` is one
  byte longer.
- Summing odd numbers, `s=0;k=1` + `while[print(s)]:s+=k;k+=2`, is 33 bytes.
- Exact integers, so every term is right; the 4300-digit int-to-str limit
  would only be reached near n = 10^2150.
- The b-file has 10001 terms (n = 0 to 10000) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 26 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000290), CC BY-SA 4.0.
