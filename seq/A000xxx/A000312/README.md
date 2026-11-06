# A000312

> a(n) = n^n; number of labeled mappings from n points to themselves (endofunctions).
> — [OEIS A000312](https://oeis.org/A000312)

Offset 0: 1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**n)]:n+=1
```

**How it works**

- The [A000027](../A000027/) counter, printing n**n. Python defines
  `0**0` as 1, which is a(0), so the counter can start at 0 with no patch.
- `print(…)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true and the body `n+=1` moves to
  the next n.

**Notes**

- `while 1:print(n**n);n+=1` is one byte longer.
  [A000169](../A000169/) prints `n**~-n` from n = 1 with the same frame.
- Exact integers, so every term is right. a(1371) is the first term with more
  than 4300 digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure.
- The b-file has 386 terms (n = 0 to 385) and all of them print at once; the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000312), CC BY-SA 4.0.
