# A000584

> Fifth powers: a(n) = n^5.
> — [OEIS A000584](https://oeis.org/A000584)

Offset 0: 0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**5)]:n+=1
```

**How it works**

- The [A000027](../A000027/) counter, printing n⁵ instead of n.
- `print(n**5)` runs in the loop condition. It returns `None`, and `[None]` is
  a non-empty list, so the condition is always true and the body `n+=1`
  moves to the next n.

**Notes**

- `while 1:print(n**5);n+=1` is 28 bytes, and `n*n*n*n*n` is 5 bytes longer
  than `n**5`.
- Exact integers, so every term is right; the 4300-digit int-to-str limit
  would only be reached near n = 10^860.
- The b-file has 501 terms (n = 0 to 500) and all of them print at once; the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000584), CC BY-SA 4.0.
