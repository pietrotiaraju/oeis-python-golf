# A000038

> Twice A000007.
> — [OEIS A000038](https://oeis.org/A000038)

Offset 0: 2, 0, 0, 0, 0, …

a(0) = 2 and a(n) = 0 for n > 0: [A000007](../A000007/) with its 1 doubled.

### Python 3 — 23 bytes

```python
n=2
while[print(n)]:n=0
```

**How it works**

- It is the [A000007](../A000007/) program with `n=1` replaced by `n=2`.
- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body sets `n` to 0 after the first term, so 2 is printed once and 0
  forever after.

**Notes**

- `n=2` + `while 1:print(n);n=0` is 24 bytes; `print(2)` followed by the
  [A000004](../A000004/) loop is 25.
- The b-file has 10001 terms (n = 0 to 10000) and the whole of it prints
  instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 23 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000038), CC BY-SA 4.0.
