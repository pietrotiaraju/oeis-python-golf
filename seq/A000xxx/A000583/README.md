# A000583

> Fourth powers: a(n) = n^4.
> — [OEIS A000583](https://oeis.org/A000583)

Offset 0: 0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**4)]:n+=1
```

**How it works**

- The [A000027](../A000027/) counter, printing n⁴ instead of n.
- `print(n**4)` runs in the loop condition. It returns `None`, and `[None]` is
  a non-empty list, so the condition is always true and the body `n+=1`
  moves to the next n.

**Notes**

- `while 1:print(n**4);n+=1` is 28 bytes, and `n*n*n*n` is 3 bytes longer
  than `n**4`.
- Exact integers, so every term is right; the 4300-digit int-to-str limit
  would only be reached near n = 10^1075.
- The b-file has 1001 terms (n = 0 to 1000) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000583), CC BY-SA 4.0.
