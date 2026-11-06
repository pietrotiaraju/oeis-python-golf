# A000400

> Powers of 6: a(n) = 6^n.
> — [OEIS A000400](https://oeis.org/A000400)

Offset 0: 1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=6
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body multiplies `n` by 6, so the loop prints 1, 6, 36, 216, … forever.
  It is the [A000079](../A000079/) and [A000244](../A000244/) loop with
  `n*=6`.

**Notes**

- `n=1` + `while 1:print(n);n*=6` is 25 bytes.
- Exact integer arithmetic, so the program is right for every n. a(5526) is
  the first term with more than 4300 digits, so Python 3.11+ stops there with
  a `ValueError` from the int-to-str limit, which is not counted as a failure.
- The b-file has 101 terms (n = 0 to 100) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000400), CC BY-SA 4.0.
