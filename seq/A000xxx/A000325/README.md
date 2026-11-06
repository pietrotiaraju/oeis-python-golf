# A000325

> a(n) = 2^n - n.
> — [OEIS A000325](https://oeis.org/A000325)

Offset 0: 1, 1, 2, 5, 12, 27, 58, 121, 248, 503, 1014, 2037, 4084, …

### Python 3 — 29 bytes

```python
n=0
while[print(2**n-n)]:n+=1
```

**How it works**

- The [A000027](../A000027/) counter, printing the closed form 2**n-n
  (`**` binds tighter than `-`, so no parentheses).
- `print(…)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true and the body `n+=1` moves to
  the next n.

**Notes**

- Exact integers, so every term is right.
- The recurrence a(n+1) = 2·a(n) + n − 1 still needs the counter n, so it
  costs a second variable and more bytes. `(1<<n)-n` needs parentheses and is
  2 bytes longer than `2**n-n`, and keeping p = 2ⁿ beside n is longer too.
- a(14285) is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not counted as
  a failure.
- The b-file has 201 terms (n = 0 to 200) and all of them print at once; the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000325), CC BY-SA 4.0.
