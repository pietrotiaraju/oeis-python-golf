# A000302

> Powers of 4: a(n) = 4^n.
> — [OEIS A000302](https://oeis.org/A000302)

Offset 0: 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=4
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body multiplies `n` by 4, so the loop prints 1, 4, 16, 64, … forever. It
  is the [A000079](../A000079/) and [A000244](../A000244/) loop with `n*=4`.

**Notes**

- `n=1` + `while 1:print(n);n*=4` is 25 bytes, and a counter with
  `print(4**n)` or `print(1<<2*n)` is longer.
- Exact integer arithmetic, so the program is right for every n. a(7143) is
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
Sequences](https://oeis.org/A000302), CC BY-SA 4.0.
