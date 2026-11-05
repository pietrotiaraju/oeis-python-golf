# A000030

> Initial digit of n.
> — [OEIS A000030](https://oeis.org/A000030)

Offset 0: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, …

### Python 3 — 31 bytes

```python
n=0
while[print("%.1s"%n)]:n+=1
```

**How it works**

- `"%.1s"%n` formats n with `%s`, which calls `str(n)`, and the precision
  `.1` keeps at most one character of that string: the first digit. For
  n = 0 it is `"0"`, so a(0) = 0 comes out with no special case.
- The loop is the [A000027](../A000027/) one, `while[print(…)]:n+=1`: `print`
  returns `None`, `[None]` is a non-empty list and so true, and the body steps
  n. Starting from `n=0` matches the offset.

**Notes**

- `str(n)[0]` and `f"{n}"[0]` are both one byte longer than `"%.1s"%n`, so
  the program would be 32 bytes. `f"{n!s:.1}"` is 34. `f"{n:.1}"` raises
  `ValueError: Precision not allowed in integer format specifier`: the
  truncating precision only works on strings, hence the `s` (or `!s`).
- `while 1:print("%.1s"%n);n+=1` is 32 bytes.
- Building the sequence from its second definition (0, then each digit 1–9
  repeated 1, 10, 100, … times) needs a digit loop inside the power loop and
  comes out far longer.
- Exact: `str(n)` is exact for every n, and n would need 4300 digits to hit the
  int-to-str limit, which no run gets close to. The whole b-file (10 001
  terms) prints in well under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000030), CC BY-SA 4.0.
