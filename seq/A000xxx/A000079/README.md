# A000079

> Powers of 2: a(n) = 2^n.
> — [OEIS A000079](https://oeis.org/A000079)

Offset 0: 1, 2, 4, 8, 16, 32, 64, 128, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=2
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body doubles `n`, so the loop prints 1, 2, 4, 8, … forever. It is the
  [A000027](../A000027/) loop with `n+=1` replaced by `n*=2`.

**Notes**

- `n+=n` doubles `n` in the same 4 bytes. `n<<=1` and
  `n=1` + `while 1:print(n);n*=2` are 25 bytes.
- Exact integer arithmetic, so the program is right for every n. a(14285) is
  the first term with more than 4300 digits, so Python 3.11+ stops there with
  a `ValueError` from the int-to-str limit, which is not counted as a failure.
- The b-file has 1001 terms (n = 0 to 1000) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000079), CC BY-SA 4.0.
