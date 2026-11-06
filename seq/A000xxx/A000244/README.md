# A000244

> Powers of 3: a(n) = 3^n.
> — [OEIS A000244](https://oeis.org/A000244)

Offset 0: 1, 3, 9, 27, 81, 243, 729, 2187, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=3
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body triples `n`, so the loop prints 1, 3, 9, 27, … forever. It is the
  [A000079](../A000079/) loop with `n*=2` replaced by `n*=3`.

**Notes**

- `n=1` + `while 1:print(n);n*=3` is 25 bytes.
- Exact integer arithmetic, so the program is right for every n. a(9013) is
  the first term with more than 4300 digits, so Python 3.11+ stops there with
  a `ValueError` from the int-to-str limit, which is not counted as a failure.
- The b-file has 201 terms (n = 0 to 200) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000244), CC BY-SA 4.0.
